import skfuzzy as fuzz
import numpy as np

class FuzzyCluster:

    def __init__(self, n_clusters=10):

        self.n_clusters = n_clusters

    def fit(self, embeddings):

        cntr, u, _, _, _, _, _ = fuzz.cluster.cmeans(
            embeddings.T,
            c=self.n_clusters,
            m=2,
            error=0.005,
            maxiter=1000
        )

        self.centers = cntr
        self.membership = u

        return u

    def get_dominant_cluster(self, embedding):

        distances = np.linalg.norm(self.centers - embedding, axis=1)

        return distances.argmin()