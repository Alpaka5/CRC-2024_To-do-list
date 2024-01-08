from concurrent import futures

import grpc
from source.proto import todo_pb2_grpc
from source.services import todo_service

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_ToDoServiceServicer_to_server(todo_service.TodoService(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == "__main__":
    serve()