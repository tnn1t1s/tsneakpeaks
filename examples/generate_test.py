# You can copy this into generate_test.py
from pathlib import Path
from tsneakpeaks.black_lodge import BlackLodge
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

# Generate images and labels
labels = np.zeros((n_images, n_colors))
half = size // 2

for i in range(n_images):
    # Create new image
    print(f"# Create new image {i}")
    img = np.zeros((size, size, 3), dtype=np.uint8)
    
    # Select random colors for each quadrant
    selected_colors = np.random.choice(len(colors), 4)
    
    # Fill quadrants
    img[0:half, 0:half] = colors[selected_colors[0]]
    img[0:half, half:] = colors[selected_colors[1]]
    img[half:, 0:half] = colors[selected_colors[2]]
    img[half:, half:] = colors[selected_colors[3]]
    
    # Save image
    Image.fromarray(img).save(output_dir / f"image_{i:04d}.png")
    
    # Update labels
    labels[i][selected_colors] = 1

# Save labels
np.save(output_dir / "labels.npy", labels)

print(f"Generated {n_images} images in {output_dir}")
