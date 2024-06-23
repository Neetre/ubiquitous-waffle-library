'''
Neetre 2024
'''

from DataManager import DatabaseManager_books

class Book:
    def __init__(self, title, author, publisher, year, genre, type, code, link_cover=""):
        self.tile = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.genre = genre
        self.type = type
        self.code = code
        self.link_cover = link_cover
        
class BookStatus:
    def __init__(self, book: Book, status, date, msg):
        self.book = book
        self.status = status
        self.date = date
        self.msg = msg

