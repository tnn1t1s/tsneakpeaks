# TSneakPeaks 🌲

⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸    A Lynchian journey through high-dimensional
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⢸    image spaces using t-SNE. Navigate between
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸    dimensions like Agent Cooper through the
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸    Black and White Lodge.

Through the curtain of dimensionality reduction, your high-dimensional image features are projected into a navigable 3D space where patterns and relationships reveal themselves in mysterious ways.

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/tsneakpeaks.git
cd tsneakpeaks

# Create and activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package
pip install -e .
```

### Generate Test Data

```python
# Create test data
python examples/generate_test.py
```

### Run Visualization

```python
# Visualize the data
python examples/visualize.py
```

## Features

╔═══════════════════════════════════════════╗
║ ⌘ Navigate image collections in 3D space   ║
║ ⌘ Project features through t-SNE          ║
║ ⌘ Dark mode inspired by the Black Lodge   ║
║ ⌘ Interactive exploration                 ║
║ ⌘ Dimensional coupling controls           ║
╚═══════════════════════════════════════════╝

## Requirements

- Python 3.8+
- NumPy
- scikit-learn
- Plotly
- Pillow

## Project Structure

```
TSneakPeaks/
├── tsneakpeaks/
│   ├── black_lodge.py    # High-dimensional data handling
│   ├── white_lodge.py    # Dimension reduction
│   ├── red_room.py       # Visualization
│   ├── waiting_room.py   # Data preprocessing
│   ├── owl_cave.py       # Logging/config
│   └── laura.py          # Core application
├── examples/
│   ├── generate_test.py
│   └── visualize.py
└── tests/
```

## Usage Examples

### Basic Usage

```python
from tsneakpeaks import TSneakPeaks

# Initialize and run visualization
peaks = TSneakPeaks("path/to/images")
peaks.load_data()
fig = peaks.visualize()
fig.show()
```

### Advanced Configuration

```python
from tsneakpeaks import TSneakPeaks
import logging

# Setup custom logging
logger = logging.getLogger("TSneakPeaks")
logger.setLevel(logging.DEBUG)

# Initialize with custom parameters
peaks = TSneakPeaks(
    data_dir="path/to/images",
    logger=logger
)

# Customize visualization
peaks.load_data()
fig = peaks.visualize("My Custom Vision")
fig.update_layout(
    scene=dict(
        bgcolor='rgb(30,0,0)',  # Dark red background
    )
)
fig.show()
```

## Data Format

The tool expects:
- A directory containing images (PNG format)
- Optional `labels.npy` file with feature vectors
- If no labels are provided, they will be generated from image features

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Citation

```bibtex
@software{tsneakpeaks2024,
  title={TSneakPeaks: Lynchian Dimensionality Reduction Visualization},
  year={2024},
  description={Where we're from, the birds sing a pretty song}
}
```

     ╭┳┳┳┳┳┳┳┳┳┳┳┳┳┳┳╮
     ┣┫┃┃┃┃┃┃┃┃┃┃┃┃┃┃┫        "The visualization 
     ┣┫┃┃┃┃┃┃┃┃┃┃┃┃┃┃┫         is not what it seems..."
     ┣┫┃┃┃┃┃┃┃┃┃┃┃┃┃┃┫                      🦉
     ╰┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻╯
