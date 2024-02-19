import argparse
import random

from client import Client
import protobuf.book_pb2 as book_pb2

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="Client of Book Store", description="Enables work with to do list"
    )
    subparsers = parser.add_subparsers(help="Desired action to perform", dest="action")

    # Common arguments for actions that require todo_pbs.TodoElement object to execute
    category_parent_parser = argparse.ArgumentParser(add_help=False)
    title_parent_parser = argparse.ArgumentParser(add_help=False)
    title_parent_parser.add_argument(
        "-t", "--title", type=str, help="Title of Book", required=True
    )
    category_parent_parser.add_argument(
        "-c",
        "--category",
        type=str,
        help="""
        Book category:     
        UNSPECIFIED = 0;
        SCIENCE_FICTION = 1;
        SELF_HELP = 2;
        MYSTERY = 3;
        """,
        required=True,
    )


    create_parser = subparsers.add_parser(
        "add",
        help="Add a new book",
        parents=[title_parent_parser, category_parent_parser],
    )

    remove_parser = subparsers.add_parser(
        "remove",
        help="Remove book from database",
        parents=[title_parent_parser],
    )
    get_parser = subparsers.add_parser(
        "get", help="Gets element from book store", parents=[title_parent_parser]
    )
    get_all_parser = subparsers.add_parser(
        "get_all", help="Gets all elements from book store"
    )


    arguments = parser.parse_args()

    client = Client()

    match arguments.action:
        case "add":
            # book = book_pb2.Book(
            #     id=random.randint(1, 10000),
            #     title=arguments.title,
            #     category=int(arguments.category),
            # )
            # client.add_book(book)
            pass

        case "get":
            # book_title = book_pb2.BookTitle(
            #     title=arguments.title
            # )
            # client.get_book(book_title)
            pass
        case "get_all":
            # client.get_all_books()
            pass
        case "remove":
            # book_title = book_pb2.BookTitle(
            #     title=arguments.title
            # )
            # client.delete_book(book_title)
            pass

        case _:
            print("Unexpected action...")
