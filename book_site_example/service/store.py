
from book_site_example.extension.database import DatabaseConnection
import book_site_example.proto.protobuf.book_pb2 as book_pb2
import book_site_example.proto.protobuf.book_pb2_grpc as book_pb2_grpc


class MyStoreService(book_pb2_grpc.StoreServicer):
    pass
