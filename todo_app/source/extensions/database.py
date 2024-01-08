import csv
from todo_app.source.proto import todo_pb2


class DatabaseConnection:
    def __init__(self):
        self.db_file_path = "./todo_list.csv"
        self.delimiter = "|"

    def insert_todo_element(self, todo_element: todo_pb2.TodoElement):
        with open(self.db_file_path, "a",newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=self.delimiter)
            writer.writerow(
                [
                    todo_element.Id,
                    todo_element.Title,
                    todo_element.Description,
                    todo_element.Finished,
                ]
            )

    def get_todo_element(self, todo_id: str) -> todo_pb2.TodoElement:
        with open(self.db_file_path, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=self.delimiter)
            for row in reader:
                if row[0] == todo_id:
                    return todo_pb2.TodoElement(
                        Id=row[0],
                        Title=row[1],
                        Description=row[2],
                        Finished=(row[3]=="True"),
                    )
            # If we couldn't find todoElement with given id, we return empty element
            return todo_pb2.TodoElement(
                Id=None,
                Title=None,
                Description=None,
                Finished=False,
            )

    def get_all_todos(self) -> list[todo_pb2.TodoElement]:
        with open(self.db_file_path, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=self.delimiter)
            element_list = []
            for row in reader:
                element_list.append(
                    todo_pb2.TodoElement(
                        Id=row[0],
                        Title=row[1],
                        Description=row[2],
                        Finished=(row[3]=="True"),
                    )
                )

        return element_list

    def finish_todo_element(self, todo_id: str):
        with open(self.db_file_path, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=self.delimiter)
            element_list = list(reader)
            for element in element_list:
                if element[0] == todo_id:
                    element[3] = True
                    break

        with open(self.db_file_path, "w",newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=self.delimiter)
            writer.writerows(element_list)

    def edit_todo_element(self, edited_todo_element: todo_pb2.TodoElement):
        with open(self.db_file_path, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=self.delimiter)
            element_list = list(reader)
            for element in element_list:
                if element[0] == edited_todo_element.Id:
                    element[1] = edited_todo_element.Title
                    element[2] = edited_todo_element.Description
                    element[3] = edited_todo_element.Finished
                    break
        with open(self.db_file_path, "w",newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=self.delimiter)
            writer.writerows(element_list)

    def remove_todo_element(self,todo_id: str):
        with open(self.db_file_path, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=self.delimiter)
            element_list = list(reader)
            for index, element  in enumerate(element_list):
                if element[0] == todo_id:
                    element_list.pop(index)
                    break

        with open(self.db_file_path, "w",newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=self.delimiter)
            writer.writerows(element_list)
