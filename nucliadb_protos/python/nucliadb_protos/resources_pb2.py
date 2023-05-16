# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nucliadb_protos/resources.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nucliadb_protos import utils_pb2 as nucliadb__protos_dot_utils__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2

from nucliadb_protos.utils_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fnucliadb_protos/resources.proto\x12\tresources\x1a\x1bnucliadb_protos/utils.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xf0\x02\n\tCloudFile\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\x05\x12\x14\n\x0c\x63ontent_type\x18\x03 \x01(\t\x12\x13\n\x0b\x62ucket_name\x18\x04 \x01(\t\x12+\n\x06source\x18\x05 \x01(\x0e\x32\x1b.resources.CloudFile.Source\x12\x10\n\x08\x66ilename\x18\x06 \x01(\t\x12\x15\n\rresumable_uri\x18\x07 \x01(\t\x12\x0e\n\x06offset\x18\x08 \x01(\x03\x12\x12\n\nupload_uri\x18\t \x01(\t\x12\r\n\x05parts\x18\n \x03(\t\x12\x0f\n\x07old_uri\x18\x0b \x01(\t\x12\x12\n\nold_bucket\x18\x0c \x01(\t\x12\x0b\n\x03md5\x18\r \x01(\t\"b\n\x06Source\x12\t\n\x05\x46LAPS\x10\x00\x12\x07\n\x03GCS\x10\x01\x12\x06\n\x02S3\x10\x02\x12\t\n\x05LOCAL\x10\x03\x12\x0c\n\x08\x45XTERNAL\x10\x04\x12\t\n\x05\x45MPTY\x10\x05\x12\n\n\x06\x45XPORT\x10\x06\x12\x0c\n\x08POSTGRES\x10\x07\"\xa0\x04\n\x05\x42\x61sic\x12\x0c\n\x04slug\x18\x01 \x01(\t\x12\x0c\n\x04icon\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0f\n\x07summary\x18\x04 \x01(\t\x12\x11\n\tthumbnail\x18\x05 \x01(\t\x12\x0e\n\x06layout\x18\x06 \x01(\t\x12+\n\x07\x63reated\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08modified\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12%\n\x08metadata\x18\t \x01(\x0b\x32\x13.resources.Metadata\x12-\n\x0cusermetadata\x18\n \x01(\x0b\x32\x17.resources.UserMetadata\x12\x33\n\rfieldmetadata\x18\x0b \x03(\x0b\x32\x1c.resources.UserFieldMetadata\x12\x35\n\x10\x63omputedmetadata\x18\x0f \x01(\x0b\x32\x1b.resources.ComputedMetadata\x12\x0c\n\x04uuid\x18\x0c \x01(\t\x12\x0e\n\x06labels\x18\r \x03(\t\x12\x12\n\nlast_seqid\x18\x0e \x01(\x03\x12\x18\n\x10last_account_seq\x18# \x01(\x03\x12)\n\x05queue\x18$ \x01(\x0e\x32\x1a.resources.Basic.QueueType\"$\n\tQueueType\x12\x0b\n\x07PRIVATE\x10\x00\x12\n\n\x06SHARED\x10\x01\"\x81\x03\n\x06Origin\x12(\n\x06source\x18\x01 \x01(\x0e\x32\x18.resources.Origin.Source\x12\x11\n\tsource_id\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12+\n\x07\x63reated\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08modified\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\x08metadata\x18\x06 \x03(\x0b\x32\x1f.resources.Origin.MetadataEntry\x12\x0c\n\x04tags\x18\x07 \x03(\t\x12\x14\n\x0c\x63olaborators\x18\x08 \x03(\t\x12\x10\n\x08\x66ilename\x18\t \x01(\t\x12\x0f\n\x07related\x18\n \x03(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\'\n\x06Source\x12\x07\n\x03WEB\x10\x00\x12\x0b\n\x07\x44\x45SKTOP\x10\x01\x12\x07\n\x03\x41PI\x10\x02\"2\n\x05\x45xtra\x12)\n\x08metadata\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"/\n\tRelations\x12\"\n\trelations\x18\x01 \x03(\x0b\x32\x0f.utils.Relation\"\xb1\x01\n\x0eMessageContent\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x30\n\x06\x66ormat\x18\x02 \x01(\x0e\x32 .resources.MessageContent.Format\x12)\n\x0b\x61ttachments\x18\x04 \x03(\x0b\x32\x14.resources.CloudFile\"4\n\x06\x46ormat\x12\t\n\x05PLAIN\x10\x00\x12\x08\n\x04HTML\x10\x01\x12\x0c\n\x08MARKDOWN\x10\x02\x12\x07\n\x03RST\x10\x03\"\x8c\x01\n\x07Message\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03who\x18\x02 \x01(\t\x12\n\n\x02to\x18\x03 \x03(\t\x12*\n\x07\x63ontent\x18\x04 \x01(\x0b\x32\x19.resources.MessageContent\x12\r\n\x05ident\x18\x05 \x01(\t\"4\n\x0c\x43onversation\x12$\n\x08messages\x18\x01 \x03(\x0b\x32\x12.resources.Message\"?\n\x11\x46ieldConversation\x12\r\n\x05pages\x18\x01 \x01(\x05\x12\x0c\n\x04size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\":\n\x0eNestedPosition\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x03\x12\x0c\n\x04page\x18\x03 \x01(\x03\"B\n\x12NestedListPosition\x12,\n\tpositions\x18\x01 \x03(\x0b\x32\x19.resources.NestedPosition\"\xb9\x08\n\x11\x46ileExtractedData\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x0b\n\x03md5\x18\x02 \x01(\t\x12<\n\x08metadata\x18\x03 \x03(\x0b\x32*.resources.FileExtractedData.MetadataEntry\x12\x38\n\x06nested\x18\x04 \x03(\x0b\x32(.resources.FileExtractedData.NestedEntry\x12G\n\x0e\x66ile_generated\x18\x05 \x03(\x0b\x32/.resources.FileExtractedData.FileGeneratedEntry\x12N\n\x12\x66ile_rows_previews\x18\x06 \x03(\x0b\x32\x32.resources.FileExtractedData.FileRowsPreviewsEntry\x12*\n\x0c\x66ile_preview\x18\x07 \x01(\x0b\x32\x14.resources.CloudFile\x12\x31\n\x13\x66ile_pages_previews\x18\x08 \x01(\x0b\x32\x14.resources.FilePages\x12,\n\x0e\x66ile_thumbnail\x18\t \x01(\x0b\x32\x14.resources.CloudFile\x12\r\n\x05\x66ield\x18\n \x01(\t\x12\x0c\n\x04icon\x18\x0b \x01(\t\x12M\n\x0fnested_position\x18\x0c \x03(\x0b\x32\x30.resources.FileExtractedData.NestedPositionEntryB\x02\x18\x01\x12R\n\x14nested_list_position\x18\r \x03(\x0b\x32\x34.resources.FileExtractedData.NestedListPositionEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a-\n\x0bNestedEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aJ\n\x12\x46ileGeneratedEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.resources.CloudFile:\x02\x38\x01\x1aO\n\x15\x46ileRowsPreviewsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.resources.RowsPreview:\x02\x38\x01\x1aP\n\x13NestedPositionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.resources.NestedPosition:\x02\x38\x01\x1aX\n\x17NestedListPositionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.resources.NestedListPosition:\x02\x38\x01\"\x92\x03\n\x11LinkExtractedData\x12(\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08language\x18\x02 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\x12<\n\x08metadata\x18\x05 \x03(\x0b\x32*.resources.LinkExtractedData.MetadataEntry\x12,\n\x0elink_thumbnail\x18\x06 \x01(\x0b\x32\x14.resources.CloudFile\x12*\n\x0clink_preview\x18\x07 \x01(\x0b\x32\x14.resources.CloudFile\x12\r\n\x05\x66ield\x18\x08 \x01(\t\x12(\n\nlink_image\x18\t \x01(\x0b\x32\x14.resources.CloudFile\x12\x13\n\x0b\x64\x65scription\x18\n \x01(\t\x12\x0c\n\x04type\x18\x0b \x01(\t\x12\r\n\x05\x65mbed\x18\x0c \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x95\x01\n\x14\x45xtractedTextWrapper\x12$\n\x04\x62ody\x18\x01 \x01(\x0b\x32\x14.utils.ExtractedTextH\x00\x12$\n\x04\x66ile\x18\x02 \x01(\x0b\x32\x14.resources.CloudFileH\x00\x12!\n\x05\x66ield\x18\x03 \x01(\x0b\x32\x12.resources.FieldIDB\x0e\n\x0c\x66ile_or_data\"\x9a\x01\n\x17\x45xtractedVectorsWrapper\x12&\n\x07vectors\x18\x01 \x01(\x0b\x32\x13.utils.VectorObjectH\x00\x12$\n\x04\x66ile\x18\x02 \x01(\x0b\x32\x14.resources.CloudFileH\x00\x12!\n\x05\x66ield\x18\x03 \x01(\x0b\x32\x12.resources.FieldIDB\x0e\n\x0c\x66ile_or_data\"\xfd\x01\n\x12UserVectorsWrapper\x12%\n\x07vectors\x18\x01 \x01(\x0b\x32\x14.utils.UserVectorSet\x12M\n\x11vectors_to_delete\x18\r \x03(\x0b\x32\x32.resources.UserVectorsWrapper.VectorsToDeleteEntry\x12!\n\x05\x66ield\x18\x03 \x01(\x0b\x32\x12.resources.FieldID\x1aN\n\x14VectorsToDeleteEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.utils.UserVectorsList:\x02\x38\x01\"3\n\x08Sentence\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x05\x12\x0b\n\x03key\x18\x03 \x01(\t\"\xdb\x02\n\tParagraph\x12\r\n\x05start\x18\x01 \x01(\r\x12\x0b\n\x03\x65nd\x18\x02 \x01(\r\x12\x15\n\rstart_seconds\x18\x03 \x03(\r\x12\x13\n\x0b\x65nd_seconds\x18\x04 \x03(\r\x12\x30\n\x04kind\x18\x05 \x01(\x0e\x32\".resources.Paragraph.TypeParagraph\x12\x32\n\x0f\x63lassifications\x18\x06 \x03(\x0b\x32\x19.resources.Classification\x12&\n\tsentences\x18\x07 \x03(\x0b\x32\x13.resources.Sentence\x12\x0b\n\x03key\x18\x08 \x01(\t\x12\x0c\n\x04text\x18\t \x01(\t\"]\n\rTypeParagraph\x12\x08\n\x04TEXT\x10\x00\x12\x07\n\x03OCR\x10\x01\x12\r\n\tINCEPTION\x10\x02\x12\x0f\n\x0b\x44\x45SCRIPTION\x10\x03\x12\x0e\n\nTRANSCRIPT\x10\x04\x12\t\n\x05TITLE\x10\x05\"&\n\x08Position\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x03\"B\n\tPositions\x12%\n\x08position\x18\x01 \x03(\x0b\x32\x13.resources.Position\x12\x0e\n\x06\x65ntity\x18\x02 \x01(\t\"\x9d\x05\n\rFieldMetadata\x12\r\n\x05links\x18\x01 \x03(\t\x12(\n\nparagraphs\x18\x02 \x03(\x0b\x32\x14.resources.Paragraph\x12.\n\x03ner\x18\x03 \x03(\x0b\x32!.resources.FieldMetadata.NerEntry\x12\x32\n\x0f\x63lassifications\x18\x04 \x03(\x0b\x32\x19.resources.Classification\x12.\n\nlast_index\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x12last_understanding\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0clast_extract\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0clast_summary\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\tthumbnail\x18\t \x01(\x0b\x32\x14.resources.CloudFile\x12\x10\n\x08language\x18\n \x01(\t\x12\x0f\n\x07summary\x18\x0b \x01(\t\x12:\n\tpositions\x18\x0c \x03(\x0b\x32\'.resources.FieldMetadata.PositionsEntry\x12\'\n\trelations\x18\r \x03(\x0b\x32\x14.resources.Relations\x1a*\n\x08NerEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x46\n\x0ePositionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.resources.Positions:\x02\x38\x01\"\xf8\x01\n\x15\x46ieldComputedMetadata\x12*\n\x08metadata\x18\x01 \x01(\x0b\x32\x18.resources.FieldMetadata\x12K\n\x0esplit_metadata\x18\x02 \x03(\x0b\x32\x33.resources.FieldComputedMetadata.SplitMetadataEntry\x12\x16\n\x0e\x64\x65leted_splits\x18\x03 \x03(\t\x1aN\n\x12SplitMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.resources.FieldMetadata:\x02\x38\x01\"u\n\x1c\x46ieldComputedMetadataWrapper\x12\x32\n\x08metadata\x18\x01 \x01(\x0b\x32 .resources.FieldComputedMetadata\x12!\n\x05\x66ield\x18\x04 \x01(\x0b\x32\x12.resources.FieldID\"\x9c\x02\n\x08Metadata\x12\x33\n\x08metadata\x18\x01 \x03(\x0b\x32!.resources.Metadata.MetadataEntry\x12\x10\n\x08language\x18\x02 \x01(\t\x12\x11\n\tlanguages\x18\x03 \x03(\t\x12\x0e\n\x06useful\x18\x04 \x01(\x08\x12*\n\x06status\x18\x05 \x01(\x0e\x32\x1a.resources.Metadata.Status\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"I\n\x06Status\x12\x0b\n\x07PENDING\x10\x00\x12\r\n\tPROCESSED\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\x0b\n\x07\x42LOCKED\x10\x03\x12\x0b\n\x07\x45XPIRED\x10\x04\"\x89\x01\n\tFieldText\x12\x0c\n\x04\x62ody\x18\x01 \x01(\t\x12+\n\x06\x66ormat\x18\x02 \x01(\x0e\x32\x1b.resources.FieldText.Format\x12\x0b\n\x03md5\x18\x03 \x01(\t\"4\n\x06\x46ormat\x12\t\n\x05PLAIN\x10\x00\x12\x08\n\x04HTML\x10\x01\x12\x07\n\x03RST\x10\x02\x12\x0c\n\x08MARKDOWN\x10\x03\"\x9c\x02\n\x05\x42lock\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\x0c\n\x04\x63ols\x18\x03 \x01(\x05\x12\x0c\n\x04rows\x18\x04 \x01(\x05\x12(\n\x04type\x18\x05 \x01(\x0e\x32\x1a.resources.Block.TypeBlock\x12\r\n\x05ident\x18\x06 \x01(\t\x12\x0f\n\x07payload\x18\x07 \x01(\t\x12\"\n\x04\x66ile\x18\x08 \x01(\x0b\x32\x14.resources.CloudFile\"s\n\tTypeBlock\x12\t\n\x05TITLE\x10\x00\x12\x0f\n\x0b\x44\x45SCRIPTION\x10\x01\x12\x0c\n\x08RICHTEXT\x10\x02\x12\x08\n\x04TEXT\x10\x03\x12\x0f\n\x0b\x41TTACHMENTS\x10\x04\x12\x0c\n\x08\x43OMMENTS\x10\x05\x12\x13\n\x0f\x43LASSIFICATIONS\x10\x06\"\x9e\x01\n\rLayoutContent\x12\x34\n\x06\x62locks\x18\x01 \x03(\x0b\x32$.resources.LayoutContent.BlocksEntry\x12\x16\n\x0e\x64\x65leted_blocks\x18\x02 \x03(\t\x1a?\n\x0b\x42locksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.resources.Block:\x02\x38\x01\"|\n\x0b\x46ieldLayout\x12&\n\x04\x62ody\x18\x01 \x01(\x0b\x32\x18.resources.LayoutContent\x12-\n\x06\x66ormat\x18\x02 \x01(\x0e\x32\x1d.resources.FieldLayout.Format\"\x16\n\x06\x46ormat\x12\x0c\n\x08NUCLIAv1\x10\x00\"[\n\x0e\x43lassification\x12\x10\n\x08labelset\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x19\n\x11\x63\x61ncelled_by_user\x18\x03 \x01(\x08\x12\r\n\x05split\x18\x04 \x01(\t\"f\n\x0cUserMetadata\x12\x32\n\x0f\x63lassifications\x18\x01 \x03(\x0b\x32\x19.resources.Classification\x12\"\n\trelations\x18\x03 \x03(\x0b\x32\x0f.utils.Relation\"m\n\x14\x46ieldClassifications\x12!\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x12.resources.FieldID\x12\x32\n\x0f\x63lassifications\x18\x02 \x03(\x0b\x32\x19.resources.Classification\"R\n\x10\x43omputedMetadata\x12>\n\x15\x66ield_classifications\x18\x01 \x03(\x0b\x32\x1f.resources.FieldClassifications\"p\n\nTokenSplit\x12\r\n\x05token\x18\x01 \x01(\t\x12\r\n\x05klass\x18\x02 \x01(\t\x12\r\n\x05start\x18\x03 \x01(\r\x12\x0b\n\x03\x65nd\x18\x04 \x01(\r\x12\x19\n\x11\x63\x61ncelled_by_user\x18\x05 \x01(\x08\x12\r\n\x05split\x18\x06 \x01(\t\"V\n\x13ParagraphAnnotation\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x32\n\x0f\x63lassifications\x18\x02 \x03(\x0b\x32\x19.resources.Classification\"\x90\x01\n\x11UserFieldMetadata\x12$\n\x05token\x18\x01 \x03(\x0b\x32\x15.resources.TokenSplit\x12\x32\n\nparagraphs\x18\x02 \x03(\x0b\x32\x1e.resources.ParagraphAnnotation\x12!\n\x05\x66ield\x18\x03 \x01(\x0b\x32\x12.resources.FieldID\"\x90\x03\n\tFieldLink\x12)\n\x05\x61\x64\x64\x65\x64\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x07headers\x18\x02 \x03(\x0b\x32!.resources.FieldLink.HeadersEntry\x12\x32\n\x07\x63ookies\x18\x03 \x03(\x0b\x32!.resources.FieldLink.CookiesEntry\x12\x0b\n\x03uri\x18\x04 \x01(\t\x12\x10\n\x08language\x18\x05 \x01(\t\x12<\n\x0clocalstorage\x18\x06 \x03(\x0b\x32&.resources.FieldLink.LocalstorageEntry\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a.\n\x0c\x43ookiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x33\n\x11LocalstorageEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x18\n\x07Keyword\x12\r\n\x05value\x18\x01 \x01(\t\"7\n\x0f\x46ieldKeywordset\x12$\n\x08keywords\x18\x01 \x03(\x0b\x32\x12.resources.Keyword\":\n\rFieldDatetime\x12)\n\x05value\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xd3\x02\n\tFieldFile\x12)\n\x05\x61\x64\x64\x65\x64\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\"\n\x04\x66ile\x18\x02 \x01(\x0b\x32\x14.resources.CloudFile\x12\x10\n\x08language\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x0b\n\x03url\x18\x05 \x01(\t\x12\x32\n\x07headers\x18\x06 \x03(\x0b\x32!.resources.FieldFile.HeadersEntry\x12\x32\n\x07\x63ookies\x18\x07 \x03(\x0b\x32!.resources.FieldFile.CookiesEntry\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a.\n\x0c\x43ookiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"3\n\x06\x45ntity\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0c\n\x04root\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\"\xa3\x01\n\x12\x46ieldLargeMetadata\x12#\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\x11.resources.Entity\x12\x39\n\x06tokens\x18\x02 \x03(\x0b\x32).resources.FieldLargeMetadata.TokensEntry\x1a-\n\x0bTokensEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"\x82\x02\n\x15LargeComputedMetadata\x12/\n\x08metadata\x18\x01 \x01(\x0b\x32\x1d.resources.FieldLargeMetadata\x12K\n\x0esplit_metadata\x18\x02 \x03(\x0b\x32\x33.resources.LargeComputedMetadata.SplitMetadataEntry\x12\x16\n\x0e\x64\x65leted_splits\x18\x03 \x03(\t\x1aS\n\x12SplitMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.resources.FieldLargeMetadata:\x02\x38\x01\"\xa9\x01\n\x1cLargeComputedMetadataWrapper\x12\x30\n\x04real\x18\x01 \x01(\x0b\x32 .resources.LargeComputedMetadataH\x00\x12$\n\x04\x66ile\x18\x02 \x01(\x0b\x32\x14.resources.CloudFileH\x00\x12!\n\x05\x66ield\x18\x03 \x01(\x0b\x32\x12.resources.FieldIDB\x0e\n\x0c\x66ile_or_data\"+\n\rPagePositions\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x03\"]\n\tFilePages\x12#\n\x05pages\x18\x01 \x03(\x0b\x32\x14.resources.CloudFile\x12+\n\tpositions\x18\x02 \x03(\x0b\x32\x18.resources.PagePositions\"\xdc\x01\n\x0bRowsPreview\x12\x32\n\x06sheets\x18\x01 \x03(\x0b\x32\".resources.RowsPreview.SheetsEntry\x1aL\n\x05Sheet\x12.\n\x04rows\x18\x01 \x03(\x0b\x32 .resources.RowsPreview.Sheet.Row\x1a\x13\n\x03Row\x12\x0c\n\x04\x63\x65ll\x18\x01 \x03(\t\x1aK\n\x0bSheetsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.resources.RowsPreview.Sheet:\x02\x38\x01\"B\n\x07\x46ieldID\x12(\n\nfield_type\x18\x01 \x01(\x0e\x32\x14.resources.FieldType\x12\r\n\x05\x66ield\x18\x02 \x01(\t*r\n\tFieldType\x12\x08\n\x04\x46ILE\x10\x00\x12\x08\n\x04LINK\x10\x01\x12\x0c\n\x08\x44\x41TETIME\x10\x02\x12\x0e\n\nKEYWORDSET\x10\x03\x12\x08\n\x04TEXT\x10\x04\x12\n\n\x06LAYOUT\x10\x05\x12\x0b\n\x07GENERIC\x10\x06\x12\x10\n\x0c\x43ONVERSATION\x10\x07P\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nucliadb_protos.resources_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ORIGIN_METADATAENTRY._options = None
  _ORIGIN_METADATAENTRY._serialized_options = b'8\001'
  _FILEEXTRACTEDDATA_METADATAENTRY._options = None
  _FILEEXTRACTEDDATA_METADATAENTRY._serialized_options = b'8\001'
  _FILEEXTRACTEDDATA_NESTEDENTRY._options = None
  _FILEEXTRACTEDDATA_NESTEDENTRY._serialized_options = b'8\001'
  _FILEEXTRACTEDDATA_FILEGENERATEDENTRY._options = None
  _FILEEXTRACTEDDATA_FILEGENERATEDENTRY._serialized_options = b'8\001'
  _FILEEXTRACTEDDATA_FILEROWSPREVIEWSENTRY._options = None
  _FILEEXTRACTEDDATA_FILEROWSPREVIEWSENTRY._serialized_options = b'8\001'
  _FILEEXTRACTEDDATA_NESTEDPOSITIONENTRY._options = None
  _FILEEXTRACTEDDATA_NESTEDPOSITIONENTRY._serialized_options = b'8\001'
  _FILEEXTRACTEDDATA_NESTEDLISTPOSITIONENTRY._options = None
  _FILEEXTRACTEDDATA_NESTEDLISTPOSITIONENTRY._serialized_options = b'8\001'
  _FILEEXTRACTEDDATA.fields_by_name['nested_position']._options = None
  _FILEEXTRACTEDDATA.fields_by_name['nested_position']._serialized_options = b'\030\001'
  _LINKEXTRACTEDDATA_METADATAENTRY._options = None
  _LINKEXTRACTEDDATA_METADATAENTRY._serialized_options = b'8\001'
  _USERVECTORSWRAPPER_VECTORSTODELETEENTRY._options = None
  _USERVECTORSWRAPPER_VECTORSTODELETEENTRY._serialized_options = b'8\001'
  _FIELDMETADATA_NERENTRY._options = None
  _FIELDMETADATA_NERENTRY._serialized_options = b'8\001'
  _FIELDMETADATA_POSITIONSENTRY._options = None
  _FIELDMETADATA_POSITIONSENTRY._serialized_options = b'8\001'
  _FIELDCOMPUTEDMETADATA_SPLITMETADATAENTRY._options = None
  _FIELDCOMPUTEDMETADATA_SPLITMETADATAENTRY._serialized_options = b'8\001'
  _METADATA_METADATAENTRY._options = None
  _METADATA_METADATAENTRY._serialized_options = b'8\001'
  _LAYOUTCONTENT_BLOCKSENTRY._options = None
  _LAYOUTCONTENT_BLOCKSENTRY._serialized_options = b'8\001'
  _FIELDLINK_HEADERSENTRY._options = None
  _FIELDLINK_HEADERSENTRY._serialized_options = b'8\001'
  _FIELDLINK_COOKIESENTRY._options = None
  _FIELDLINK_COOKIESENTRY._serialized_options = b'8\001'
  _FIELDLINK_LOCALSTORAGEENTRY._options = None
  _FIELDLINK_LOCALSTORAGEENTRY._serialized_options = b'8\001'
  _FIELDFILE_HEADERSENTRY._options = None
  _FIELDFILE_HEADERSENTRY._serialized_options = b'8\001'
  _FIELDFILE_COOKIESENTRY._options = None
  _FIELDFILE_COOKIESENTRY._serialized_options = b'8\001'
  _FIELDLARGEMETADATA_TOKENSENTRY._options = None
  _FIELDLARGEMETADATA_TOKENSENTRY._serialized_options = b'8\001'
  _LARGECOMPUTEDMETADATA_SPLITMETADATAENTRY._options = None
  _LARGECOMPUTEDMETADATA_SPLITMETADATAENTRY._serialized_options = b'8\001'
  _ROWSPREVIEW_SHEETSENTRY._options = None
  _ROWSPREVIEW_SHEETSENTRY._serialized_options = b'8\001'
  _FIELDTYPE._serialized_start=9435
  _FIELDTYPE._serialized_end=9549
  _CLOUDFILE._serialized_start=139
  _CLOUDFILE._serialized_end=507
  _CLOUDFILE_SOURCE._serialized_start=409
  _CLOUDFILE_SOURCE._serialized_end=507
  _BASIC._serialized_start=510
  _BASIC._serialized_end=1054
  _BASIC_QUEUETYPE._serialized_start=1018
  _BASIC_QUEUETYPE._serialized_end=1054
  _ORIGIN._serialized_start=1057
  _ORIGIN._serialized_end=1442
  _ORIGIN_METADATAENTRY._serialized_start=1354
  _ORIGIN_METADATAENTRY._serialized_end=1401
  _ORIGIN_SOURCE._serialized_start=1403
  _ORIGIN_SOURCE._serialized_end=1442
  _EXTRA._serialized_start=1444
  _EXTRA._serialized_end=1494
  _RELATIONS._serialized_start=1496
  _RELATIONS._serialized_end=1543
  _MESSAGECONTENT._serialized_start=1546
  _MESSAGECONTENT._serialized_end=1723
  _MESSAGECONTENT_FORMAT._serialized_start=1671
  _MESSAGECONTENT_FORMAT._serialized_end=1723
  _MESSAGE._serialized_start=1726
  _MESSAGE._serialized_end=1866
  _CONVERSATION._serialized_start=1868
  _CONVERSATION._serialized_end=1920
  _FIELDCONVERSATION._serialized_start=1922
  _FIELDCONVERSATION._serialized_end=1985
  _NESTEDPOSITION._serialized_start=1987
  _NESTEDPOSITION._serialized_end=2045
  _NESTEDLISTPOSITION._serialized_start=2047
  _NESTEDLISTPOSITION._serialized_end=2113
  _FILEEXTRACTEDDATA._serialized_start=2116
  _FILEEXTRACTEDDATA._serialized_end=3197
  _FILEEXTRACTEDDATA_METADATAENTRY._serialized_start=1354
  _FILEEXTRACTEDDATA_METADATAENTRY._serialized_end=1401
  _FILEEXTRACTEDDATA_NESTEDENTRY._serialized_start=2823
  _FILEEXTRACTEDDATA_NESTEDENTRY._serialized_end=2868
  _FILEEXTRACTEDDATA_FILEGENERATEDENTRY._serialized_start=2870
  _FILEEXTRACTEDDATA_FILEGENERATEDENTRY._serialized_end=2944
  _FILEEXTRACTEDDATA_FILEROWSPREVIEWSENTRY._serialized_start=2946
  _FILEEXTRACTEDDATA_FILEROWSPREVIEWSENTRY._serialized_end=3025
  _FILEEXTRACTEDDATA_NESTEDPOSITIONENTRY._serialized_start=3027
  _FILEEXTRACTEDDATA_NESTEDPOSITIONENTRY._serialized_end=3107
  _FILEEXTRACTEDDATA_NESTEDLISTPOSITIONENTRY._serialized_start=3109
  _FILEEXTRACTEDDATA_NESTEDLISTPOSITIONENTRY._serialized_end=3197
  _LINKEXTRACTEDDATA._serialized_start=3200
  _LINKEXTRACTEDDATA._serialized_end=3602
  _LINKEXTRACTEDDATA_METADATAENTRY._serialized_start=1354
  _LINKEXTRACTEDDATA_METADATAENTRY._serialized_end=1401
  _EXTRACTEDTEXTWRAPPER._serialized_start=3605
  _EXTRACTEDTEXTWRAPPER._serialized_end=3754
  _EXTRACTEDVECTORSWRAPPER._serialized_start=3757
  _EXTRACTEDVECTORSWRAPPER._serialized_end=3911
  _USERVECTORSWRAPPER._serialized_start=3914
  _USERVECTORSWRAPPER._serialized_end=4167
  _USERVECTORSWRAPPER_VECTORSTODELETEENTRY._serialized_start=4089
  _USERVECTORSWRAPPER_VECTORSTODELETEENTRY._serialized_end=4167
  _SENTENCE._serialized_start=4169
  _SENTENCE._serialized_end=4220
  _PARAGRAPH._serialized_start=4223
  _PARAGRAPH._serialized_end=4570
  _PARAGRAPH_TYPEPARAGRAPH._serialized_start=4477
  _PARAGRAPH_TYPEPARAGRAPH._serialized_end=4570
  _POSITION._serialized_start=4572
  _POSITION._serialized_end=4610
  _POSITIONS._serialized_start=4612
  _POSITIONS._serialized_end=4678
  _FIELDMETADATA._serialized_start=4681
  _FIELDMETADATA._serialized_end=5350
  _FIELDMETADATA_NERENTRY._serialized_start=5236
  _FIELDMETADATA_NERENTRY._serialized_end=5278
  _FIELDMETADATA_POSITIONSENTRY._serialized_start=5280
  _FIELDMETADATA_POSITIONSENTRY._serialized_end=5350
  _FIELDCOMPUTEDMETADATA._serialized_start=5353
  _FIELDCOMPUTEDMETADATA._serialized_end=5601
  _FIELDCOMPUTEDMETADATA_SPLITMETADATAENTRY._serialized_start=5523
  _FIELDCOMPUTEDMETADATA_SPLITMETADATAENTRY._serialized_end=5601
  _FIELDCOMPUTEDMETADATAWRAPPER._serialized_start=5603
  _FIELDCOMPUTEDMETADATAWRAPPER._serialized_end=5720
  _METADATA._serialized_start=5723
  _METADATA._serialized_end=6007
  _METADATA_METADATAENTRY._serialized_start=1354
  _METADATA_METADATAENTRY._serialized_end=1401
  _METADATA_STATUS._serialized_start=5934
  _METADATA_STATUS._serialized_end=6007
  _FIELDTEXT._serialized_start=6010
  _FIELDTEXT._serialized_end=6147
  _FIELDTEXT_FORMAT._serialized_start=6095
  _FIELDTEXT_FORMAT._serialized_end=6147
  _BLOCK._serialized_start=6150
  _BLOCK._serialized_end=6434
  _BLOCK_TYPEBLOCK._serialized_start=6319
  _BLOCK_TYPEBLOCK._serialized_end=6434
  _LAYOUTCONTENT._serialized_start=6437
  _LAYOUTCONTENT._serialized_end=6595
  _LAYOUTCONTENT_BLOCKSENTRY._serialized_start=6532
  _LAYOUTCONTENT_BLOCKSENTRY._serialized_end=6595
  _FIELDLAYOUT._serialized_start=6597
  _FIELDLAYOUT._serialized_end=6721
  _FIELDLAYOUT_FORMAT._serialized_start=6699
  _FIELDLAYOUT_FORMAT._serialized_end=6721
  _CLASSIFICATION._serialized_start=6723
  _CLASSIFICATION._serialized_end=6814
  _USERMETADATA._serialized_start=6816
  _USERMETADATA._serialized_end=6918
  _FIELDCLASSIFICATIONS._serialized_start=6920
  _FIELDCLASSIFICATIONS._serialized_end=7029
  _COMPUTEDMETADATA._serialized_start=7031
  _COMPUTEDMETADATA._serialized_end=7113
  _TOKENSPLIT._serialized_start=7115
  _TOKENSPLIT._serialized_end=7227
  _PARAGRAPHANNOTATION._serialized_start=7229
  _PARAGRAPHANNOTATION._serialized_end=7315
  _USERFIELDMETADATA._serialized_start=7318
  _USERFIELDMETADATA._serialized_end=7462
  _FIELDLINK._serialized_start=7465
  _FIELDLINK._serialized_end=7865
  _FIELDLINK_HEADERSENTRY._serialized_start=7718
  _FIELDLINK_HEADERSENTRY._serialized_end=7764
  _FIELDLINK_COOKIESENTRY._serialized_start=7766
  _FIELDLINK_COOKIESENTRY._serialized_end=7812
  _FIELDLINK_LOCALSTORAGEENTRY._serialized_start=7814
  _FIELDLINK_LOCALSTORAGEENTRY._serialized_end=7865
  _KEYWORD._serialized_start=7867
  _KEYWORD._serialized_end=7891
  _FIELDKEYWORDSET._serialized_start=7893
  _FIELDKEYWORDSET._serialized_end=7948
  _FIELDDATETIME._serialized_start=7950
  _FIELDDATETIME._serialized_end=8008
  _FIELDFILE._serialized_start=8011
  _FIELDFILE._serialized_end=8350
  _FIELDFILE_HEADERSENTRY._serialized_start=7718
  _FIELDFILE_HEADERSENTRY._serialized_end=7764
  _FIELDFILE_COOKIESENTRY._serialized_start=7766
  _FIELDFILE_COOKIESENTRY._serialized_end=7812
  _ENTITY._serialized_start=8352
  _ENTITY._serialized_end=8403
  _FIELDLARGEMETADATA._serialized_start=8406
  _FIELDLARGEMETADATA._serialized_end=8569
  _FIELDLARGEMETADATA_TOKENSENTRY._serialized_start=8524
  _FIELDLARGEMETADATA_TOKENSENTRY._serialized_end=8569
  _LARGECOMPUTEDMETADATA._serialized_start=8572
  _LARGECOMPUTEDMETADATA._serialized_end=8830
  _LARGECOMPUTEDMETADATA_SPLITMETADATAENTRY._serialized_start=8747
  _LARGECOMPUTEDMETADATA_SPLITMETADATAENTRY._serialized_end=8830
  _LARGECOMPUTEDMETADATAWRAPPER._serialized_start=8833
  _LARGECOMPUTEDMETADATAWRAPPER._serialized_end=9002
  _PAGEPOSITIONS._serialized_start=9004
  _PAGEPOSITIONS._serialized_end=9047
  _FILEPAGES._serialized_start=9049
  _FILEPAGES._serialized_end=9142
  _ROWSPREVIEW._serialized_start=9145
  _ROWSPREVIEW._serialized_end=9365
  _ROWSPREVIEW_SHEET._serialized_start=9212
  _ROWSPREVIEW_SHEET._serialized_end=9288
  _ROWSPREVIEW_SHEET_ROW._serialized_start=9269
  _ROWSPREVIEW_SHEET_ROW._serialized_end=9288
  _ROWSPREVIEW_SHEETSENTRY._serialized_start=9290
  _ROWSPREVIEW_SHEETSENTRY._serialized_end=9365
  _FIELDID._serialized_start=9367
  _FIELDID._serialized_end=9433
# @@protoc_insertion_point(module_scope)
