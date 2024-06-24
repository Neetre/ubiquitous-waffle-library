'''
Neetre 2024
'''

import argparse
from icecream import ic

from DataManager import DatabaseManager_books
from html_templates import *


def args_parsing():
    parser = argparse.ArgumentParser(description='PyTorch MNIST Example')
    parser.add_argument("-l", '--local', action="store_true", default=False,
                        help='Host the website localy')
    parser.add_argument("-v", '--verbose', action="store_true", default=False,
                        help='Prints everything')


    args = parser.parse_args()
    return args


class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def __str__(self) -> str:
        return f"{self.name} located in {self.location} with {len(self.books)} books"


class Book:
    def __init__(self, title, author, publisher, year, genre, type, code, link_cover="", desciption=""):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.genre = genre
        self.type = type
        self.code = code
        self.link_cover = link_cover
        self.desciption = desciption

    def __str__(self):
        return f"{self.title} by {self.author} published by {self.publisher} in {self.year} - {self.genre} - {self.type} - {self.code}"


class BookStatus:
    def __init__(self, book: Book, status, date, note):
        self.book = book
        self.status = status
        self.date = date
        self.note = note

    def __str__(self):
        return f"{self.book.title} - {self.status} - {self.date} - {self.note}"


def read_books():
    db = DatabaseManager_books()
    books = db.read_books()
    library = Library("Library", "Rome")
    library.add_book([Book(book[1], book[2], book[3], book[4], book[5], book[6], book[7], book[8], book[9]) for book in books])
    return library


def create_books_webpage():
    db = DatabaseManager_books()  # keep the default path
    books = db.read_books()
    
    with open("./templates/books.html", "w") as f:
        f.write(HEADER)
        
        for book in books:
            f.write(f"<tr><td><a href='/load_book?code={book[7]}'>{book[1]}</a></td><td>{book[2]}</td><td>{book[3]}</td><td>{book[4]}</td><td>{book[5]}</td><td>{book[6]}</td><td>{book[7]}</td></tr>\n")

        f.write("</tbody>")
        f.write("</table>")
        f.write("</section>")
        
        f.write("\t\t\t\t<section class='from-section'>\n")
        f.write("\t\t\t\t\t<h2>Add/Remove Book</h2>\n")
        f.write(ADD_BOOK)
        f.write("<br>")
        f.write(UPDATE_BOOK)
        f.write("<br>")
        f.write(DELETE_BOOK)
        f.write("</section>")
        
        f.write("<section class='search-section'>")
        f.write("<h2>Search Book</h2>")
        f.write(SEARCH_BOOKS)
        f.write("<br>")
        f.write(SEARCH_BOOKS_AUTHOR)
        f.write("<br>")
        f.write(SEARCH_BOOKS_GENRE)
        f.write("<br>")
        f.write(SEARCH_BOOKS_TYPE)
        f.write("</section>")
        
        f.write("<h2>Add link of the book cover</h2>")
        f.write(BOOK_ADD_LINK)
        
        f.write("<section class='status-section'>")
        f.write(STATUS)
        f.write("</section>")
        
        f.write(FOOTER)
    ic("Books webpage created")
    

def search_books_webpage(search):
    db = DatabaseManager_books()
    books = db.read_books()
    
    with open("./templates/books.html", "w") as f:
        f.write(HEADER)
        
        for book in books:
            if search in [book[n] for n in range(len(book)-1)] or search in [book[n].lower() for n in range(len(book)-1)]:
                f.write(f"<tr><td><a href='/load_book?code={book[7]}'>{book[1]}</a></td><td>{book[2]}</td><td>{book[3]}</td><td>{book[4]}</td><td>{book[5]}</td><td>{book[6]}</td><td>{book[7]}</td></tr>")
        f.write("\t</table>")
        f.write(HOME)
        f.write(FOOTER)

    ic("Books webpage created")


def search_books_webpage_author(author):
    db = DatabaseManager_books()
    books = db.read_books()
    
    with open("./templates/books.html", "w") as f:
        f.write(HEADER)
        
        for book in books:
            if author in book[2] or author in book[2].lower():
                f.write(f"<tr><td><a href='/load_book?code={book[7]}'>{book[1]}</a></td><td>{book[2]}</td><td>{book[3]}</td><td>{book[4]}</td><td>{book[5]}</td><td>{book[6]}</td><td>{book[7]}</td></tr>")
        f.write("\t</table>")
        f.write(HOME)
        f.write(FOOTER)

    ic("Books webpage created")


def search_books_webpage_genre(genre):
    db = DatabaseManager_books()
    books = db.read_books()
    
    with open("./templates/books.html", "w") as f:
        f.write(HEADER)
        
        for book in books:
            if genre in book[5] or genre in book[5].lower():
                f.write(f"<tr><td><a href='/load_book?code={book[7]}'>{book[1]}</a></td><td>{book[2]}</td><td>{book[3]}</td><td>{book[4]}</td><td>{book[5]}</td><td>{book[6]}</td></tr>")
        f.write("\t</table>")
        f.write(HOME)
        f.write(FOOTER)
        
    ic("Books webpage created")

def search_books_webpage_type(type):
    db = DatabaseManager_books()
    books = db.read_books()
    
    with open("./templates/books.html", "w") as f:
        f.write(HEADER)

        for book in books:
            if type in book[6] or type in book[6].lower():
                f.write(f"<tr><td><a href='/load_book?code={book[7]}'>{book[1]}</a></td><td>{book[2]}</td><td>{book[3]}</td><td>{book[4]}</td><td>{book[5]}</td><td>{book[6]}</td></tr>")
        f.write("\t</table>")
        f.write(HOME)
        f.write(FOOTER)
    
    ic("Books webpage created")


def search_books_webpage_year(year):
    db = DatabaseManager_books()
    books = db.read_books()
    
    with open("./templates/books.html", "w") as f:
        f.write(HEADER)

        for book in books:
            if type in book[6] or type in book[6].lower():
                f.write(f"<tr><td><a href='/load_book?code={book[7]}'>{book[1]}</a></td><td>{book[2]}</td><td>{book[3]}</td><td>{book[4]}</td><td>{book[5]}</td><td>{book[6]}</td></tr>")
        f.write("\t</table>")
        f.write(HOME)
        f.write(FOOTER)
    
    ic("Books webpage created")


def add_book_webpage(title, author, publisher, year, genre, type):
    db = DatabaseManager_books()
    
    code = title[:3].upper() + author[:3].upper() + publisher[:3] + str(year)
    book = Book(title, author, publisher, year, genre, type, code)
    db.write_book(book)
    create_books_webpage()


def write_book_test():
    book = Book("Test", "Test", "Test", 2021, "Test", "Test", "TST")
    library = read_books()
    library.add_book(book)
    for book in library.books:
        print(book)


if __name__ == "__main__":
    write_book_test()
