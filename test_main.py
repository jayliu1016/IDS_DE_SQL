import pytest
import sqlite3
from mylib.query import connect_to_db, create_table, insert_book, fetch_all_books
from mylib.transform_load import load_data_to_db
from mylib.extract import load_data_from_csv

# Setup fixture for database connection and table creation
@pytest.fixture
def setup_database():
    conn = connect_to_db('BooksDB.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS books')
    create_table(cursor)
    yield conn, cursor
    conn.close()

# Test the insert_book function
def test_insert_book(setup_database):
    conn, cursor = setup_database
    insert_book(cursor, '1984', 'George Orwell', 8.99)
    conn.commit()
    cursor.execute('SELECT * FROM books')
    result = cursor.fetchone()
    assert result == (1, '1984', 'George Orwell', 8.99)

# Test the fetch_all_books function
def test_fetch_all_books(setup_database):
    conn, cursor = setup_database
    insert_book(cursor, 'To Kill a Mockingbird', 'Harper Lee', 7.99)
    conn.commit()
    books = fetch_all_books(cursor)
    assert len(books) == 1
    assert books[0] == (1, 'To Kill a Mockingbird', 'Harper Lee', 7.99)

# Test loading data from CSV and inserting it into the database
def test_load_data_from_csv_and_insert(setup_database):
    conn, cursor = setup_database
    # Assuming spotify.csv is used as a dummy for books data with columns: title, author, price
    df = load_data_from_csv('spotify.csv')  # Replace 'spotify.csv' with the correct path or dataset
    df = df[['title', 'author', 'price']]  # Make sure columns align with your schema
    load_data_to_db(df, cursor)
    conn.commit()
    cursor.execute('SELECT COUNT(*) FROM books')
    count = cursor.fetchone()[0]
    assert count == len(df)

