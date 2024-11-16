# tests/test_tsneakpeaks.py
import pytest
import numpy as np
from pathlib import Path
from tsneakpeaks import TSneakPeaks, BlackLodge, WhiteLodge, Visualizer

@pytest.fixture
def test_data_dir(tmp_path):
    """Create test data directory with sample images and labels"""
    data_dir = tmp_path / "test_data"
    data_dir.mkdir()
    
    # Create test images
    for i in range(5):
        img = np.random.randint(0, 255, (64, 64, 3), dtype=np.uint8)
        img_path = data_dir / f"image_{i:04d}.png"
        Image.fromarray(img).save(img_path)
    
    # Create test labels
    labels = np.random.rand(5, 10)
    np.save(data_dir / "labels.npy", labels)
    
    return data_dir

def test_tsneakpeaks_initialization(test_data_dir):
    """Test basic initialization"""
    peaks = TSneakPeaks(str(test_data_dir))
    assert isinstance(peaks.black_lodge, BlackLodge)
    assert isinstance(peaks.white_lodge, WhiteLodge)
    assert isinstance(peaks.visualizer, Visualizer)

def test_data_loading(test_data_dir):
    """Test data loading functionality"""
    peaks = TSneakPeaks(str(test_data_dir))
    peaks.load_data()
    
    assert len(peaks.image_paths) == 5
    assert peaks.labels.shape == (5, 10)

def test_dimension_reduction(test_data_dir):
    """Test dimension reduction"""
    peaks = TSneakPeaks(str(test_data_dir))
    peaks.load_data()
    peaks.reduce_dimensions()
    
    assert peaks.coords_3d.shape == (5, 3)

def test_visualization(test_data_dir):
    """Test visualization creation"""
    peaks = TSneakPeaks(str(test_data_dir))
    peaks.load_data()
    fig = peaks.visualize()
    
    assert fig is not None
    assert 'data' in fig
    assert len(fig.data) > 0

def test_error_handling(tmp_path):
    """Test error handling for invalid data"""
    with pytest.raises(FileNotFoundError):
        peaks = TSneakPeaks(str(tmp_path))
        peaks.load_data()
