"""Query the database"""

import sqlite3


def query():
    """Query the database for the top 5 rows of the GroceryDB table"""
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT avg (count_products) FROM GroceryDB")
    print("Sum of count_products:", cursor.fetchall())
    cursor.execute("SELECT sum (count_products) FROM GroceryDB")
    print("Avg of count_products:", cursor.fetchall())
    conn.close()
    return "Success"


print(query())
