def transform_data(df):
    """Perform any necessary transformations on the DataFrame."""
    # Example: Remove any rows with missing values
    return df.dropna()

def load_data_to_db(df, cursor):
    """Load DataFrame data into the database."""
    for _, row in df.iterrows():
        cursor.execute('INSERT INTO books (title, author, price) VALUES (?, ?, ?)', 
                       (row['title'], row['author'], row['price']))
