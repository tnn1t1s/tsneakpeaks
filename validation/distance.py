from sklearn.metrics import pairwise_distances
from sklearn.manifold import TSNE
import numpy as np

# Load labels
labels = np.load("test_data/labels.npy")

# Compute pairwise distances (Euclidean)
distance_matrix = pairwise_distances(labels, metric="euclidean")

# Run t-SNE with precomputed distances
tsne = TSNE(n_components=3, metric="precomputed", random_state=42, init="random")
coords_3d = tsne.fit_transform(distance_matrix)

print(coords_3d)

