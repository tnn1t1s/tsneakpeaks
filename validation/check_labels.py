import numpy as np
from collections import Counter

def load_and_analyze_labels(label_file):
    """
    Load labels from a .npy file, group them, and count occurrences.

    Parameters:
    - label_file (str): Path to the .npy file containing labels.

    Prints:
    - Unique label groups and their counts.
    """
    # Load labels
    try:
        labels = np.load(label_file)
        print("Labels loaded successfully.")
    except FileNotFoundError:
        print(f"Error: File not found - {label_file}")
        return

    # Convert labels to tuples for grouping
    label_tuples = [tuple(label) for label in labels]
    for label_tuple in label_tuples:
        print(label_tuple)

    # Count occurrences of each unique label group
    label_counts = Counter(label_tuples)

    # Output results
    print("\nUnique Label Groups and Counts:")
    for label, count in label_counts.items():
        print(f"Label: {label}, Count: {count}")

if __name__ == "__main__":
    # Path to the labels file
    label_file = "test_data/labels.npy"
    
    # Analyze labels
    load_and_analyze_labels(label_file)

