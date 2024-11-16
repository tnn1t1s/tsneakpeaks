import argparse
from pathlib import Path
import numpy as np
from PIL import Image
import json

def load_palette(palette_file: Path):
    """
    Load the color palette from a `.palette` JSON file.

    Parameters:
    - palette_file (Path): Path to the palette file.

    Returns:
    - List[Tuple[int, int, int]]: List of RGB tuples representing the color palette.
    """
    if not palette_file.is_file():
        raise FileNotFoundError(f"Palette file not found: {palette_file}")
    with open(palette_file, "r") as f:
        palette_data = json.load(f)
    return [tuple(color["color"]) for color in palette_data["palette"]]

def generate_monochromatic_images(output_dir: Path, palette: list, color1_idx: int, color2_idx: int, n_images: int, size: int):
    """
    Generate two sets of monochromatic images, each set with a single color.

    Parameters:
    - output_dir (Path): Directory to save the generated images and labels.
    - palette (list): List of RGB tuples representing the color palette.
    - color1_idx (int): Index of the first color in the palette.
    - color2_idx (int): Index of the second color in the palette.
    - n_images (int): Number of images per color.
    - size (int): Size of each image (in pixels).
    """
    output_dir.mkdir(exist_ok=True)

    # Preallocate labels array
    labels = np.zeros((n_images * 2, 4), dtype=int)  # Store quadrant color indices

    # Retrieve RGB values for the two selected colors
    color1 = tuple(palette[color1_idx])
    color2 = tuple(palette[color2_idx])

    print(f"Selected Colors: {color1} (index {color1_idx}) and {color2} (index {color2_idx})")

    # Generate images for the first color
    for i in range(n_images):
        img = np.full((size, size, 3), color1, dtype=np.uint8)
        labels[i] = [color1_idx] * 4  # All quadrants have the same color
        Image.fromarray(img).save(output_dir / f"image_{i:04d}.png")

    # Generate images for the second color
    for i in range(n_images, n_images * 2):
        img = np.full((size, size, 3), color2, dtype=np.uint8)
        labels[i] = [color2_idx] * 4  # All quadrants have the same color
        Image.fromarray(img).save(output_dir / f"image_{i:04d}.png")

    # Save labels in a `.npy` file
    np.save(output_dir / "labels.npy", labels)

    print(f"Generated {n_images * 2} images with corresponding labels in {output_dir}")

def main():
    parser = argparse.ArgumentParser(description="Generate two monochromatic sets of images.")
    parser.add_argument("--palette", type=str, default=".palette", help="Path to the color palette file (JSON format).")
    parser.add_argument("--output-dir", type=str, default="test_data", help="Directory to save generated images and labels.")
    parser.add_argument("--n-images", type=int, default=50, help="Number of images per color.")
    parser.add_argument("--size", type=int, default=256, help="Size of each image (in pixels).")
    parser.add_argument("--color1", type=int, help="Index of the first color in the palette.")
    parser.add_argument("--color2", type=int, help="Index of the second color in the palette.")

    args = parser.parse_args()

    # Load the palette
    try:
        palette = load_palette(Path(args.palette))
    except FileNotFoundError as e:
        print(e)
        exit(1)

    # Randomly select colors if not specified
    if args.color1 is None or args.color2 is None:
        args.color1, args.color2 = np.random.choice(len(palette), size=2, replace=False)

    # Validate color indices
    if args.color1 < 0 or args.color2 < 0 or args.color1 >= len(palette) or args.color2 >= len(palette):
        raise ValueError(f"Color indices must be between 0 and {len(palette) - 1}.")

    # Generate monochromatic images
    generate_monochromatic_images(
        output_dir=Path(args.output_dir),
        palette=palette,
        color1_idx=args.color1,
        color2_idx=args.color2,
        n_images=args.n_images,
        size=args.size
    )

if __name__ == "__main__":
    main()

