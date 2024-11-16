import numpy as np
labels = np.load("test_data/labels.npy")
print(np.unique(labels, axis=0))

