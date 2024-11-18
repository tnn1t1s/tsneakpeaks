import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Load the feature matrix
features = np.load("test_data/labels.npy")

# Perform PCA to reduce to 2D
pca = PCA(n_components=2)
reduced_features = pca.fit_transform(features)

# Simulated ground truth labels
num_clusters = 4 
images_per_cluster = 25
labels = np.repeat(range(num_clusters),
                   images_per_cluster)  

# Plot the PCA results
plt.figure(figsize=(8, 6))
scatter = plt.scatter(reduced_features[:, 0], reduced_features[:, 1], c=labels, cmap="tab10")
plt.colorbar(scatter, label="Cluster")
plt.title("PCA Projection of Input Features")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(True)
plt.show()

