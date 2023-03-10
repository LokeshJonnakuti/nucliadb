# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nucliadb_protos/knowledgebox.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"nucliadb_protos/knowledgebox.proto\x12\x0cknowledgebox\",\n\x0eKnowledgeBoxID\x12\x0c\n\x04slug\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\"\x96\x01\n\x0cKnowledgeBox\x12\x0c\n\x04slug\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x38\n\x06status\x18\x03 \x01(\x0e\x32(.knowledgebox.KnowledgeBoxResponseStatus\x12\x30\n\x06\x63onfig\x18\x04 \x01(\x0b\x32 .knowledgebox.KnowledgeBoxConfig\"\x92\x01\n\x12KnowledgeBoxConfig\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x17\n\x0f\x65nabled_filters\x18\x03 \x03(\t\x12\x18\n\x10\x65nabled_insights\x18\x04 \x03(\t\x12\x0c\n\x04slug\x18\x05 \x01(\t\x12\x17\n\x0f\x64isable_vectors\x18\x06 \x01(\x08\"d\n\x0fKnowledgeBoxNew\x12\x0c\n\x04slug\x18\x01 \x01(\t\x12\x30\n\x06\x63onfig\x18\x02 \x01(\x0b\x32 .knowledgebox.KnowledgeBoxConfig\x12\x11\n\tforceuuid\x18\x03 \x01(\t\"a\n\x17NewKnowledgeBoxResponse\x12\x38\n\x06status\x18\x01 \x01(\x0e\x32(.knowledgebox.KnowledgeBoxResponseStatus\x12\x0c\n\x04uuid\x18\x02 \x01(\t\"$\n\x12KnowledgeBoxPrefix\x12\x0e\n\x06prefix\x18\x01 \x01(\t\"b\n\x12KnowledgeBoxUpdate\x12\x0c\n\x04slug\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x30\n\x06\x63onfig\x18\x03 \x01(\x0b\x32 .knowledgebox.KnowledgeBoxConfig\"d\n\x1aUpdateKnowledgeBoxResponse\x12\x38\n\x06status\x18\x01 \x01(\x0e\x32(.knowledgebox.KnowledgeBoxResponseStatus\x12\x0c\n\x04uuid\x18\x02 \x01(\t\"\x18\n\x16GCKnowledgeBoxResponse\"V\n\x1a\x44\x65leteKnowledgeBoxResponse\x12\x38\n\x06status\x18\x01 \x01(\x0e\x32(.knowledgebox.KnowledgeBoxResponseStatus\"\x1d\n\x1b\x43leanedKnowledgeBoxResponse\"B\n\x05Label\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07related\x18\x03 \x01(\t\x12\x0c\n\x04text\x18\x04 \x01(\t\x12\x0b\n\x03uri\x18\x05 \x01(\t\"\xd0\x01\n\x08LabelSet\x12\r\n\x05title\x18\x01 \x01(\t\x12\r\n\x05\x63olor\x18\x02 \x01(\t\x12#\n\x06labels\x18\x03 \x03(\x0b\x32\x13.knowledgebox.Label\x12\x10\n\x08multiple\x18\x04 \x01(\x08\x12\x31\n\x04kind\x18\x05 \x03(\x0e\x32#.knowledgebox.LabelSet.LabelSetKind\"<\n\x0cLabelSetKind\x12\r\n\tRESOURCES\x10\x00\x12\x0e\n\nPARAGRAPHS\x10\x01\x12\r\n\tSENTENCES\x10\x02\"\x87\x01\n\x06Labels\x12\x34\n\x08labelset\x18\x01 \x03(\x0b\x32\".knowledgebox.Labels.LabelsetEntry\x1aG\n\rLabelsetEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.knowledgebox.LabelSet:\x02\x38\x01\";\n\x06\x45ntity\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0e\n\x06merged\x18\x03 \x01(\x08\x12\x12\n\nrepresents\x18\x04 \x03(\t\"\xc1\x01\n\rEntitiesGroup\x12;\n\x08\x65ntities\x18\x01 \x03(\x0b\x32).knowledgebox.EntitiesGroup.EntitiesEntry\x12\r\n\x05title\x18\x02 \x01(\t\x12\r\n\x05\x63olor\x18\x03 \x01(\t\x12\x0e\n\x06\x63ustom\x18\x04 \x01(\x08\x1a\x45\n\rEntitiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.knowledgebox.Entity:\x02\x38\x01\"\xfc\x03\n\x06Widget\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12-\n\x04mode\x18\x03 \x01(\x0e\x32\x1f.knowledgebox.Widget.WidgetMode\x12\x35\n\x08\x66\x65\x61tures\x18\x04 \x01(\x0b\x32#.knowledgebox.Widget.WidgetFeatures\x12\x0f\n\x07\x66ilters\x18\x05 \x03(\t\x12\x13\n\x0btopEntities\x18\x06 \x03(\t\x12.\n\x05style\x18\x07 \x03(\x0b\x32\x1f.knowledgebox.Widget.StyleEntry\x1a\xb7\x01\n\x0eWidgetFeatures\x12\x12\n\nuseFilters\x18\x01 \x01(\x08\x12\x17\n\x0fsuggestEntities\x18\x02 \x01(\x08\x12\x18\n\x10suggestSentences\x18\x03 \x01(\x08\x12\x19\n\x11suggestParagraphs\x18\x04 \x01(\x08\x12\x15\n\rsuggestLabels\x18\x05 \x01(\x08\x12\x12\n\neditLabels\x18\x06 \x01(\x08\x12\x18\n\x10\x65ntityAnnotation\x18\x07 \x01(\x08\x1a,\n\nStyleEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"-\n\nWidgetMode\x12\n\n\x06\x42UTTON\x10\x00\x12\t\n\x05INPUT\x10\x01\x12\x08\n\x04\x46ORM\x10\x02\"\x1e\n\tVectorSet\x12\x11\n\tdimension\x18\x01 \x01(\x05\"\x96\x01\n\nVectorSets\x12<\n\nvectorsets\x18\x01 \x03(\x0b\x32(.knowledgebox.VectorSets.VectorsetsEntry\x1aJ\n\x0fVectorsetsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.knowledgebox.VectorSet:\x02\x38\x01\" \n\x0cTermSynonyms\x12\x10\n\x08synonyms\x18\x01 \x03(\t\"\x86\x01\n\x08Synonyms\x12\x30\n\x05terms\x18\x01 \x03(\x0b\x32!.knowledgebox.Synonyms.TermsEntry\x1aH\n\nTermsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.knowledgebox.TermSynonyms:\x02\x38\x01*K\n\x1aKnowledgeBoxResponseStatus\x12\x06\n\x02OK\x10\x00\x12\x0c\n\x08\x43ONFLICT\x10\x01\x12\x0c\n\x08NOTFOUND\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nucliadb_protos.knowledgebox_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LABELS_LABELSETENTRY._options = None
  _LABELS_LABELSETENTRY._serialized_options = b'8\001'
  _ENTITIESGROUP_ENTITIESENTRY._options = None
  _ENTITIESGROUP_ENTITIESENTRY._serialized_options = b'8\001'
  _WIDGET_STYLEENTRY._options = None
  _WIDGET_STYLEENTRY._serialized_options = b'8\001'
  _VECTORSETS_VECTORSETSENTRY._options = None
  _VECTORSETS_VECTORSETSENTRY._serialized_options = b'8\001'
  _SYNONYMS_TERMSENTRY._options = None
  _SYNONYMS_TERMSENTRY._serialized_options = b'8\001'
  _KNOWLEDGEBOXRESPONSESTATUS._serialized_start=2527
  _KNOWLEDGEBOXRESPONSESTATUS._serialized_end=2602
  _KNOWLEDGEBOXID._serialized_start=52
  _KNOWLEDGEBOXID._serialized_end=96
  _KNOWLEDGEBOX._serialized_start=99
  _KNOWLEDGEBOX._serialized_end=249
  _KNOWLEDGEBOXCONFIG._serialized_start=252
  _KNOWLEDGEBOXCONFIG._serialized_end=398
  _KNOWLEDGEBOXNEW._serialized_start=400
  _KNOWLEDGEBOXNEW._serialized_end=500
  _NEWKNOWLEDGEBOXRESPONSE._serialized_start=502
  _NEWKNOWLEDGEBOXRESPONSE._serialized_end=599
  _KNOWLEDGEBOXPREFIX._serialized_start=601
  _KNOWLEDGEBOXPREFIX._serialized_end=637
  _KNOWLEDGEBOXUPDATE._serialized_start=639
  _KNOWLEDGEBOXUPDATE._serialized_end=737
  _UPDATEKNOWLEDGEBOXRESPONSE._serialized_start=739
  _UPDATEKNOWLEDGEBOXRESPONSE._serialized_end=839
  _GCKNOWLEDGEBOXRESPONSE._serialized_start=841
  _GCKNOWLEDGEBOXRESPONSE._serialized_end=865
  _DELETEKNOWLEDGEBOXRESPONSE._serialized_start=867
  _DELETEKNOWLEDGEBOXRESPONSE._serialized_end=953
  _CLEANEDKNOWLEDGEBOXRESPONSE._serialized_start=955
  _CLEANEDKNOWLEDGEBOXRESPONSE._serialized_end=984
  _LABEL._serialized_start=986
  _LABEL._serialized_end=1052
  _LABELSET._serialized_start=1055
  _LABELSET._serialized_end=1263
  _LABELSET_LABELSETKIND._serialized_start=1203
  _LABELSET_LABELSETKIND._serialized_end=1263
  _LABELS._serialized_start=1266
  _LABELS._serialized_end=1401
  _LABELS_LABELSETENTRY._serialized_start=1330
  _LABELS_LABELSETENTRY._serialized_end=1401
  _ENTITY._serialized_start=1403
  _ENTITY._serialized_end=1462
  _ENTITIESGROUP._serialized_start=1465
  _ENTITIESGROUP._serialized_end=1658
  _ENTITIESGROUP_ENTITIESENTRY._serialized_start=1589
  _ENTITIESGROUP_ENTITIESENTRY._serialized_end=1658
  _WIDGET._serialized_start=1661
  _WIDGET._serialized_end=2169
  _WIDGET_WIDGETFEATURES._serialized_start=1893
  _WIDGET_WIDGETFEATURES._serialized_end=2076
  _WIDGET_STYLEENTRY._serialized_start=2078
  _WIDGET_STYLEENTRY._serialized_end=2122
  _WIDGET_WIDGETMODE._serialized_start=2124
  _WIDGET_WIDGETMODE._serialized_end=2169
  _VECTORSET._serialized_start=2171
  _VECTORSET._serialized_end=2201
  _VECTORSETS._serialized_start=2204
  _VECTORSETS._serialized_end=2354
  _VECTORSETS_VECTORSETSENTRY._serialized_start=2280
  _VECTORSETS_VECTORSETSENTRY._serialized_end=2354
  _TERMSYNONYMS._serialized_start=2356
  _TERMSYNONYMS._serialized_end=2388
  _SYNONYMS._serialized_start=2391
  _SYNONYMS._serialized_end=2525
  _SYNONYMS_TERMSENTRY._serialized_start=2453
  _SYNONYMS_TERMSENTRY._serialized_end=2525
# @@protoc_insertion_point(module_scope)
