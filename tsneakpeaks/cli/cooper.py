#!/usr/bin/env python3
"""
Command-line interface for TSneakPeaks
Named after Agent Dale Cooper, who guides us through the mysteries
"""

import argparse
import sys
from pathlib import Path
from ..laura import TSneakPeaks
from ..owl_cave import setup_logging

def main():
    parser = argparse.ArgumentParser(
        description="TSneakPeaks: A dimensional journey through image collections"
    )
    parser.add_argument("data_dir", type=str, help="Path to image directory")
    parser.add_argument("--perplexity", type=int, default=30,
                       help="t-SNE perplexity parameter")
    parser.add_argument("--debug", action="store_true",
                       help="Enable debug logging")
    
    args = parser.parse_args()
    logger = setup_logging(debug=args.debug)
    
    try:
        peaks = TSneakPeaks(args.data_dir, logger=logger)
        peaks.load_data()
        fig = peaks.visualize()
        fig.show()
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
