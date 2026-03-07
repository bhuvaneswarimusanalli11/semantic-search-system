from fastapi import FastAPI
from data_loader import load_dataset
from embeddings.embedder import Embedder
from vector_store.faiss_store import VectorStore
from clustering.fuzzy_cluster import FuzzyCluster
from cache.semantic_cache import SemanticCache

import numpy as np
#app = FastAPI(title="Trademarkia Semantic Search API")

app = FastAPI()

# Load dataset
docs = load_dataset()

# Create embedder
embedder = Embedder()

# Generate embeddings
doc_embeddings = embedder.embed_documents(docs)

# Vector database
vector_db = VectorStore(doc_embeddings.shape[1])
vector_db.add(doc_embeddings, docs)

# Clustering
cluster_model = FuzzyCluster(n_clusters=10)
cluster_model.fit(doc_embeddings)

# Cache
cache = SemanticCache()


@app.post("/query")
def query_api(body: dict):

    query = body["query"]

    # Generate query embedding
    query_embedding = embedder.embed_query(query)

    # Check cache
    hit, entry, sim = cache.lookup(query_embedding)

    if hit:
        return {
            "query": str(query),
            "cache_hit": True,
            "matched_query": str(entry["query"]),
            "similarity_score": float(sim),
            "result": str(entry["result"]),
            "dominant_cluster": int(entry["cluster"])
        }

    # Vector search
    results = vector_db.search(query_embedding)

    # Get dominant cluster
    dominant_cluster = cluster_model.get_dominant_cluster(query_embedding)

    result = str(results[0])

    # Add to cache
    cache.add(query, query_embedding, result, int(dominant_cluster))

    return {
        "query": str(query),
        "cache_hit": False,
        "matched_query": None,
        "similarity_score": None,
        "result": result,
        "dominant_cluster": int(dominant_cluster)
    }


@app.get("/cache/stats")
def cache_stats():
    return cache.stats()


@app.delete("/cache")
def clear_cache():

    cache.clear()

    return {"message": "Cache cleared"}