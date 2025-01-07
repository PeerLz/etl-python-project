import requests
from utils import log_message
import time

class Extractor:
    def __init__(self, api_key, base_url):
        self.base_url = base_url
        self.api_key = api_key
        

    def fetch_data(self, endpoint, params=None, retries=3):
        url = f"{self.base_url}/{endpoint}"
        if params is None:
            params = {}
        params['api_key'] = self.api_key 
        
        for attempt in range(retries):
            response = requests.get(url, params=params)
            if response.status_code == 200:
                log_message(f"Data fetched from {url}")
                return response.json()
            elif response.status_code == 401:
                log_message(f"Failed to fetch data from {url}. Status code: {response.status_code}")
                log_message("Invalid API key")
                return None
            elif response.status_code == 429:   
                log_message(f"Failed to fetch data from {url}. Status code: {response.status_code}")
                log_message(f"Retrying in {response.headers['Retry-After']} seconds")
                time.sleep(int(response.headers['Retry-After']))
            else:
                log_message(f"Failed to fetch data from {url}. Status code: {response.status_code}")
                return None
        if response.status_code == 200:
            log_message(f"Data fetched from {url}")
            return response.json()
        else:
            log_message(f"Failed to fetch data from {url}. Status code: {response.status_code}")    
            return None
    
    def fetch_movies(self, page=1):
        return self.fetch_data("movie/popular", {"page": page})
    
    def fetch_movie_details(self, movie_id):
        return self.fetch_data(f"movie/{movie_id}")
    
    def fetch_movie_genres(self):
        return self.fetch_data("genre/movie/list")  
    
    def fetch_all_movies(self, max_pages=5):
        all_movies = []
        for page in range(1, max_pages+1):
            data = self.fetch_movies(page)
            if data and "results" in data:
                all_movies.extend(data["results"])
            else:
                log_message("no more movies to fetch")
                break
        return all_movies
    