import argparse
from pathlib import Path
import numpy as np
from PIL import Image
import json
import ast

def load_palette(palette_file: Path):
    if not palette_file.is_file():
        raise FileNotFoundError(f"Palette file not found: {palette_file}")
    with open(palette_file, "r") as f:
        palette_data = json.load(f)
    return [tuple(color["color"]) for color in palette_data["palette"]]

def generate_monochromatic_clusters(output_dir: Path, palette: list, color_indices: list, num_clusters: int, 
                                  num_images: int, size: int):
    output_dir.mkdir(exist_ok=True)
    total_images = num_clusters * num_images
    labels = np.zeros((total_images, 4), dtype=int)

    for cluster_idx in range(num_clusters):
        color_idx = color_indices[cluster_idx]
        color = tuple(palette[color_idx])
        start_idx = cluster_idx * num_images
        end_idx = start_idx + num_images

        print(f"Cluster {cluster_idx}: Using color {color} (index {color_idx})")

        for i in range(start_idx, end_idx):
            img = np.full((size, size, 3), color, dtype=np.uint8)
            labels[i] = [color_idx] * 4
            Image.fromarray(img).save(output_dir / f"image_{i:04d}.png")

    np.save(output_dir / "labels.npy", labels)
    print(f"Generated {total_images} images across {num_clusters} clusters in {output_dir}")

def main():
    parser = argparse.ArgumentParser(description="Generate multiple monochromatic clusters of images.")
    parser.add_argument("--palette", type=str, default="./examples/twinpeaks.palette", help="Path to the color palette file (JSON format).")
    parser.add_argument("--output-dir", type=str, default="test_data", help="Directory to save generated images and labels.")
    parser.add_argument("--num-images", type=int, default=50, help="Number of images per cluster.")
    parser.add_argument("--size", type=int, default=256, help="Size of each image (in pixels).")
    parser.add_argument("--num-clusters", type=int, required=True, help="Number of clusters to generate.")
    parser.add_argument("--color-indices", type=str, help="Array of color indices, e.g. '[1,2,3]'")
    parser.add_argument("--with-replacement", action="store_true", help="Allow random color selection with replacement")

    args = parser.parse_args()

    try:
        palette = load_palette(Path(args.palette))
    except FileNotFoundError as e:
        print(e)
        exit(1)

    if args.color_indices:
        try:
            color_indices = ast.literal_eval(args.color_indices)
            if len(color_indices) != args.num_clusters:
                raise ValueError(f"Number of color indices ({len(color_indices)}) must match num_clusters ({args.num_clusters})")
        except (ValueError, SyntaxError) as e:
            print(f"Error parsing color indices: {e}")
            exit(1)
    else:
        if args.num_clusters > len(palette) and not args.with_replacement:
            raise ValueError(f"Cannot select {args.num_clusters} unique colors from palette of size {len(palette)}")
        color_indices = np.random.choice(len(palette), size=args.num_clusters, replace=args.with_replacement)

    # Validate color indices
    if any(idx < 0 or idx >= len(palette) for idx in color_indices):
        raise ValueError(f"Color indices must be between 0 and {len(palette) - 1}")

    generate_monochromatic_clusters(
        output_dir=Path(args.output_dir),
        palette=palette,
        color_indices=color_indices,
        num_clusters=args.num_clusters,
        num_images=args.num_images,
        size=args.size
    )

if __name__ == "__main__":
    main()
