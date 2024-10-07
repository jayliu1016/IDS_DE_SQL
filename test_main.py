import sqlite3
import pytest
from main import insert_book, get_books, update_book_price, delete_book

@pytest.fixture
def setup_database():
    conn = sqlite3.connect('BooksDB.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS books')
    cursor.execute('''CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, price REAL)''')
    yield conn, cursor
    conn.close()

def test_insert_book(setup_database):
    conn, cursor = setup_database
    insert_book('1984', 'George Orwell', 8.99)
    cursor.execute('SELECT * FROM books')
    result = cursor.fetchone()
    assert result == (1, '1984', 'George Orwell', 8.99)

def test_update_book_price(setup_database):
    conn, cursor = setup_database
    insert_book('To Kill a Mockingbird', 'Harper Lee', 7.99)
    update_book_price(1, 9.99)
    cursor.execute('SELECT price FROM books WHERE id = 1')
    result = cursor.fetchone()
    assert result[0] == 9.99

def test_delete_book(setup_database):
    conn, cursor = setup_database
    insert_book('Pride and Prejudice', 'Jane Austen', 6.99)
    delete_book(1)
    cursor.execute('SELECT * FROM books')
    result = cursor.fetchone()
    assert result is None

