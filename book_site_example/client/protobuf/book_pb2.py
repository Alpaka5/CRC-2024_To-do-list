# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/book.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13protobuf/book.proto\"B\n\x04\x42ook\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x1f\n\x08\x63\x61tegory\x18\x03 \x01(\x0e\x32\r.BookCategory\"\x07\n\x05\x45mpty\"\x18\n\x06Status\x12\x0e\n\x06status\x18\x01 \x01(\x08\"\x1a\n\tBookTitle\x12\r\n\x05title\x18\x01 \x01(\t*?\n\x0c\x42ookCategory\x12\x0b\n\x07MYSTERY\x10\x00\x12\x13\n\x0fSCIENCE_FICTION\x10\x01\x12\r\n\tSELF_HELP\x10\x02\x32\x89\x01\n\x05Store\x12 \n\x0bGetAllBooks\x12\x06.Empty\x1a\x05.Book\"\x00\x30\x01\x12\x1e\n\x07GetBook\x12\n.BookTitle\x1a\x05.Book\"\x00\x12\x19\n\x07\x41\x64\x64\x42ook\x12\x05.Book\x1a\x05.Book\"\x00\x12#\n\nRemoveBook\x12\n.BookTitle\x1a\x07.Status\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protobuf.book_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_BOOKCATEGORY']._serialized_start=154
  _globals['_BOOKCATEGORY']._serialized_end=217
  _globals['_BOOK']._serialized_start=23
  _globals['_BOOK']._serialized_end=89
  _globals['_EMPTY']._serialized_start=91
  _globals['_EMPTY']._serialized_end=98
  _globals['_STATUS']._serialized_start=100
  _globals['_STATUS']._serialized_end=124
  _globals['_BOOKTITLE']._serialized_start=126
  _globals['_BOOKTITLE']._serialized_end=152
  _globals['_STORE']._serialized_start=220
  _globals['_STORE']._serialized_end=357
# @@protoc_insertion_point(module_scope)
