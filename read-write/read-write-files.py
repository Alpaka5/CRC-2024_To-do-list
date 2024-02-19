
##########################################
# You need to import simple_pb2 here
# To generate python code from proto files use the following command:
# protoc -Iproto --python_out=proto  .\proto\*.proto
#
# Next, import this file as simple_pb2
# call the function and see what happens....


def simple():
    return simple_pb2.Simple(
        id=42,
        name="Stefan",
        is_simple=True,
        count=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    )


def file(message):
    path = "test_file.bin"

    print("Write to file")
    with open(path, "wb") as f:
        bytes_as_string = message.SerializeToString()
        f.write(bytes_as_string)

    print("Read from file")
    with open(path, "rb") as fil:
        message2 = type(message).FromString(fil.read())
    print(message2)

