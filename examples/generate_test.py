# examples/generate_test.py
from pathlib import Path
import numpy as np
from PIL import Image

print("starting")
# Create test directory
output_dir = Path("test_data")
output_dir.mkdir(exist_ok=True)

# Generate 100 test images (2x2 color grid)
n_images = 100
size = 256
n_colors = 16
n_quadrants = 4

# Create color palette
colors = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (128, 0, 0),    # Maroon
    (0, 128, 0),    # Dark Green
    (0, 0, 128),    # Navy
    (128, 128, 0),  # Olive
    (128, 0, 128),  # Purple
    (0, 128, 128),  # Teal
    (255, 128, 0),  # Orange
    (255, 192, 203),# Pink
    (128, 128, 128),# Gray
    (255, 255, 255) # White
]

# Generate images and save their quadrant-color indices
labels = np.zeros((n_images, n_quadrants), dtype=int)  # Store color indices per quadrant
half = size // 2

for i in range(n_images):
    # Create new image
    print(f"Creating image {i + 1}/{n_images}")
    img = np.zeros((size, size, 3), dtype=np.uint8)
    
    # Select random colors for each quadrant
    selected_colors = np.random.choice(len(colors), n_quadrants, replace=False)  # Avoid duplicate colors
    
    # Fill quadrants
    img[0:half, 0:half] = colors[selected_colors[0]]  # Top-left
    img[0:half, half:] = colors[selected_colors[1]]   # Top-right
    img[half:, 0:half] = colors[selected_colors[2]]   # Bottom-left
    img[half:, half:] = colors[selected_colors[3]]    # Bottom-right
    
    # Save image
    Image.fromarray(img).save(output_dir / f"image_{i:04d}.png")
    
    # Update labels with the color indices for each quadrant
    labels[i] = selected_colors

# Save labels as a separate file
np.save(output_dir / "labels.npy", labels)

print(f"Generated {n_images} images with corresponding labels in {output_dir}")

