import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class SemanticCache:

    def __init__(self, threshold=0.85):

        self.cache = []

        self.threshold = threshold

        self.hit_count = 0
        self.miss_count = 0

    def lookup(self, query_embedding):

        for entry in self.cache:

            sim = cosine_similarity(
                query_embedding.reshape(1,-1),
                entry["embedding"].reshape(1,-1)
            )[0][0]

            if sim > self.threshold:

                self.hit_count += 1

                return True, entry, sim

        self.miss_count += 1

        return False, None, None

    def add(self, query, embedding, result, cluster):

        self.cache.append({
            "query": query,
            "embedding": embedding,
            "result": result,
            "cluster": cluster
        })

    def stats(self):

        total = len(self.cache)

        hits = self.hit_count
        misses = self.miss_count

        hit_rate = hits / (hits + misses) if hits+misses>0 else 0

        return {
            "total_entries": total,
            "hit_count": hits,
            "miss_count": misses,
            "hit_rate": hit_rate
        }

    def clear(self):

        self.cache = []

        self.hit_count = 0
        self.miss_count = 0