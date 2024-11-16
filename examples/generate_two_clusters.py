from pathlib import Path
import numpy as np
from PIL import Image

# Twin Peaks-inspired color palette
TP_COLORS = [
    (140, 0, 0),      # Dark Red
    (20, 20, 20),     # Black
    (255, 255, 255),  # White
    (0, 50, 0),       # Dark Green
    (101, 67, 33),    # Log Brown
    (200, 155, 100),  # Coffee Cream
    (50, 0, 0),       # Dark Maroon
    (255, 215, 0),    # Gold
    (0, 0, 50),       # Night Blue
    (150, 75, 0),     # Owl Brown
    (255, 182, 193),  # Pink
    (128, 0, 0),      # Blood Red
    (218, 165, 32),   # Diner Gold
    (25, 25, 112),    # FBI Blue
    (139, 69, 19),    # Douglas Fir
    (112, 128, 144)   # Fog Gray
]

def generate_simple_clusters(output_dir: Path, color1_idx: int, color2_idx: int, n_images: int = 500, size: int = 256):
    """
    Generate two simple clusters of images with a single color for all quadrants.

    Parameters:
    - output_dir (Path): Directory to save the generated images.
    - color1_idx (int): Index of the first color in the palette.
    - color2_idx (int): Index of the second color in the palette.
    - n_images (int): Number of images per cluster.
    - size (int): Size of each image (in pixels).

    Each cluster contains `n_images` images, where all quadrants of the images 
    have the same color. Labels are stored in a `.npy` file for consistency.
    """
    # Create the output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)

    # Preallocate labels array
    labels = np.zeros((n_images * 2, 4), dtype=int)  # Store quadrant color indices

    # Retrieve RGB values for the two selected colors
    color1 = TP_COLORS[color1_idx]
    color2 = TP_COLORS[color2_idx]

    # Log selected colors for clarity
    print(f"Selected Colors: {color1} (index {color1_idx}) and {color2} (index {color2_idx})")

    # Generate first cluster (Color 1)
    for i in range(n_images):
        img = np.full((size, size, 3), color1, dtype=np.uint8)
        labels[i] = [color1_idx] * 4  # All quadrants have the same color
        Image.fromarray(img).save(output_dir / f"image_{i:04d}.png")

    # Generate second cluster (Color 2)
    for i in range(n_images, n_images * 2):
        img = np.full((size, size, 3), color2, dtype=np.uint8)
        labels[i] = [color2_idx] * 4  # All quadrants have the same color
        Image.fromarray(img).save(output_dir / f"image_{i:04d}.png")

    # Save labels in a `.npy` file
    np.save(output_dir / "labels.npy", labels)

    print(f"Generated {n_images * 2} images with corresponding labels in {output_dir}")

if __name__ == "__main__":
    # Output directory for consistency
    output_dir = Path("test_data")

    # Randomly select two distinct colors from the palette
    color_idx_1, color_idx_2 = np.random.choice(len(TP_COLORS), size=2, replace=False)

    # Generate clusters with the selected random colors
    generate_simple_clusters(output_dir, color1_idx=color_idx_1, color2_idx=color_idx_2, n_images=500)

