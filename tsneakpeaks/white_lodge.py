# tsneakpeaks/white_lodge.py
"""
The White Lodge: Dimension reduction and transformation
Like the White Lodge, this is where things become more comprehensible
"""

import numpy as np
from sklearn.manifold import TSNE
from scipy.sparse import vstack
from typing import Optional, List
import logging
from .data_processing import convert_to_sparse_one_hot


class WhiteLodge:
    """Handles dimension reduction to 3D space"""
    
    def __init__(self, 
                 perplexity: float = 30.0,
                 n_iter: int = 1000,
                 random_state: int = 42,
                 logger: Optional[logging.Logger] = None):
        self.perplexity = perplexity
        self.n_iter = n_iter
        self.random_state = random_state
        self.logger = logger or logging.getLogger(__name__)
        self.tsne = None

    def prepare_data(self, quadrant_labels: np.ndarray, num_quadrants: int, num_colors: int) -> np.ndarray:
        """
        Convert quadrant labels (color indices) into a dense dataset for t-SNE.
        
        Parameters:
        - quadrant_labels (np.ndarray): Array of shape (n_images, num_quadrants),
          where each entry contains the color index for a quadrant.
        - num_quadrants (int): Number of quadrants in each image.
        - num_colors (int): Total number of colors in the palette.

        Returns:
        - np.ndarray: Dense dataset ready for t-SNE.
        """
        self.logger.info("Converting quadrant labels to sparse one-hot encoding...")

        # Convert each image to a sparse matrix
        sparse_matrices = [
            convert_to_sparse_one_hot(image_data, num_quadrants, num_colors)
            for image_data in quadrant_labels
        ]
        
        # Stack all sparse matrices into one
        sparse_dataset = vstack(sparse_matrices)
        self.logger.info(f"Generated sparse dataset with shape {sparse_dataset.shape}.")
        
        # Convert to dense format for t-SNE
        dense_dataset = sparse_dataset.toarray()
        self.logger.info("Converted sparse dataset to dense format.")
        
        return dense_dataset
    
    def project(self, high_dim_data: np.ndarray) -> np.ndarray:
        """Project high-dimensional data into 3D space"""
        self.logger.info("Initiating projection through the White Lodge...")
        
        self.tsne = TSNE(
            n_components=3,
            perplexity=self.perplexity,
            n_iter=self.n_iter,
            random_state=self.random_state,
            metric="cosine"
        )
        
        coords_3d = self.tsne.fit_transform(high_dim_data)
        self.logger.info("Projection complete")
        
        return coords_3d
    
    def project_images(self, quadrant_labels: np.ndarray, num_quadrants: int, num_colors: int) -> np.ndarray:
        """
        Full pipeline: Convert quadrant labels to one-hot representation, then project to 3D space.
        
        Parameters:
        - quadrant_labels (np.ndarray): Array of shape (n_images, num_quadrants).
        - num_quadrants (int): Number of quadrants in each image.
        - num_colors (int): Total number of colors in the palette.

        Returns:
        - np.ndarray: 3D coordinates for each image.
        """
        self.logger.info("Starting full pipeline for image projection...")
        dense_dataset = self.prepare_data(quadrant_labels, num_quadrants, num_colors)
        return self.project(dense_dataset)
    
    def visualize_clusters(self, coords_3d: np.ndarray, quadrant_labels: np.ndarray, output_path: Path):
        """
        Visualize the clusters by mapping the 3D coordinates back to their quadrant labels.

        Parameters:
        - coords_3d (np.ndarray): 3D t-SNE coordinates.
        - quadrant_labels (np.ndarray): Original quadrant labels for each image.
        - output_path (Path): Path to save the visualization.
        """
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D

        self.logger.info("Visualizing clusters...")
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Scatter plot with quadrant labels as colors
        unique_labels = np.unique(quadrant_labels)
        for label in unique_labels:
            indices = np.where(quadrant_labels[:, 0] == label)  # Example: color quadrant 1
            ax.scatter(coords_3d[indices, 0], coords_3d[indices, 1], coords_3d[indices, 2], label=f"Color {label}")
        
        ax.set_title("3D Cluster Visualization")
        ax.legend()
        plt.savefig(output_path)
        self.logger.info(f"Visualization saved to {output_path}")

