# TSneakPeaks Methodology

## Overview
TSneakPeaks visualizes high-dimensional image relationships in an interactive 3D space. Like Agent Cooper navigating between the Black and White Lodge, users can explore relationships between images that might not be immediately apparent in regular browsing.

## How It Works

1. **Dimension Reduction**
   - Each image is represented by a 16-dimensional vector (based on color presence)
   - t-SNE algorithm reduces these 16 dimensions to 3 visible dimensions
   - Similar images are positioned closer together in this 3D space

2. **Visualization Elements**
   - Each point represents one image
   - Color intensity indicates number of unique colors in the image
   - Dark points = fewer colors
   - Bright points = more colors

## Interacting with the Visualization

1. **Navigation**
   - Drag to rotate the view
   - Scroll to zoom in/out
   - Right-click drag to pan

2. **Image Viewing**
   - Click any point to see the full image in the sidebar
   - Hover over points to see image details

3. **Interpreting Distance**
   - Points close together = images with similar color patterns
   - Points far apart = images with different color patterns

## Understanding the Results

The visualization creates "neighborhoods" of similar images. When you find an interesting image, look at its neighbors in 3D space - they likely share similar color combinations or patterns. The spatial arrangement preserves local relationships, meaning nearby points are genuinely similar, but distances between far-apart points may be less meaningful.

## Limitations

- t-SNE focuses on preserving local structure, so very distant relationships might not be meaningful
- The current implementation only considers color presence, not spatial arrangements or patterns
- 3D projection is an approximation of the full 16-dimensional relationship space

## Future Possibilities
- Additional feature vectors (texture, patterns, etc.)
- Different dimension reduction techniques (UMAP, PCA)
- Clustering analysis
