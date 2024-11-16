# TSneakPeaks Methodology

## Overview
TSneakPeaks visualizes high-dimensional image relationships in an interactive 3D space. Like Agent Cooper navigating between the Black and White Lodge, users can explore relationships between images that might not be immediately apparent in regular browsing.

## How It Works

### 1. **Data Representation**
Each image is divided into 4 quadrants, and each quadrant is assigned a single color from a 16-color palette. Instead of representing images with dense vectors, TSneakPeaks uses a **sparse one-hot encoding**:
- Each image is represented by a sparse matrix where:
  - Rows correspond to quadrants.
  - Columns represent one-hot encoded color indices from the palette.
- This sparse representation preserves both the **categorical nature** of colors and the **spatial structure** of the image.

### 2. **Dimension Reduction**
The sparse one-hot representation is reduced to 3 dimensions using the **t-SNE algorithm**:
- t-SNE uses **cosine similarity** to measure relationships between high-dimensional points.
- Local neighborhoods are preserved, meaning similar images are placed closer together in the 3D space.

### 3. **Visualization Elements**
- Each point represents one image in the dataset.
- Color intensity indicates the variety of colors in the image:
  - **Dark points**: Images with fewer unique colors.
  - **Bright points**: Images with more diverse colors.

## Interacting with the Visualization

1. **Navigation**
   - Drag to rotate the view.
   - Scroll to zoom in/out.
   - Right-click drag to pan.

2. **Image Viewing**
   - Click any point to see the full image in the sidebar.
   - Hover over points to see image details.

3. **Interpreting Distance**
   - **Close Points**: Images with similar quadrant color patterns.
   - **Distant Points**: Images with different color distributions.

## Understanding the Results

The visualization creates "neighborhoods" of similar images:
- Images with similar quadrant color combinations are grouped closely.
- Spatial arrangement preserves local relationships (e.g., nearest neighbors are genuinely similar).
- **Global distances** between far-apart points may be less meaningful due to t-SNE's focus on local structure.

## Recent Improvements

1. **Sparse Representation**:
   - Images are now represented as sparse one-hot encoded matrices, making the pipeline more efficient and preserving the categorical nature of colors.

2. **Improved t-SNE Integration**:
   - The t-SNE algorithm now uses **cosine similarity**, which better reflects the nature of the sparse, categorical data.

3. **Cluster Analysis Support**:
   - The pipeline supports generating and visualizing clusters, helping users explore how images group based on shared color patterns.

## Limitations

- t-SNE emphasizes local structure, so large-scale distances may not fully represent relationships.
- The current implementation only considers **color indices**; texture and spatial patterns are not yet included.
- 3D projection is an approximation of the full high-dimensional relationship space.

## Future Possibilities
- Incorporate additional features (e.g., textures, patterns, gradients).
- Experiment with alternative dimensionality reduction techniques (e.g., UMAP, PCA).
- Add configurable t-SNE parameters for real-time experimentation.
- Expand cluster analysis with metrics like silhouette scores or Davies-Bouldin index.

