import sqlite3

def list_tables(db_path="movies.db"):
    """
    Connect to the SQLite database and list all tables.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Query to list tables
    #cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    cursor.execute("select * from movies")
    tables = cursor.fetchall()
    
    print("Data in table:")
    for table in tables:
        print(table)

    conn.close()

if __name__ == "__main__":
    list_tables()
