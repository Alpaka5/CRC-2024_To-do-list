import candy_examples.proto.example_pb2 as example_pb2


def complex_candy():
    candy_box = example_pb2.CandyBox()
    candy_box.one_candy.id = 42
    candy_box.one_candy.name = "KinderBox"
    candy_box.many_candies.add(id=42, name="Kinder Egg")
    candy_box.many_candies.add(id=43, name="Bueno")
    candy_box.many_candies.add(id=44, name="Country")
    return candy_box


print(complex_candy())


