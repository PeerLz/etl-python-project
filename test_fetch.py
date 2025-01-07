from extract import Extractor

# Configuration
API_KEY = "80a12cfe9baae08e99a2e3418de32df2"  # Replace with your TMDB API key
BASE_URL = "https://api.themoviedb.org/3"

if __name__ == "__main__":
    # Initialize the Extractor
    extractor = Extractor(api_key=API_KEY, base_url=BASE_URL)

    # Test fetch_data (generic API call)
    print("Testing fetch_data:")
    raw_data = extractor.fetch_data("movie/popular", {"page": 1})
    if raw_data:
        print(f"Raw data fetched (keys): {list(raw_data.keys())}")
        print(f"Number of results: {len(raw_data.get('results', []))}")
    else:
        print("Failed to fetch data.")

    # Test fetch_movies (specific API call)
    print("\nTesting fetch_movies:")
    movies_data = extractor.fetch_movies(page=1)
    if movies_data:
        print(f"Movies data fetched (keys): {list(movies_data.keys())}")
        print(f"Sample movie: {movies_data['results'][0]}")
    else:
        print("Failed to fetch movies.")
