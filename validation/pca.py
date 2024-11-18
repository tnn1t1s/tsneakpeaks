import argparse
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def visualize_pca(features_file, num_clusters, images_per_cluster, output_file=None, figsize=(8, 6)):
    features = np.load(features_file)
    pca = PCA(n_components=2)
    reduced_features = pca.fit_transform(features)
    
    labels = np.repeat(range(num_clusters), images_per_cluster)
    
    plt.figure(figsize=figsize)
    scatter = plt.scatter(reduced_features[:, 0], reduced_features[:, 1], c=labels, cmap="tab10")
    plt.colorbar(scatter, label="Cluster")
    plt.title("PCA Projection of Input Features")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.grid(True)
    
    if output_file:
        plt.savefig(output_file)
    else:
        plt.show()

def main():
    parser = argparse.ArgumentParser(description="Visualize PCA of feature matrix")
    parser.add_argument("--features", default="test_data/labels.npy", help="Path to features .npy file")
    parser.add_argument("--num-clusters", type=int, default=4, help="Number of clusters")
    parser.add_argument("--images-per-cluster", type=int, default=25, help="Images per cluster")
    parser.add_argument("--output", help="Save plot to file instead of displaying")
    parser.add_argument("--figsize", type=float, nargs=2, default=[8, 6], help="Figure size (width height)")
    
    args = parser.parse_args()
    
    visualize_pca(
        args.features,
        args.num_clusters,
        args.images_per_cluster,
        args.output,
        tuple(args.figsize)
    )

if __name__ == "__main__":
    main()
