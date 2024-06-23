'''
Templates for the various webpages

Neetre 2024
'''

HEADER = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Book of the Library</title>
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link rel='stylesheet' type='text/css' href="{{ url_for('static', filename='styles/styles.css') }}">
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    </head>
    <body>
        <header>
            <div class="container">
                <h1>Book of the Library</h1>
            </div>
        </header>
        <main>
            <div class="container">
                <section class="book-section">
                    <h2>Books Available</h2>
                    <table>
                        <thead>
                            <tr>
                            <th>Title</th>
                            <th>Author</th>
                            <th>Publisher</th>
                            <th>Year</th>
                            <th>Genre</th>
                            <th>Type</th>
                            <th>Code</th>
                            </tr>
                        </thead>
                        <tbody>
'''

HOME = '''
                    <form action='/home_page' method='get'>
                    <input type='submit' value='Home'>
                    </form>
'''

SEARCH_BOOKS = '''
                    <form action='/search_books' method='post'>
                    <input type='text' name='search' placeholder='Insert the name'>
                    <input type='submit' value='Search Book'>
                    </form>
'''

SEARCH_BOOKS_AUTHOR = '''
                    <form action='/search_author' method='post'>
                    <input type='text' name='author' placeholder='Author'>
                    <input type='submit' value='Search Author'>
                    </form>
'''

SEARCH_BOOKS_GENRE = '''
                    <form action='/search_genre' method='post'>
                    <input type='text' name='genre' placeholder='Insert the genre'>
                    <input type='submit' value='Search Genre'>
                    </form>
'''

SEARCH_BOOKS_TYPE = '''
                    <form action='/search_type' method='post'>
                    <input type='text' name='type' placeholder='Insert the type'>
                    <input type='submit' value='Search Type'>
                    </form>
'''

ADD_BOOK = '''
                    <form action='/add_book' method='post' class='book-form'>
                    <input type='text' name='title' placeholder='Title'>
                    <input type='text' name='surname' placeholder='Author surname'>
                    <input type='text' name='name' placeholder='Author name'>
                    <input type='text' name='publisher' placeholder="Publisher'>
                    <input type='text' name='year' placeholder='Year'>
                    <input type='text' name='genre' placeholder='Genre'>
                    <input type='text' name='type' placeholder='Type'>
                    <input type='submit' value="Add Book">
                    </form>
'''

UPDATE_BOOK = '''
                    <form action='/update_book' method='post' class='book-form'>
                    <input type='text' name='code' placeholder='Code'>
                    <input type='text' name='title' placeholder='Title'>
                    <input type='text' name='author' placeholder='Author'>
                    <input type='text' name='publisher' placeholder="Publisher'>
                    <input type='text' name='year' placeholder='Year'>
                    <input type='text' name='genre' placeholder='Genre'>
                    <input type='text' name='type' placeholder='Type'>
                    <input type='submit' value="Update Book">
                    </form>
'''

DELETE_BOOK = '''
                    <form action='/delete_book' method='post'>
                    <input type='text' name='code' placeholder='Code'>
                    <input type='submit' value='Delete Book'>
                    </form>
'''

BOOK_ADD_LINK = '''
                    <form action='/add_link' method='post' class='book-form'>
                    <input type='text' name='code' placeholder='Code'>
                    <input type='text' name='photo_link' placeholder='Link cover'>
                    <input type='submit' value="Add cover link">
                    </form>
'''

BOOK_ADD_DESCRIPTION = '''
                    <form action='/add_description' method='post' class='book-form'>
                    <textarea id="book-description" name="book-description" placeholder="Write the book description here..."></textarea>
                    <button type="submit" class="submit-btn">Submit</button>
                    </form>
'''


FOOTER = '''
            </div>
        </main>
        <footer>
            <div class="container">
                <p>&copy; 2024 Neetre. All rights reserved.</p>
            </div>
        </footer>
    </body>
</html>
'''

STATUS_HEADER = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Status of the Books</title>
        <link rel='stylesheet' type='text/css' href="{{ url_for('static', filename='styles/style.css') }}
    </head>
    <body>
        <table border='1'>
            <tr>
            <th>Code</th>
            <th>Status</th>
            <th>Date</th>
            <th>Note</th>
            </tr>
'''

STATUS = '''
        <form action='/status_page' method='get'>
        <input type='submit' value='Show Status'>
        <form>
'''

STATUS_STATUS = '''
        <form action='/status' method='post'
        <input type='text' name='code' placeholder='Insert Code'>
        <input type='text' name='status' placeholder='Insert Status'>
        <input type='submit' value='Add Status'>
        </form>
'''

STATUS_DATE = '''

'''

STATUS_REMOVE = '''

'''

HEADER_BOOK_PAGE = '''

'''
