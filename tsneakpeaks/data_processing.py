# File: src/data_processing.py

from scipy.sparse import csr_matrix
import numpy as np

def convert_to_sparse_one_hot(image_data, num_quadrants, num_colors):
    """
    Converts image data into a sparse one-hot encoded representation.
    
    Parameters:
    - image_data (list of int): A list where each entry is a color index for a quadrant.
    - num_quadrants (int): Number of quadrants in the image.
    - num_colors (int): Total number of colors in the palette.
    
    Returns:
    - csr_matrix: Sparse matrix with shape (num_quadrants, num_colors).
    """
    # Validate input dimensions
    if len(image_data) != num_quadrants:
        raise ValueError("Length of image_data must match num_quadrants.")

    # Create rows, columns, and data for the sparse matrix
    rows = np.arange(num_quadrants)  # Row indices correspond to quadrants
    cols = image_data                # Column indices correspond to color indices
    data = np.ones(num_quadrants)    # Each quadrant has a single active color
    
    # Create the sparse matrix
    sparse_matrix = csr_matrix((data, (rows, cols)), shape=(num_quadrants, num_colors))
    
    return sparse_matrix

