from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TodoElement(_message.Message):
    __slots__ = ("Id", "Title", "Description", "Finished")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    Id: str
    Title: str
    Description: str
    Finished: bool
    def __init__(self, Id: _Optional[str] = ..., Title: _Optional[str] = ..., Description: _Optional[str] = ..., Finished: bool = ...) -> None: ...

class TodoId(_message.Message):
    __slots__ = ("Id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    Id: str
    def __init__(self, Id: _Optional[str] = ...) -> None: ...

class Succeed(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...
