Semantic Search System
Overview

The Semantic Search System is an AI-powered search application that retrieves documents based on semantic meaning rather than exact keyword matching.

Traditional search engines rely on keyword matching, which may miss relevant results when different wording is used. This system solves that problem by using sentence embeddings and vector similarity search to find contextually relevant results.

The project integrates sentence-transformer embeddings, FAISS vector indexing, semantic caching, and clustering techniques to deliver fast and intelligent search results.

Features
Semantic Search

Uses Sentence Transformers to convert text into vector embeddings so queries can be matched based on meaning.

Fast Similarity Search

Uses FAISS (Facebook AI Similarity Search) for efficient nearest-neighbor search in high-dimensional vector space.

Semantic Cache

Implements a cache that stores previous query results to reduce computation and improve response time.

Query Clustering

Groups similar queries together using clustering techniques to improve search efficiency.

Cache Analytics

Tracks cache statistics including:

Total entries

Cache hits

Cache misses

Hit rate

REST API

A lightweight API built using FastAPI for interacting with the semantic search engine.

System Architecture

The system works in the following steps:

Input query is received via API

Query is converted into sentence embeddings

FAISS performs vector similarity search

Relevant documents are retrieved

Results may be stored in semantic cache

Response is returned to the user

Project Structure
semantic_search_system/

api/
   main.py                # FastAPI application and endpoints

cache/
   semantic_cache.py      # Semantic caching logic

clustering/
   query_clustering.py    # Query clustering implementation

embeddings/
   embedding_model.py     # Sentence embedding generation

vector_store/
   faiss_index.py         # FAISS vector index and similarity search

data_loader.py            # Dataset loading and preprocessing

requirements.txt          # Project dependencies
Technologies Used

Python

FastAPI

Sentence Transformers

FAISS

NumPy

Scikit-learn

Installation
1 Clone the Repository
git clone https://github.com/your-username/semantic-search-system.git
2 Navigate to Project Directory
cd semantic-search-system
3 Create Virtual Environment
python -m venv venv
4 Activate Virtual Environment
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
5 Install Dependencies
pip install -r requirements.txt
Running the Application

Start the FastAPI server:

uvicorn api.main:app --reload

Once the server starts, it will run on:

http://127.0.0.1:8000
API Documentation

FastAPI automatically generates interactive API documentation.

Open the following link in your browser:

http://127.0.0.1:8000/docs

This interface allows you to test the API endpoints directly from the browser.

API Endpoints
Search Query

POST /search

Search for semantically similar documents.

Example request:

{
  "query": "space exploration technology"
}
Cache Statistics

GET /cache/stats

Returns cache performance metrics.

Example response:

{
  "total_entries": 0,
  "hit_count": 0,
  "miss_count": 0,
  "hit_rate": 0
}
Clear Cache

DELETE /cache

Removes all cached entries.

Future Improvements

Add hybrid search (keyword + semantic search)

Implement query suggestion system

Improve clustering with advanced unsupervised algorithms

Deploy the system using Docker or cloud services

Author

Bhuvaneswari Musanalli
AI/ML Engineer Task Submission
