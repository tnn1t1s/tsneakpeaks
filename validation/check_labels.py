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
    try:
        labels = np.load(label_file)
        print("Labels loaded successfully.")
    except FileNotFoundError:
        print(f"Error: File not found - {label_file}")
        return
    
    # Convert numpy arrays to regular Python lists for better printing
    label_tuples = [tuple(map(int, label)) for label in labels]
    
    for label_tuple in label_tuples:
        print(label_tuple)
    
    label_counts = Counter(label_tuples)
    
    print("\nUnique Label Groups and Counts:")
    for label, count in label_counts.items():
        print(f"Label: {label}, Count: {count}")

if __name__ == "__main__":
    label_file = "test_data/labels.npy"
    load_and_analyze_labels(label_file)
