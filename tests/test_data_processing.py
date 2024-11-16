# File: tests/test_data_processing.py

from tsneakpeaks.data_processing import convert_to_sparse_one_hot

def test_sparse_one_hot_conversion():
    """
    Test the convert_to_sparse_one_hot function with a simple dataset.
    """
    # Example input: 4 quadrants, 16 colors
    image_data = [2, 5, 0, 8]  # Colors for each quadrant
    num_quadrants = 4
    num_colors = 16

    # Run conversion
    sparse_matrix = convert_to_sparse_one_hot(image_data, num_quadrants, num_colors)
    
    # Expected output (manual verification):
    # Quadrant 1 -> Color 2
    # Quadrant 2 -> Color 5
    # Quadrant 3 -> Color 0
    # Quadrant 4 -> Color 8
    expected_nonzero = [
        (0, 2),  # Quadrant 1, Color 2
        (1, 5),  # Quadrant 2, Color 5
        (2, 0),  # Quadrant 3, Color 0
        (3, 8),  # Quadrant 4, Color 8
    ]

    # Assert the sparse matrix has the correct nonzero indices
    assert (sparse_matrix.nonzero()[0] == [r for r, c in expected_nonzero]).all()
    assert (sparse_matrix.nonzero()[1] == [c for r, c in expected_nonzero]).all()

    print("Test passed: Sparse one-hot encoding works correctly.")

