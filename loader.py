import sqlite3
from utils import log_message

class Loader:
    def __init__(self, db_path="movies.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        
    def insert_movies(self, movies):
        cursor = self.conn.cursor()
        try:
            cursor.executemany("""
                INSERT OR REPLACE INTO movies (id, title, release_date, popularity, vote_average, genre_ids)
                VALUES (:id, :title, :release_date, :popularity, :vote_average, :genre_ids);
            """, movies)
            self.conn.commit()
            log_message(f"{len(movies)} movies inserted into database")
        except sqlite3.Error as e:
            log_message(f"Error inserting movies: {e}")
        except Exception as e:
            log_message(f"Error inserting movies: {e}")
            
    def close_connection(self):
        self.conn.close()
        log_message("Database connection closed")
    
    
    
        

