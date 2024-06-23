'''

Neetre 2024
'''

from flask import Flask, render_template, request
from utils import *

app = Flask(__name__)


@app.route('/')
def books_page():
    create_books_webpage()
    return render_template('books.html')


@app.route('/home_page')
def home_page():
    create_books_webpage()
    return render_template('books.html')


@app.route('/search_books', methods=['POST', 'GET'])
def search_book():
    if request.method == 'POST':
        search = request.form['search']
    else:
        search = request.args.get('search')
    search_books_webpage(search)
    return render_template('books.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
