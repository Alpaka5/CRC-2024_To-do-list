from __future__ import print_function

import logging

import grpc

import todo_pb2_grpc, todo_pb2

import datetime
import argparse


def create_element(todo_element: todo_pb2.TodoElement):
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = todo_pb2_grpc.ToDoServiceStub(channel)
        print(todo_element)
        response: todo_pb2.TodoId = stub.CreateTodo(todo_element)
        print(f"Todo element created: {response.Id}")


def get_element(element_id: todo_pb2.TodoId):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = todo_pb2_grpc.ToDoServiceStub(channel)
        response: todo_pb2.TodoElement = stub.GetTodo(element_id)
        print(f"Received todo element: {response}")


def get_all_elements():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = todo_pb2_grpc.ToDoServiceStub(channel)
        print(f"Received todo elements:")
        for element in stub.GetAllTodos(todo_pb2.Empty()):
            print(f"{element}")


def finish_todo(element_id: todo_pb2.TodoId):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = todo_pb2_grpc.ToDoServiceStub(channel)
        response: todo_pb2.Succeed = stub.FinishTodo(element_id)
        print(f"Received status: {response}")


def edit_todo(element: todo_pb2.TodoElement):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = todo_pb2_grpc.ToDoServiceStub(channel)
        response: todo_pb2.Succeed = stub.EditTodo(element)
        print(f"Received status: {response}")


def remove_todo(element_id: todo_pb2.TodoId):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = todo_pb2_grpc.ToDoServiceStub(channel)
        response: todo_pb2.Succeed = stub.RemoveTodo(element_id)
        print(f"Received status: {response}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="To do list client", description="Enables work with to do list"
    )
    subparsers = parser.add_subparsers(help="Desired action to perform", dest="action")

    get_all_parser = subparsers.add_parser(
        "get_all", help="Gets all elements from to do list"
    )
    # Common arguments for actions that require ID of object to execute
    id_parent_parser = argparse.ArgumentParser(add_help=False)
    id_parent_parser.add_argument(
        "-i", "--id", help="ID of to do list element", required=True
    )
    # Common arguments for actions that require todo_pbs.TodoElement object to execute
    element_parent_parser = argparse.ArgumentParser(add_help=False)
    element_parent_parser.add_argument(
        "-t", "--title", type=str, help="Title of to do list element", required=True
    )
    element_parent_parser.add_argument(
        "-d",
        "--description",
        type=str,
        help="Description of to do list element",
        required=True,
    )
    element_parent_parser.add_argument(
        "-f", "--finished", type=bool, help="Finishes element in to do", default=False
    )

    create_parser = subparsers.add_parser(
        "create",
        help="Creates element in to do list",
        parents=[element_parent_parser],
    )

    edit_parser = subparsers.add_parser(
        "edit",
        help="Edits element in to do list",
        parents=[id_parent_parser, element_parent_parser],
    )
    get_parser = subparsers.add_parser(
        "get", help="Gets element from to do list", parents=[id_parent_parser]
    )

    finish_parser = subparsers.add_parser(
        "finish", help="Finishes element in to do list", parents=[id_parent_parser]
    )

    remove_parser = subparsers.add_parser(
        "remove", help="Removes element from to do list", parents=[id_parent_parser]
    )

    arguments = parser.parse_args()

    if arguments.action in ["create", "edit"]:
        element = todo_pb2.TodoElement(
            Id=None,
            Title=arguments.title,
            Description=arguments.description,
            Finished=arguments.finished,
        )
        if arguments.action == "create":
            create_element(element)
        elif arguments.action == "edit":
            element.Id = arguments.id
            edit_todo(element)

    elif arguments.action in ["get", "finish", "remove"]:
        todo_id = todo_pb2.TodoId(Id=arguments.id)
        if arguments.action == "get":
            get_element(todo_id)
        elif arguments.action == "finish":
            finish_todo(todo_id)
        elif arguments.action == "remove":
            remove_todo(todo_id)

    elif arguments.action == "get_all":
        get_all_elements()
