// Copyright (C) 2021 Bosutech XXI S.L.
//
// nucliadb is offered under the AGPL v3.0 and as commercial software.
// For commercial licensing, contact us at info@nuclia.com.
//
// AGPL:
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Affero General Public License as
// published by the Free Software Foundation, either version 3 of the
// License, or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU Affero General Public License for more details.
//
// You should have received a copy of the GNU Affero General Public License
// along with this program. If not, see <http://www.gnu.org/licenses/>.

use std::fmt::Debug;
use std::fs::File;
use std::path::PathBuf;
use std::time::SystemTime;

use nucliadb_core::metrics;
use nucliadb_core::metrics::request_time;
use nucliadb_core::prelude::*;
use nucliadb_core::protos::prost::Message;
use nucliadb_core::protos::{
    DocumentScored, DocumentVectorIdentifier, SentenceMetadata, VectorSearchRequest,
    VectorSearchResponse,
};
use nucliadb_core::tracing::{self, *};

use super::{MaybeLocked, SET_LOCK};
use crate::data_point_provider::*;
use crate::formula::{Formula, LabelClause};

impl<'a> SearchRequest for (usize, &'a VectorSearchRequest, Formula) {
    fn with_duplicates(&self) -> bool {
        self.1.with_duplicates
    }
    fn get_filter(&self) -> &Formula {
        &self.2
    }
    fn get_query(&self) -> &[f32] {
        &self.1.vector
    }
    fn no_results(&self) -> usize {
        self.0
    }
}

pub struct VectorReaderService {
    rest_lock: File,
    rest: PathBuf,
    default: Reader,
}
impl Debug for VectorReaderService {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.debug_struct("VectorReaderService").finish()
    }
}

impl VectorReader for VectorReaderService {
    #[tracing::instrument(skip_all)]
    fn count(&self, vectorset: &str) -> NodeResult<usize> {
        let time = SystemTime::now();
        let some_reader = self.get_index(vectorset)?;
        let reader = some_reader.inner();
        let no_nodes = reader.number_of_nodes();
        let metrics = metrics::get_metrics();
        let took = time.elapsed().map(|i| i.as_secs_f64()).unwrap_or(f64::NAN);
        let metric = request_time::RequestTimeKey::vectors("count".to_string());
        metrics.record_request_time(metric, took);
        debug!("Ending at {took} ms");
        Ok(no_nodes)
    }
}
impl ReaderChild for VectorReaderService {
    type Request = VectorSearchRequest;
    type Response = VectorSearchResponse;
    #[tracing::instrument(skip_all)]
    fn search(&self, request: &Self::Request) -> NodeResult<Self::Response> {
        let time = SystemTime::now();

        let id = Some(&request.id);
        let offset = request.result_per_page * request.page_number;
        let total_to_get = offset + request.result_per_page;
        let offset = offset as usize;
        let total_to_get = total_to_get as usize;
        let mut formula = Formula::new();
        request
            .tags
            .iter()
            .cloned()
            .map(LabelClause::new)
            .for_each(|c| formula.extend(c));

        if let Ok(v) = time.elapsed().map(|s| s.as_millis()) {
            debug!("{id:?} - Searching: starts at {v} ms");
        }
        let search_request = (total_to_get, request, formula);
        let some_reader = self.get_index(&request.vector_set)?;
        let reader = some_reader.inner();
        let result = reader.search(&search_request)?;
        reader.schedule_update();
        if let Ok(v) = time.elapsed().map(|s| s.as_millis()) {
            debug!("{id:?} - Searching: ends at {v} ms");
        }

        if let Ok(v) = time.elapsed().map(|s| s.as_millis()) {
            debug!("{id:?} - Creating results: starts at {v} ms");
        }
        let documents = result
            .into_iter()
            .enumerate()
            .filter(|(idx, _)| *idx >= offset)
            .map(|(_, v)| v)
            .flat_map(DocumentScored::try_from)
            .collect::<Vec<_>>();
        if let Ok(v) = time.elapsed().map(|s| s.as_millis()) {
            debug!("{id:?} - Creating results: ends at {v} ms");
        }

        let metrics = metrics::get_metrics();
        let took = time.elapsed().map(|i| i.as_secs_f64()).unwrap_or(f64::NAN);
        let metric = request_time::RequestTimeKey::vectors("search".to_string());
        metrics.record_request_time(metric, took);
        debug!("{id:?} - Ending at {took} ms");

        Ok(VectorSearchResponse {
            documents,
            page_number: request.page_number,
            result_per_page: request.result_per_page,
        })
    }
    #[tracing::instrument(skip_all)]
    fn stored_ids(&self) -> NodeResult<Vec<String>> {
        let time = SystemTime::now();
        let result = self.default.keys()?;
        if let Ok(v) = time.elapsed().map(|s| s.as_millis()) {
            debug!("Ending at {v} ms")
        }
        Ok(result)
    }
}

impl TryFrom<Neighbour> for DocumentScored {
    type Error = String;
    fn try_from(neighbour: Neighbour) -> Result<Self, Self::Error> {
        let id = std::str::from_utf8(neighbour.id());
        let metadata = neighbour.metadata().map(SentenceMetadata::decode);
        let labels = neighbour.labels();
        let Ok(id) = id.map(|i| i.to_string())else {
            return Err("Id could not be decoded".to_string())
        };
        let Ok(metadata) = metadata.transpose() else {
            return Err("The metadata could not be decoded".to_string());
        };
        Ok(DocumentScored {
            labels,
            metadata,
            doc_id: Some(DocumentVectorIdentifier { id }),
            score: neighbour.score(),
        })
    }
}

impl VectorReaderService {
    fn get_index<'a>(&'a self, name: &str) -> NodeResult<MaybeLocked<'a, Reader>> {
        if name.is_empty() {
            Ok(MaybeLocked::no_lock(&self.default))
        } else {
            let path = self.rest.join(name);
            let reader = Index::open(&path).and_then(|i| i.reader())?;
            Ok(MaybeLocked::with_shared_lock(reader, &self.rest_lock)?)
        }
    }
    #[tracing::instrument(skip_all)]
    pub fn start(config: &VectorConfig) -> NodeResult<Self> {
        if !config.path.exists() {
            return Err(node_error!("Shard does not exist".to_string()));
        }
        let rest = config.vectorset.clone();
        let rest_path = rest.join(SET_LOCK);
        let default = Index::open(&config.path).and_then(|i| Index::reader(&i))?;
        let rest_lock = File::open(&rest_path).or_else(|_| File::create(&rest_path))?;
        Ok(VectorReaderService {
            default,
            rest,
            rest_lock,
        })
    }
}

#[cfg(test)]
mod tests {
    use std::collections::HashMap;

    use nucliadb_core::protos::resource::ResourceStatus;
    use nucliadb_core::protos::{
        IndexParagraph, IndexParagraphs, Resource, ResourceId, VectorSentence, VectorSimilarity,
    };
    use tempfile::TempDir;

    use super::*;
    use crate::service::writer::VectorWriterService;

    #[test]
    fn test_new_vector_reader() {
        let dir = TempDir::new().unwrap();
        let vsc = VectorConfig {
            similarity: Some(VectorSimilarity::Cosine),
            path: dir.path().join("vectors"),
            vectorset: dir.path().join("vectorset"),
        };
        let raw_sentences = [
            ("DOC/KEY/1/1".to_string(), vec![1.0, 3.0, 4.0]),
            ("DOC/KEY/1/2".to_string(), vec![2.0, 4.0, 5.0]),
            ("DOC/KEY/1/3".to_string(), vec![3.0, 5.0, 6.0]),
            ("DOC/KEY/1/4".to_string(), vec![3.0, 5.0, 6.0]),
        ];
        let resource_id = ResourceId {
            shard_id: "DOC".to_string(),
            uuid: "DOC/KEY".to_string(),
        };

        let mut sentences = HashMap::new();
        for (key, vector) in raw_sentences {
            let vector = VectorSentence {
                vector,
                ..Default::default()
            };
            sentences.insert(key, vector);
        }
        let paragraph = IndexParagraph {
            start: 0,
            end: 0,
            sentences,
            field: "".to_string(),
            labels: vec!["1".to_string()],
            index: 3,
            split: "".to_string(),
            repeated_in_field: false,
            metadata: None,
        };
        let paragraphs = IndexParagraphs {
            paragraphs: HashMap::from([("DOC/KEY/1".to_string(), paragraph)]),
        };
        let resource = Resource {
            resource: Some(resource_id),
            metadata: None,
            texts: HashMap::with_capacity(0),
            status: ResourceStatus::Processed as i32,
            labels: vec!["2".to_string()],
            paragraphs: HashMap::from([("DOC/KEY".to_string(), paragraphs)]),
            paragraphs_to_delete: vec![],
            sentences_to_delete: vec![],
            relations_to_delete: vec![],
            relations: vec![],
            vectors: HashMap::default(),
            vectors_to_delete: HashMap::default(),
            shard_id: "DOC".to_string(),
        };
        // insert - delete - insert sequence
        let mut writer = VectorWriterService::start(&vsc).unwrap();
        let res = writer.set_resource(&resource);
        assert!(res.is_ok());
        let reader = VectorReaderService::start(&vsc).unwrap();
        let request = VectorSearchRequest {
            id: "".to_string(),
            vector_set: "".to_string(),
            vector: vec![4.0, 6.0, 7.0],
            tags: vec!["1".to_string()],
            page_number: 0,
            result_per_page: 20,
            with_duplicates: true,
            ..Default::default()
        };
        let result = reader.search(&request).unwrap();
        assert_eq!(result.documents.len(), 4);

        let request = VectorSearchRequest {
            id: "".to_string(),
            vector_set: "".to_string(),
            vector: vec![4.0, 6.0, 7.0],
            tags: vec!["1".to_string()],
            page_number: 0,
            result_per_page: 20,
            with_duplicates: false,
            ..Default::default()
        };
        let result = reader.search(&request).unwrap();
        let no_nodes = reader.count("").unwrap();
        assert_eq!(no_nodes, 4);
        assert_eq!(result.documents.len(), 3);
    }
}