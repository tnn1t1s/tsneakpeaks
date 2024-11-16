# tsneakpeaks/white_lodge.py
"""
The White Lodge: Dimension reduction and transformation
Like the White Lodge, this is where things become more comprehensible
"""

import numpy as np
from sklearn.manifold import TSNE
from typing import Optional
import logging

class WhiteLodge:
    """Handles dimension reduction to 3D space"""
    
    def __init__(self, 
                 perplexity: float = 30.0,
                 n_iter: int = 1000,
                 random_state: int = 42,
                 logger: Optional[logging.Logger] = None):
        self.perplexity = perplexity
        self.n_iter = n_iter
        self.random_state = random_state
        self.logger = logger or logging.getLogger(__name__)
        self.tsne = None
        
    def project(self, high_dim_data: np.ndarray) -> np.ndarray:
        """Project high-dimensional data into 3D space"""
        self.logger.info("Initiating projection through the White Lodge...")
        
        self.tsne = TSNE(
            n_components=3,
            perplexity=self.perplexity,
            n_iter=self.n_iter,
            random_state=self.random_state
        )
        
        coords_3d = self.tsne.fit_transform(high_dim_data)
        self.logger.info("Projection complete")
        
        return coords_3d
