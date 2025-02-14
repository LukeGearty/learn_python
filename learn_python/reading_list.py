import json
import os

def get_book():
    book = input("What is the name of the book?: ")
    return book


def get_author():
    author = input("Who is the author of the book? If there is more than one author, separate them with a '&': ")
    return author


def get_date():
    date = input("When did you finish the book? Enter it in this format: YYYY-DD-MM: ")
    return date


def main():


    filename = "reading.json"

    

    if os.path.exists(filename):
        with open(filename, "r") as json_file:
            try:
                books = json.load(json_file)
                if not isinstance(books, list):
                    books = []
            except json.JSONDecodeError:
                books = []
    else:
        books = []
    
    book_data = {
        "book": get_book(),
        "author": get_author(),
        "date": get_date(),
    }

    books.append(book_data)

    with open(filename, "w") as json_file:
        json.dump(books, json_file, indent=4)


if __name__ == "__main__":
    main()
