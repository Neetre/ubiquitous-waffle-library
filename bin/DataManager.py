import sqlite3
import os

class DatabaseManager_books:
    def __init__(self, db_file="../data/books.db"):
        self.db_file = db_file
        
        if not os.path.exists(os.path.dirname(self.db_file)):
            os.makedirs(os.path.dirname(self.db_file))
        
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()
        self.create_database()
        
    def create_database(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS book (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT,
                            author TEXT,
                            publisher TEXT,
                            year INTEGER,
                            genre TEXT,
                            type TEXT,
                            code TEXT UNIQUE,
                            link_cover TEXT
                            )''')
        self.connection.commit()
        
    def check_duplicate(self, book: object):
        self.cursor.execute("SELECT * FROM book WHERE title=? AND author=? OR code=?",
                            (book.title, book.author, book.code))
        return self.cursor.fetchone() is not None
    
    def write_book(self, book):
        if not self.check_duplicate(book):
            self.cursor.execute("INSERT INTO book (title, author, publisher, year, genre, type, code, link_cover) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                                (book.title, book.author, book.editor, book.year, book.genre, book.type, book.code, book.link_cover))
            self.connection.commit()
            
    def read_books(self):
        self.cursor.execute("SELECT * FROM book ORDER BY author ASC, title ASC")
        return self.cursor.fetchall()
    
    def update_book(self, book):
        self.cursor.execute("UPDATE book SET title=?, author=?, publisher=?, year=?, genre=?, type=?, link_cover=? WHERE code=?",
                            (book.title, book.author, book.editor, book.year, book.genre, book.type, book.link_cover, book.codice))
        self.connection.commit()
        
    def update_code(self, book):
        pass
    
    def delete_book(self, book):
        self.cursor.execute("DELETE FROM book WHERE author=? AND title=? OR code=?",
                            (book.author, book.title, book.code))
        self.connection.commit()
        
    def search_book(self, search):
        pass
        
    def __del__(self):
        if self.connection:
            self.connection.close()
