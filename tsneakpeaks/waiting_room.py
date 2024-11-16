"""
The Waiting Room: Data preprocessing and validation
A place where data waits to be transformed
"""

import numpy as np
from typing import Optional, Tuple
import logging
from pathlib import Path

class WaitingRoom:
    """Handles data preprocessing and validation"""
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        self.logger = logger or logging.getLogger(__name__)
        
    def validate_data(self, 
                     image_paths: list,
                     labels: Optional[np.ndarray] = None) -> bool:
        """Validate input data"""
        if not image_paths:
            raise ValueError("No image paths provided")
            
        if labels is not None:
            if len(image_paths) != len(labels):
                raise ValueError(
                    f"Number of images ({len(image_paths)}) does not match "
                    f"number of labels ({len(labels)})"
                )
        
        return True
        
    def preprocess_labels(self, 
                         labels: np.ndarray) -> np.ndarray:
        """Preprocess labels for dimension reduction"""
        # Normalize if needed
        if labels.max() > 1.0 or labels.min() < 0.0:
            self.logger.info("Normalizing labels to [0,1] range")
            labels = (labels - labels.min()) / (labels.max() - labels.min())
            
        return labels
