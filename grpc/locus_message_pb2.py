# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: locus_message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13locus_message.proto\x12\rlocus_package\"\x13\n\x05Locus\x12\n\n\x02id\x18\x01 \x01(\t\"!\n\x0f\x46ilterExecution\x12\x0e\n\x06status\x18\x01 \x01(\x08\x32T\n\rLocusMessager\x12\x43\n\tSendLocus\x12\x14.locus_package.Locus\x1a\x1e.locus_package.FilterExecution\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'locus_message_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_LOCUS']._serialized_start=38
  _globals['_LOCUS']._serialized_end=57
  _globals['_FILTEREXECUTION']._serialized_start=59
  _globals['_FILTEREXECUTION']._serialized_end=92
  _globals['_LOCUSMESSAGER']._serialized_start=94
  _globals['_LOCUSMESSAGER']._serialized_end=178
# @@protoc_insertion_point(module_scope)
