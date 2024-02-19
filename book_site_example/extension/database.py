import csv
import book_site_example.proto.protobuf.book_pb2 as book_pb2


class DatabaseConnection:

    def __init__(self):
        self.db_file_path = "./todo_list.csv"
        self.delimiter = "|"

    def insert_element(self, recommend_element: book_pb2.Book):
        with open(self.db_file_path, "a", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=self.delimiter)
            writer.writerow(
                [
                    recommend_element.id,
                    recommend_element.title,
                    recommend_element.category,
                ]
            )

    def get_book(self, title: str) -> book_pb2.BookTitle:
        with open(self.db_file_path, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=self.delimiter)
            for row in reader:
                if row[1] == title:
                    book =book_pb2.Book(
                        id=int(row[0]),
                        title=row[1],
                        category=int(row[2]),
                        )
                    return book
            # If we couldn't find todoElement with given id, we return empty element
            return book_pb2.Book(
                id=None,
                title=None,
                category=None
            )

    def get_all_books(self) -> list[book_pb2.Book]:
        with open(self.db_file_path, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=self.delimiter)
            element_list = []
            for row in reader:
                element_list.append(book_pb2.Book(
                        id=int(row[0]),
                        title=row[1],
                        category=int(row[2]),
                    )
                )
        return element_list

    def remove_book(self, title: str) -> bool:
        result_status = False
        with open(self.db_file_path, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=self.delimiter)
            element_list = list(reader)
            for index, element in enumerate(element_list):
                if element[1] == title:
                    result_status = True
                    element_list.pop(index)
                    break

        with open(self.db_file_path, "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=self.delimiter)
            writer.writerows(element_list)
        return result_status
