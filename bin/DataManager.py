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
                            link_cover TEXT,
                            description text
                            )''')
        self.cursor.execute("CREATE INDEX IF NOT EXISTS idx_title ON book(title)")
        self.cursor.execute("CREATE INDEX IF NOT EXISTS idx_author ON book(author)")
        self.cursor.execute("CREATE INDEX IF NOT EXISTS idx_code ON book(code)")
        self.connection.commit()
        
    def check_duplicate(self, book: object):
        self.cursor.execute("SELECT * FROM book WHERE title=? AND author=? OR code=?",
                            (book.title, book.author, book.code))
        return self.cursor.fetchone() is not None
    
    def write_book(self, book):
        if not self.check_duplicate(book):
            self.cursor.execute('''INSERT INTO book
                                (title, author, publisher, year, genre, type, code, link_cover, description)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                                (book.title, book.author, book.publisher, book.year, book.genre, book.tipe, book.code, book.link_cover, book.description))
            self.connection.commit()
            
    def read_books(self):
        self.cursor.execute("SELECT * FROM book ORDER BY author ASC, title ASC")
        return self.cursor.fetchall()
    
    def update_book(self, book):
        self.cursor.execute('''UPDATE book
                            SET title=?, author=?, publisher=?, year=?, genre=?, type=?, link_cover=? description=?
                            WHERE code=?''',
                            (book.title, book.author, book.publisher, book.year, book.genre, book.tipe, book.link_cover, book.description, book.codice))
        self.connection.commit()
        
    def update_code(self, book):
        pass
    
    def delete_book(self, book):
        self.cursor.execute("DELETE FROM book WHERE author=? AND title=? OR code=?",
                            (book.author, book.title, book.code))
        self.connection.commit()
        
    def __del__(self):
        if self.connection:
            self.connection.close()


class DatabaseManager_status:
    def __init__(self, db_file="../data/books.db"):
        self.db_file = db_file
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()
        self.create_database()

    def create_database(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS status (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            code TEXT,
                            status TEXT,
                            date TEXT,
                            note TEXT
                            )''')
        self.cursor.execute("CREATE INDEX IF NOT EXISTS idx_code ON status(code)")
        self.connection.commit()

    def check_duplicate(self, book):
        self.cursor.execute("SELECT * FROM status WHERE code=?",
                             (book.code,))
        return self.cursor.fetchone() is not None

    def write_status(self, book, status='Available', date='N/A', note='No note'):
        if not self.check_duplicate(book):
            self.cursor.execute('''INSERT INTO status
                                (code, status, date, note)
                                VALUES (?, ?, ?, ?)''',
                                (book.code, status, date, note))
            self.connection.commit()

    def read_status(self):
        self.cursor.execute("SELECT * FROM status")
        return self.cursor.fetchall()
    
    def update_status(self, status, code):
        self.cursor.execute("UPDATE status SET status=? WHERE code=?",
                            (status, code))
        self.connection.commit()

    def delete_status(self, code):
        self.cursor.execute("DELETE FROM status WHERE code=?",
                            (code,))
        self.connection.commit()


