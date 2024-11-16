# TSneakPeaks

TSneakPeaks is a Python-based tool for visualizing high-dimensional image data using **t-SNE** (t-distributed Stochastic Neighbor Embedding). It allows users to explore patterns and relationships in image collections by projecting features into an interactive 3D space.

<img width="1246" alt="Screenshot 2024-11-16 at 12 37 08 PM" src="https://github.com/user-attachments/assets/6a3083cc-ab6c-4463-8113-f3647aac5e70">



## Overview

High-dimensional datasets often contain hidden structures that are difficult to interpret. TSneakPeaks simplifies this by reducing dimensions and providing an intuitive visualization of relationships between images based on their features. This tool is particularly suited for exploring image collections with categorical or spatial data.

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/tsneakpeaks.git
cd tsneakpeaks

# Create and activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package
pip install -e .
```

### Generate Test Data

```bash
# Create test data with random quadrant colors
python examples/generate_test.py
```

### Run Visualization

```bash
# Visualize the data in 3D
python examples/visualize.py
```

## Features

- **Interactive 3D Visualization**: Navigate high-dimensional image spaces using t-SNE.
- **Customizable Feature Representation**: Supports sparse one-hot encoding to preserve categorical and spatial relationships.
- **Cluster Exploration**: Analyze clusters formed by similar image features.
- **Efficient Data Handling**: Designed to handle large datasets with sparse data efficiently.
- **Flexible Configuration**: Easily tweak t-SNE parameters (e.g., perplexity, iterations).

## Requirements

- Python 3.8+
- NumPy
- scikit-learn
- Plotly
- Pillow

## Project Structure

```
TSneakPeaks/
├── tsneakpeaks/
│   ├── data_processing.py   # Utility functions for data preparation
│   ├── white_lodge.py       # Dimension reduction pipeline
│   └── ...other modules...
├── examples/
│   ├── generate_test.py     # Script to generate test data
│   ├── generate_clusters.py # Script to create clustered test data
│   └── visualize.py         # Script to run visualization
├── tests/                   # Unit tests
└── README.md
```

## Usage Examples

### Basic Usage

```python
from tsneakpeaks.white_lodge import WhiteLodge
import numpy as np

# Load quadrant labels (e.g., from test_data)
quadrant_labels = np.load("test_data/quadrant_labels.npy")
num_quadrants = 4
num_colors = 16

# Initialize WhiteLodge for dimensionality reduction
wl = WhiteLodge(perplexity=30, n_iter=1000)

# Project to 3D
coords_3d = wl.project_images(quadrant_labels, num_quadrants, num_colors)

# coords_3d contains the 3D t-SNE projection
print(coords_3d)
```

### Cluster Visualization

```python
import numpy as np
from tsneakpeaks.white_lodge import WhiteLodge
from pathlib import Path

# Load quadrant labels
quadrant_labels = np.load("test_data/quadrant_labels.npy")

# Initialize WhiteLodge
wl = WhiteLodge()

# Perform dimensionality reduction
coords_3d = wl.project_images(quadrant_labels, num_quadrants=4, num_colors=16)

# Visualize clusters
wl.visualize_clusters(coords_3d, quadrant_labels, output_path=Path("clusters.png"))
```

## Data Format

- **Images**: PNG format, divided into 4 quadrants, each assigned a unique color from a palette.
- **Labels**: A `.npy` file (`quadrant_labels.npy`) containing the color indices for each quadrant of all images.

## Limitations

- t-SNE emphasizes local relationships, so global distances between far-apart points may not always be meaningful.
- Currently supports only color-based features; future versions may incorporate texture and pattern analysis.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.
