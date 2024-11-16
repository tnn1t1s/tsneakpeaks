# tsneakpeaks/black_lodge.py
"""
The Black Lodge: High-dimensional data handling
Like the mysterious Black Lodge, this is where our raw high-dimensional data resides
"""

import numpy as np
from pathlib import Path
from typing import List, Tuple, Optional
import logging
from PIL import Image

class BlackLodge:
    """Handles loading and processing of high-dimensional data"""
    
    def __init__(self, data_dir: Path, logger: Optional[logging.Logger] = None):
        self.data_dir = Path(data_dir)
        self.logger = logger or logging.getLogger(__name__)
        self.labels = None
        self.image_paths = []
        
    def enter(self) -> Tuple[List[str], np.ndarray]:
        """Enter the Black Lodge to retrieve our data"""
        self.logger.info("Entering the Black Lodge...")
        
        # Load labels if they exist
        labels_path = self.data_dir / 'labels.npy'
        if labels_path.exists():
            self.labels = np.load(labels_path)
            self.logger.debug(f"Labels shape: {self.labels.shape}")
        
        # Get image paths
        self.image_paths = sorted(
            str(p) for p in self.data_dir.glob('image_*.png')
        )
        
        if len(self.image_paths) == 0:
            raise FileNotFoundError(f"No images found in {self.data_dir}")
            
        self.logger.info(f"Found {len(self.image_paths)} images")
        
        return self.image_paths, self.labels
        
    def generate_labels(self, method: str = 'color_grid') -> np.ndarray:
        """Generate labels from images if not provided"""
        self.logger.info(f"Generating labels using method: {method}")
        
        if method == 'color_grid':
            labels = []
            for path in self.image_paths:
                img = Image.open(path)
                # Convert image to numpy array and analyze
                arr = np.array(img)
                # Extract color features (simplified for example)
                features = np.concatenate([
                    arr.mean(axis=(0,1)),  # Average RGB
                    arr.std(axis=(0,1)),   # Color variation
                ])
                labels.append(features)
            
            self.labels = np.array(labels)
            return self.labels
        else:
            raise ValueError(f"Unknown label generation method: {method}")

