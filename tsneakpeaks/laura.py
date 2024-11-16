# tsneakpeaks/laura.py
"""
Laura: The main TSneakPeaks application class
Like Laura Palmer, this ties everything together
"""

import numpy as np
from pathlib import Path
from typing import Optional
import logging

from .black_lodge import BlackLodge
from .white_lodge import WhiteLodge
from .waiting_room import WaitingRoom
from .red_room import Visualizer
from .owl_cave import setup_logging, get_config

class TSneakPeaks:
    """Main class for the TSneakPeaks visualization system"""
    
    def __init__(self, 
                 data_dir: str,
                 logger: Optional[logging.Logger] = None):
        """Initialize TSneakPeaks"""
        self.data_dir = Path(data_dir)
        self.logger = logger or setup_logging()
        
        # Initialize components
        self.black_lodge = BlackLodge(self.data_dir, self.logger)
        self.white_lodge = WhiteLodge(logger=self.logger)
        self.waiting_room = WaitingRoom(logger=self.logger)
        self.visualizer = Visualizer(logger=self.logger)
        
        # Data storage
        self.image_paths = []
        self.labels = None
        self.coords_3d = None
        
        # Load configuration
        self.config = get_config()
        
    def load_data(self) -> None:
        """Load and prepare data"""
        # Enter the Black Lodge to retrieve our data
        self.image_paths, self.labels = self.black_lodge.enter()
        
        # Generate labels if none exist
        if self.labels is None:
            self.labels = self.black_lodge.generate_labels()
            
        # Validate in the Waiting Room
        self.waiting_room.validate_data(self.image_paths, self.labels)
        self.labels = self.waiting_room.preprocess_labels(self.labels)
        
    def reduce_dimensions(self) -> None:
        """Project through the White Lodge"""
        if self.labels is None:
            raise ValueError("No data loaded. Call load_data() first.")
            
        self.coords_3d = self.white_lodge.project(self.labels)
        
    def visualize(self, title: str = "TSneakPeaks: A Vision") -> 'plotly.graph_objects.Figure':
        """Create visualization in the Red Room"""
        if self.coords_3d is None:
            self.reduce_dimensions()
            
        return self.visualizer.create_figure(
            self.coords_3d,
            self.labels,
            self.image_paths,
            title
        )
