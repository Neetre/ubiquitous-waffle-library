'''

Neetre 2024
'''

from flask import Flask, render_template, request
from utils import *

app = Flask(__name__)


def handle_search(search_term, search_type):
    if search_type == 'title':
        search_books_webpage(search_term)
    elif search_type == 'author':
        search_books_webpage_author(search_term)
    elif search_type == 'genre':
        search_books_webpage_genre(search_term)
    elif search_type == 'type':
        search_books_webpage_type(search_term)
    elif search_type == 'year':
        search_books_webpage_year(search_term)


@app.route('/')
def books_page():
    create_books_webpage()
    return render_template('books.html')


@app.route('/home_page')
def home_page():
    books_page()


@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        search = request.form['search']
        search_type = request.form['search_type']
    else:
        search = request.args.get('search')
        search_type = request.args.get('search_type')
    handle_search(search, search_type)
    return render_template('books.html')


@app.route('/add_book', methods=['POST', 'GET'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        surname = request.form['surname']
        name = request.form['name']
        publisher = request.form['publisher']
        year = request.form['year']
        genre = request.form['genre']
        tipe = request.form['type']
        author = f"{surname} {name}"
        ic(title, author)
    else:
        title = request.args.get('title')
        surname = request.args.get('author')
        name = request.args.get('name')
        publisher = request.args.get('publisher')
        year = request.args.get('year')
        genre = request.args.get('genre')
        tipe = request.args.get('type')
        author = f"{surname} {name}"
        ic(title, author)
    add_book_webpage(title, author, publisher, year, genre, tipe)
    return render_template('books.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
