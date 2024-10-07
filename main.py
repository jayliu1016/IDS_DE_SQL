import sqlite3

# Connect to the database
conn = sqlite3.connect('BooksDB.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS books
                  (id INTEGER PRIMARY KEY, title TEXT, author TEXT, price REAL)''')

# Insert data
def insert_book(title, author, price):
    cursor.execute('INSERT INTO books (title, author, price) VALUES (?, ?, ?)', (title, author, price))
    conn.commit()

# Query data
def get_books():
    cursor.execute('SELECT * FROM books')
    return cursor.fetchall()

# Update data
def update_book_price(book_id, new_price):
    cursor.execute('UPDATE books SET price = ? WHERE id = ?', (new_price, book_id))
    conn.commit()

# Delete data
def delete_book(book_id):
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()

# Example usage
insert_book('The Great Gatsby', 'F. Scott Fitzgerald', 10.99)
books = get_books()
print(books)
update_book_price(1, 12.99)
delete_book(1)

# Close the connection
conn.close()

