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
        <link rel='stylesheet' type='text/css' href="{{url_for('static', filename='styles/styles.css') }}">
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