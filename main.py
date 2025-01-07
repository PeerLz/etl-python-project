from extract import Extractor
from transform import Transform 
from loader import Loader
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

API_KEY="80a12cfe9baae08e99a2e3418de32df2"
BASE_URL="https://api.themoviedb.org/3"
DB_PATH="movies.db"

def run_etl_pipeline():
    extractor = Extractor(api_key=API_KEY, base_url=BASE_URL)
    transformer = Transform()
    loader = Loader(db_path=DB_PATH)
    
    
    try:
        logging.info("Extracting movies data")
        raw_movies=[]
        for page in range(1,6):
            logging.info(f"Extracting page {page}")
            data=extractor.fetch_movies(page=page)
            if data and "results" in data:
                raw_movies.extend(data["results"])
            else:
                logging.warning("No more movies to fetch on page {page}")
                break
    
        logging.info("starting data transformation")
        cleaned_movies=transformer.clean_movies(raw_movies)
        
        logging.info("starting data loading")
        loader.insert_movies(cleaned_movies)
        
        logging.info("ETL pipeline completed")
    except Exception as e:
        logging.error(f"ETL pipeline failed: {e}")        
        
    finally:
        loader.close_connection()
        logging.info("Database connection closed")
        
if __name__ == "__main__":
    run_etl_pipeline()
    
    
    