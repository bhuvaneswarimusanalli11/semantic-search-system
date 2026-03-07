import faiss
import numpy as np

class VectorStore:

    def __init__(self, dimension):

        self.index = faiss.IndexFlatL2(dimension)

        self.documents = []

    def add(self, embeddings, docs):

        self.index.add(np.array(embeddings))

        self.documents.extend(docs)

    def search(self, query_embedding, k=5):

        D, I = self.index.search(query_embedding.reshape(1, -1), k)

        results = [self.documents[i] for i in I[0]]

        return results