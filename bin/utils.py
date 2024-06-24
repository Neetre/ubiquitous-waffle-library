'''
Neetre 2024
'''

import argparse
from icecream import ic

from DataManager import DatabaseManager_books, DatabaseManager_status
from html_templates import *


def args_parsing():
    parser = argparse.ArgumentParser(description='PyTorch MNIST Example')
    parser.add_argument("-l", '--local', action="store_true", default=False,
                        help='Host the website localy')
    parser.add_argument("-v", '--verbose', action="store_true", default=False,
                        help='Prints everything')


    args = parser.parse_args()
    return args


class Book:
    def __init__(self, title, author, publisher, year, genre, tipe, code, link_cover="", desciption=""):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.genre = genre
        self.tipe = tipe
        self.code = code
        self.link_cover = link_cover
        self.description = desciption

    def __str__(self):
        return f"{self.title} by {self.author} published by {self.publisher} in {self.year} - {self.genre} - {self.tipe} - {self.code}"


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
    return [Book(*book[1:]) for book in books]


def create_books_webpage():
    books = read_books()
    
    with open("./templates/books.html", "w") as f:
        f.write(HEADER)
        
        for book in books:
            f.write(f"<tr><td><a href='/load_book?code={book.code}'>{book.title}</a></td><td>{book.author}</td><td>{book.publisher}</td><td>{book.year}</td><td>{book.genre}</td><td>{book.tipe}</td><td>{book.code}</td></tr>\n")

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
    books = read_books()
    
    with open("./templates/books.html", "w") as f:
        f.write(HEADER)
        
        for book in books:
            if search in [book[n] for n in range(len(book)-1)] or search in [book[n].lower() for n in range(len(book)-1)]:
                f.write(f"<tr><td><a href='/load_book?code={book.code}'>{book.title}</a></td><td>{book.author}</td><td>{book.publisher}</td><td>{book.year}</td><td>{book.genre}</td><td>{book.tipe}</td><td>{book.code}</td></tr>\n")
        f.write("\t</table>")
        f.write(HOME)
        f.write(FOOTER)

    ic("Books webpage created")


def search_books_webpage_author(author):
    books = read_books()
    
    with open("./templates/books.html", "w") as f:
        f.write(HEADER)
        
        for book in books:
            if author in book[2] or author in book[2].lower():
                f.write(f"<tr><td><a href='/load_book?code={book.code}'>{book.title}</a></td><td>{book.author}</td><td>{book.publisher}</td><td>{book.year}</td><td>{book.genre}</td><td>{book.tipe}</td><td>{book.code}</td></tr>\n")
        f.write("\t</table>")
        f.write(HOME)
        f.write(FOOTER)

    ic("Books webpage created")


def search_books_webpage_genre(genre):
    books = read_books()
    
    with open("./templates/books.html", "w") as f:
        f.write(HEADER)
        
        for book in books:
            if genre in book[5] or genre in book[5].lower():
                f.write(f"<tr><td><a href='/load_book?code={book.code}'>{book.title}</a></td><td>{book.author}</td><td>{book.publisher}</td><td>{book.year}</td><td>{book.genre}</td><td>{book.tipe}</td><td>{book.code}</td></tr>\n")
        f.write("\t</table>")
        f.write(HOME)
        f.write(FOOTER)
        
    ic("Books webpage created")

def search_books_webpage_type(tipe):
    books = read_books()
    
    with open("./templates/books.html", "w") as f:
        f.write(HEADER)

        for book in books:
            if tipe in book[6] or tipe in book[6].lower():
                f.write(f"<tr><td><a href='/load_book?code={book.code}'>{book.title}</a></td><td>{book.author}</td><td>{book.publisher}</td><td>{book.year}</td><td>{book.genre}</td><td>{book.tipe}</td><td>{book.code}</td></tr>\n")
        f.write("\t</table>")
        f.write(HOME)
        f.write(FOOTER)
    
    ic("Books webpage created")


def search_books_webpage_year(year):
    books = read_books()
    
    with open("./templates/books.html", "w") as f:
        f.write(HEADER)

        for book in books:
            if year in book[4] or year in book[4].lower():
                f.write(f"<tr><td><a href='/load_book?code={book.code}'>{book.title}</a></td><td>{book.author}</td><td>{book.publisher}</td><td>{book.year}</td><td>{book.genre}</td><td>{book.tipe}</td><td>{book.code}</td></tr>\n")
        f.write("\t</table>")
        f.write(HOME)
        f.write(FOOTER)
    
    ic("Books webpage created")


def add_book_webpage(title, author, publisher, year, genre, tipe):
    db = DatabaseManager_books()
    
    code = title[:3].upper() + author[:3].upper() + publisher[:3].upper() + str(year)
    book = Book(title, author, publisher, year, genre, tipe, code)
    db.write_book(book)
    create_books_webpage()


def update_book_webpage(code, title, author, publisher, year, genre, tipe):
    books = read_books()
    current_book = [book for book in books if book.code == code][0]

    updated_book = Book(
        title if title != current_book[1] else current_book[1],
        author if author != current_book[2] else current_book[2],
        publisher if publisher != current_book[3] else current_book[3],
        year if year != current_book[4] else current_book[4],
        genre if genre != current_book[5] else current_book[5],
        tipe if tipe != current_book[6] else current_book[6],
        current_book[7],
        current_book[8],
        current_book[9]
    )

    db = DatabaseManager_books()
    db.update_book(updated_book)
    create_books_webpage()


def delete_book_webpage(code):
    db = DatabaseManager_books()
    db_status = DatabaseManager_status()   # modified after status implementation
    books = read_books()
    book = [book for book in books if book.code == code][0]
    db.delete_book(book)
    db_status.delete_status(book.code)
    create_books_webpage()


def load_book_webpage(code):
    books = read_books()
    book = [book for book in books if book.code == code][0]
    
    with open("./templates/book.html", "w") as file:
        file.write(HEADER_BOOK_PAGE)
        file.write(f"<h1>Title: {book.title}</h1>")
        file.write(f"<h2>Author: {book.author}</h2>")
        file.write(f"<h2>Publisher: {book.publisher}</h2>")
        file.write(f"<h2>Year: {book.year}</h2>")
        file.write(f"<h2>Genre: {book.genre}</h2>")
        file.write(f"<h2>Type: {book.tipe}</h2>")
        file.write(f"<h2>Code: {book.code}</h2>")
        file.write(f"<h2>Description: {book.description}</h2>")
        file.write("<div class='cover'>")
        file.write("<img src=\"{{ url_for(\'static\',filename=\'covers/"+ book.link_cover + "\') }}\" alt=\'Cover of the book\'>")
        file.write(HOME)
        file.write("</div>")
        file.write(FOOTER)


def add_book_link(code, link):
    db = DatabaseManager_books()
    books = read_books()
    book = [book for book in books if book.code == code][0]
    book.link_cover = link
    db.update_book(book)
    load_book_webpage(code)


def create_status_webpage():
    db_status = DatabaseManager_status()

    books = read_books()

    for book in books:
        db_status.write_status(book)

    status_books = db_status.read_status()

    with open("./templates/status.html", "w") as f:
        f.write(STATUS_HEADER)

        for status in status_books:
            f.write(f"<tr><td><a href='/load_book?code={status[1]}'>{status[1]}</a></td><td>{status[2]}</td><td>{status[3]}</td><td>{status[4]}</td></tr>")

        f.write("</table>")
        f.write(STATUS_STATUS)
        f.write(STATUS_DATE)
        f.write(STATUS_NOTE)
        f.write(HOME)
        f.write(FOOTER)

    ic("Status webpage created")


def update_status_webpage(code, status):
    db_status = DatabaseManager_status()
    db_status.update_status(status, code)
    create_status_webpage()
