import sqlite3

def create_database():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    print("Opened database successfully")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        release_date TEXT,
        popularity REAL,
        vote_average REAL,
        genre_ids TEXT
        );
""")
    
    conn.commit()
    conn.close()
    
    
if __name__ == "__main__":
    create_database()
    
    