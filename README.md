# Trademarkia - AI/ML Engineer Task

## Semantic Search System

This project implements a **semantic search system** that retrieves results based on meaning rather than exact keyword matching.

The system uses **sentence embeddings, FAISS vector search, clustering, and semantic caching** to improve search performance.

---

## Features

- Semantic search using embeddings
- Fast similarity search using FAISS
- Intelligent semantic cache
- Query clustering
- Cache statistics tracking
- REST API built with FastAPI

---

## Project Structure

semantic_search_system/

api/ → FastAPI endpoints

cache/ → Semantic caching logic

clustering/ → Query clustering

embeddings/ → Text embedding generation

vector_store/ → FAISS vector search

data_loader.py → Dataset loading

requirements.txt → Dependencies

---

## Installation

Clone the repository

git clone https://github.com/your-username/semantic-search-system.git

Go to project folder

cd semantic-search-system

Install dependencies

pip install -r requirements.txt

---

## Run the Application
## How to Run the Project

Follow the steps below to run the application locally.

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate the virtual environment

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the FastAPI server

```bash
uvicorn api.main:app --reload
```

After running the above command, the server will start and a message will appear in the terminal showing the local server address.

### 5. Open the API documentation

Open the following link in your browser:

http://127.0.0.1:8000/docs

This will open the interactive API documentation where you can test the semantic search endpoints.


---

## API Endpoints

Search Query

POST /search

Cache Statistics

GET /cache/stats

Clear Cache

DELETE /cache

---

## Example Cache Stats Output

{
  "total_entries": 0,
  "hit_count": 0,
  "miss_count": 0,
  "hit_rate": 0
}

---

## Technologies Used

Python  
FastAPI  
Sentence Transformers  
FAISS  
NumPy

---

## Author

AI/ML Engineer Task Submission
