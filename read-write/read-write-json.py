import google.protobuf.json_format as json_format


##########################################
# You need to import simple_pb2 here
# To generate python code from proto files use the following command:
# protoc -Iproto --python_out=proto  .\proto\*.proto
#
# Next, import this file as simple_pb2


def simple():
    return simple_pb2.Simple(
        id=42,
        name="Stefan",
        is_simple=True,
        count=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    )


def to_json(message):
    return json_format.MessageToJson(message)


def from_json(json_str: str, obj_type):
    return json_format.Parse(json_str, obj_type())


json_example = to_json(simple())
print(json_example)
proto_obj_example = from_json(json_example, simple_pb2.Simple)
