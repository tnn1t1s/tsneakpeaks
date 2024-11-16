"""
The Owl Cave: Logging and configuration
Where we find the map to guide us
"""

import logging
from pathlib import Path
from typing import Optional

def setup_logging(debug: bool = False,
                 log_file: Optional[str] = None) -> logging.Logger:
    """Setup logging configuration"""
    
    # Create logger
    logger = logging.getLogger("TSneakPeaks")
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    
    # Create formatters
    console_formatter = logging.Formatter(
        '🌲 %(asctime)s - %(name)s - %(levelname)s - %(message)s 🌲'
    )
    
    # Setup console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    # Setup file handler if requested
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(console_formatter)
        logger.addHandler(file_handler)
    
    return logger

def get_config():
    """Load configuration (placeholder for future use)"""
    return {
        'default_perplexity': 30,
        'default_n_iter': 1000,
        'default_random_state': 42,
        'visualization_width': 1000,
        'visualization_height': 800,
    }
