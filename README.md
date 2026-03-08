# Semantic Search System

## Overview
The Semantic Search System is an AI-powered search application that retrieves documents based on semantic meaning rather than exact keyword matching.

Traditional search systems rely on keyword matching, which may miss relevant results when different wording is used. This system solves that problem by using sentence embeddings and vector similarity search to find contextually relevant results.

The project integrates Sentence Transformers, FAISS vector indexing, semantic caching, and clustering techniques to deliver fast and intelligent search results.

---

## Features

- Semantic search using sentence embeddings
- Fast similarity search using FAISS
- Intelligent semantic caching
- Query clustering
- Cache statistics tracking
- REST API built using FastAPI

---

## System Workflow

1. User sends a search query through the API.
2. The query is converted into a vector embedding.
3. FAISS performs similarity search on stored document embeddings.
4. The most relevant documents are retrieved.
5. Results may be stored in the semantic cache.
6. The response is returned to the user.

---

## Project Structure

```
semantic_search_system/

api/
    main.py                # FastAPI endpoints

cache/
    semantic_cache.py      # Semantic caching logic

clustering/
    query_clustering.py    # Query clustering

embeddings/
    embedding_model.py     # Text embedding generation

vector_store/
    faiss_index.py         # FAISS vector search

data_loader.py             # Dataset loading

requirements.txt           # Project dependencies
```

---

## Technologies Used

- Python
- FastAPI
- Sentence Transformers
- FAISS
- NumPy
- Scikit-learn

---

## Installation

### 1 Clone the Repository

```
git clone https://github.com/your-username/semantic-search-system.git
```

### 2 Navigate to Project Directory

```
cd semantic-search-system
```

### 3 Create Virtual Environment

```
python -m venv venv
```

### 4 Activate Virtual Environment

Windows

```
venv\Scripts\activate
```

Linux / Mac

```
source venv/bin/activate
```

### 5 Install Dependencies

```
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI server:

```
uvicorn api.main:app --reload
```

Once the server starts, it will run locally at:

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

Open the following link in your browser:

```
http://127.0.0.1:8000/docs
```

This interface allows you to test the API endpoints directly from the browser.

---

## API Endpoints

### Search Query

POST `/search`

Example request:

```
{
  "query": "space exploration technology"
}
```
<img width="1766" height="879" alt="image" src="https://github.com/user-attachments/assets/e7b62f77-d888-4f60-8ef5-da0d2957f3da" />

---

### Cache Statistics

GET `/cache/stats`

Example response:

```
{
  "total_entries": 0,
  "hit_count": 0,
  "miss_count": 0,
  "hit_rate": 0
}
```

---

### Clear Cache

DELETE `/cache`

Removes all cached entries.

---

## Future Improvements

- Hybrid search (keyword + semantic search)
- Query suggestion system
- Improved clustering techniques
- Deployment using Docker
- Web interface for search visualization

---

## Author

Bhuvaneswari Musanalli  
AI/ML Engineer Task Submission
