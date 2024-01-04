from todo_app.source.proto import todo_pb2, todo_pb2_grpc
from unittest import mock
class TodoService(todo_pb2_grpc.ToDoServiceServicer):
    def __init__(self):
        self.database_connection = mock.MagicMock()
    def CreateTodo(self, request: todo_pb2.TodoElement, context) -> todo_pb2.Succeed:
        self.database_connection.insert_todo_element(request.Title, request.Title, request.Finished)
        return todo_pb2.Succeed(value=True)
