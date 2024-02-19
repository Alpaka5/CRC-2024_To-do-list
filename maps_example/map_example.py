import maps_example.proto.example_pb2 as example_pb2


def example_map():
    proto_map = example_pb2.Person()
    proto_map.person["Andrzej"].nick_name = "Andrzej123"
    proto_map.person["Tomek"].nick_name = "Tomek123"
    proto_map.person["Amelia"].nick_name = "Terminator2000"
    proto_map.person["John"].nick_name = "Boy-John"
    return proto_map

print(example_map())