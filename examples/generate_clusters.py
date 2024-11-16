import numpy as np
from PIL import Image
import os
from pathlib import Path

# Twin Peaks inspired color palette
TP_COLORS = [
    (140, 0, 0),      # Dark Red (Red Room curtains)
    (20, 20, 20),     # Black Lodge black
    (255, 255, 255),  # White Lodge white
    (0, 50, 0),       # Dark forest green
    (101, 67, 33),    # Log brown
    (200, 155, 100),  # Coffee cream
    (50, 0, 0),       # Black Lodge floor
    (255, 215, 0),    # Laura's hair
    (0, 0, 50),       # Night sky blue
    (150, 75, 0),     # Owl brown
    (255, 182, 193),  # Audrey's lipstick
    (128, 0, 0),      # Blood red
    (218, 165, 32),   # Double R Diner gold
    (25, 25, 112),    # FBI blue
    (139, 69, 19),    # Douglas Fir
    (112, 128, 144)   # Pacific Northwest fog
]

def generate_cluster_params(n_clusters=5, n_dims=16):
    """Generate cluster centers and spreads in color space"""
    centers = np.random.rand(n_clusters, n_dims) * 0.6 + 0.2  # Keep away from edges
    spreads = np.random.rand(n_clusters, n_dims) * 0.1 + 0.05  # Relatively tight clusters
    return centers, spreads

def generate_color_vector(centers, spreads, n_colors=4):
    """Generate colors from one of the clusters"""
    cluster = np.random.randint(len(centers))
    # Sample from normal distribution around cluster center
    probs = np.random.normal(centers[cluster], spreads[cluster])
    probs = np.clip(probs, 0, 1)  # Ensure valid probabilities
    
    # Select colors based on probabilities
    color_indices = np.random.choice(
        len(TP_COLORS), 
        size=n_colors, 
        p=probs/probs.sum()
    )
    return color_indices, probs

def main():
    output_dir = Path("test_data")
    output_dir.mkdir(exist_ok=True)
    
    # Parameters
    n_images = 1000
    image_size = 256
    half = image_size // 2
    
    # Generate cluster parameters
    centers, spreads = generate_cluster_params(n_clusters=5, n_dims=len(TP_COLORS))
    
    # Store labels (probability vectors)
    all_labels = np.zeros((n_images, len(TP_COLORS)))
    
    # Generate images
    for i in range(n_images):
        # Create new image
        img = np.zeros((image_size, image_size, 3), dtype=np.uint8)
        
        # Get colors for this image
        color_indices, probs = generate_color_vector(centers, spreads)
        all_labels[i] = probs
        
        # Fill quadrants
        quadrants = [
            (0, 0, half, half),
            (0, half, half, image_size),
            (half, 0, image_size, half),
            (half, half, image_size, image_size)
        ]
        
        for (y1, x1, y2, x2), color_idx in zip(quadrants, color_indices):
            color = TP_COLORS[color_idx]
            img[y1:y2, x1:x2] = color
        
        # Save image
        Image.fromarray(img).save(output_dir / f"image_{i:04d}.png")
    
    # Save labels
    np.save(output_dir / "labels.npy", all_labels)
    print(f"Generated {n_images} images in {output_dir}")

if __name__ == "__main__":
    main()
