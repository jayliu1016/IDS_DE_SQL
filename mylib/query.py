import sqlite3

def connect_to_db(db_name):
    """Establish a connection to the SQLite database."""
    return sqlite3.connect(db_name)

def create_table(cursor):
    """Create books table if it doesn't exist."""
    cursor.execute('''CREATE TABLE IF NOT EXISTS books
                      (id INTEGER PRIMARY KEY, title TEXT, author TEXT, price REAL)''')

def insert_book(cursor, title, author, price):
    """Insert a new book record into the books table."""
    cursor.execute('INSERT INTO books (title, author, price) VALUES (?, ?, ?)', (title, author, price))

def fetch_all_books(cursor):
    """Fetch all books from the books table."""
    cursor.execute('SELECT * FROM books')
    return cursor.fetchall()

