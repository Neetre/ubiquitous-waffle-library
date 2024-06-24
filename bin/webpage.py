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
    create_books_webpage()
    return render_template('books.html')


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


@app.route('/update_book', methods=['POST', 'GET'])
def update_book():
    if request.method == 'POST':
        code = request.form['code']
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
        code = request.args.get('code')
        title = request.args.get('title')
        surname = request.args.get('author')
        name = request.args.get('name')
        publisher = request.args.get('publisher')
        year = request.args.get('year')
        genre = request.args.get('genre')
        tipe = request.args.get('type')
    update_book_webpage(code, title, author, publisher, year, genre, tipe)
    return render_template('books.html')


@app.route('/delete_book', methods=['POST', 'GET'])
def delete_book():
    if request.method == 'POST':
        code = request.form['code']
    else:
        code = request.args.get('code')
    delete_book_webpage(code)
    return render_template('books.html')


@app.route('/status_page')
def status_page():
    create_status_webpage()
    return render_template('status.html')


@app.route('/status', methods=['POST', 'GET'])
def update_status():
    if request.method == 'POST':
        code = request.form['code']
        status = request.form['status']
    else:
        code = request.args.get('code')
        status = request.args.get('status')
    update_status_webpage(code, status)
    return render_template('status.html')


@app.route('/load_book', methods=['POST', 'GET'])
def load_book():
    if request.method == 'POST':
        code = request.form['code']
    else:
        code = request.args.get('code')
    load_book_webpage(code)
    return render_template('book.html')


@app.route('/add_link', methods=['POST', 'GET'])
def add_link():
    if request.method == 'POST':
        code = request.form['code']
        link = request.form['link']
    else:
        code = request.args.get('code')
        link = request.args.get('link')
    add_book_link(code, link)
    return render_template('book.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
