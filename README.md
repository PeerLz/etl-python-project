# ETL Python Project with Docker Integration

This project demonstrates an **ETL (Extract, Transform, Load)** pipeline written in Python. It extracts movie data from the TMDB API, transforms and enriches it, and loads it into an SQLite database for further analysis.

The project is containerized with **Docker**, making it easy to set up and run in any environment.

---

## **Features**
- Extracts movie data using the TMDB API.
- Cleans, enriches, and transforms the extracted data.
- Stores the processed data into an SQLite database (`movies.db`).
- Modular design with separate components for **extraction**, **transformation**, and **loading**.
- Includes standalone utilities for database querying and testing.
- Dockerized for easy deployment.

---

## **Project Structure**

```plaintext
proj_de/
├── create_db.py       # Script to create the database schema
├── extract.py         # Extractor module: fetches data from the TMDB API
├── transform.py       # Transformer module: cleans and enriches data
├── loader.py          # Loader module: loads data into SQLite database
├── main.py            # Main script: orchestrates the ETL pipeline
├── movies.db          # SQLite database file (created by `create_db.py`)
├── query_db.py        # Utility script: queries the database for validation
├── test_fetch.py      # Utility script: tests the extraction process
├── utils.py           # Utility functions for logging and other helpers
├── requirements.txt   # Lists Python dependencies
└── Dockerfile         # Instructions to build the Docker image
