from mylib.extract import load_data_from_csv
from mylib.query import connect_to_db, create_table, insert_book, fetch_all_books
from mylib.transform_load import transform_data, load_data_to_db

# Connect to the database
conn = connect_to_db('BooksDB.db')
cursor = conn.cursor()

# Create table
create_table(cursor)

# Insert example data
insert_book(cursor, 'The Great Gatsby', 'F. Scott Fitzgerald', 10.99)
conn.commit()

# Fetch and print data
books = fetch_all_books(cursor)
print(books)

# Close the connection
conn.close()

