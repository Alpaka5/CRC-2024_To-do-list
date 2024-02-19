import grpc

import protobuf.book_pb2 as book_pb2
import protobuf.book_pb2_grpc as book_pb2_grpc


class Client:

    def __init__(self):
        self.host = "localhost:50051"

    def add_book(self, book_element: book_pb2.Book):
        with grpc.insecure_channel(self.host) as channel:
            client = book_pb2_grpc.StoreStub(channel)
            print(f"Adding book: {book_element}")
            response: book_pb2.Book = client.AddBook(book_element)
            print(f"Todo element created: {response.title}")

    def get_book(self, book_title: book_pb2.BookTitle):
        with grpc.insecure_channel(self.host) as channel:
            client = book_pb2_grpc.StoreStub(channel)
            print(f"Get book with {book_title}", end="")
            response: book_pb2.Book = client.GetBook(book_title)
            print("Book")
            print(f"\tTitle: {response.title}")
            print(f"\tId: {response.id}")
            print(f"\tCategory: {response.category}", end="\n\n")

    def delete_book(self, book_title: book_pb2.BookTitle):
        with grpc.insecure_channel(self.host) as channel:
            client = book_pb2_grpc.StoreStub(channel)
            response: book_pb2.Status = client.RemoveBook(book_title)
            print(f"Result: {response.status}")
            if response.status:
                print(f"Delete book with {book_title} ")
            else:
                print(f"Couldn't delete book with {book_title}")

    def get_all_books(self):
        with grpc.insecure_channel(self.host) as channel:
            client = book_pb2_grpc.StoreStub(channel)
            print(f"Getting all book...")
            for book in client.GetAllBooks(book_pb2.Empty()):
                print(f"Book:")
                print(f"\tTitle: {book.title}")
                print(f"\tId: {book.id}")
                print(f"\tCategory: {book.category}")
            print("\n\n")

