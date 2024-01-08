from source.proto import todo_pb2, todo_pb2_grpc
from source.extensions.database import DatabaseConnection
import uuid


class TodoService(todo_pb2_grpc.ToDoServiceServicer):
    def __init__(self):
        self.database_connection = DatabaseConnection()

    def CreateTodo(self, request: todo_pb2.TodoElement, context) -> todo_pb2.TodoId:
        # We overwrite ID of request to avoid doubling IDs
        request.Id = uuid.uuid4().hex
        try:
            self.database_connection.insert_todo_element(request)
        except:
            return todo_pb2.TodoId(Id=None)
        return todo_pb2.TodoId(Id=request.Id)

    def GetTodo(self, request: todo_pb2.TodoId, context) -> todo_pb2.TodoElement:
        return self.database_connection.get_todo_element(request.Id)

    def GetAllTodos(self, request, context) -> todo_pb2.TodoElement:
        for element in self.database_connection.get_all_todos():
            yield element

    def FinishTodo(self, request: todo_pb2.TodoId, context) -> todo_pb2.Succeed:
        try:
            self.database_connection.finish_todo_element(request.Id)
        except:
            return todo_pb2.Succeed(value=False)
        return todo_pb2.Succeed(value=True)

    def EditTodo(self, request: todo_pb2.TodoElement, context) -> todo_pb2.Succeed:
        try:
            self.database_connection.edit_todo_element(request)
        except:
            return todo_pb2.Succeed(value=False)
        return todo_pb2.Succeed(value=True)

    def RemoveTodo(self, request: todo_pb2.TodoId, context) -> todo_pb2.Succeed:
        try:
            self.database_connection.remove_todo_element(request.Id)
        except:
            return todo_pb2.Succeed(value=False)
        return todo_pb2.Succeed(value=True)