
from book_site_example.extension.database import DatabaseConnection
import book_site_example.proto.protobuf.book_pb2 as book_pb2
import book_site_example.proto.protobuf.book_pb2_grpc as book_pb2_grpc


class MyStoreService(book_pb2_grpc.StoreServicer):

    def __init__(self):
        self.database_connection = DatabaseConnection()

    def GetAllBooks(self, request, context):
        print("Getting all books")
        for book in self.database_connection.get_all_books():
            yield book

    def GetBook(self, request, context):
        book = self.database_connection.get_book(request.title)
        print("Getting book")
        print(book)
        return book

    def RemoveBook(self, request, context):
        print("Removing book")
        try:
            result_status: bool = self.database_connection.remove_book(request.title)
        except Exception as err:
            print(f"Error removing book: {err}")
            result_status = False
        if result_status:
            print(f"Removed book: {request.title}")
        else:
            print("Couldn't remove book'")
        status = book_pb2.Status(
            status=result_status
        )
        return status

    def AddBook(self, request, context):
        self.database_connection.insert_element(request)
        print(f"Book {request.title} was added to database")
        return book_pb2.Book(
            id=request.id,
            title=request.title,
            category=request.category
        )
