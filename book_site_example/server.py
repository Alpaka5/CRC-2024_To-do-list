
import grpc

from book_site_example.service.store import MyStoreService
from concurrent import futures
import book_site_example.proto.protobuf.book_pb2_grpc as book_pb2_grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_pb2_grpc.add_StoreServicer_to_server(
        MyStoreService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
