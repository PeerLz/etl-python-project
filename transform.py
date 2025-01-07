class Transform:
    def __init__(self):
        pass
    
    def clean_movies(self, movies):
        
        cleaned_movies = []
        for movie in movies:
            cleaned_movie = {
                "id": movie.get("id",None),
                "title": movie.get("title","Unknown title"),
                "release_date": movie.get("release_date","Unknown release date"), 
                "popularity": movie.get("popularity",0.0),
                "vote_average": movie.get("vote_average",0.0),
                "genre_ids": str(movie.get("genre_ids",[]))
            }
            cleaned_movies.append(cleaned_movie)
        return cleaned_movies

    def flatten_genres(self, genres):
        return {genre["id"]:genre["name"] for genre in genres}
    
    def enrich_movies(self, movies):
        for movie in movies:
            movie["is_highly_popular"] = movie["popularity"] > 8.0  
            
            if movie["popularity"] > 10.0:
                movie["popularity_type"] = "Very High"
            elif movie["popularity"] > 5.0:
                movie["popularity_type"] = "Moderate"
            else:
                movie["popularity_type"] = "Low"
        return movies



    
