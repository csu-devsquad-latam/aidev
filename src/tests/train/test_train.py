"""A set of tests for train.py ."""

import sys
sys.path.append('segmentation/')
from training import train

def test_get_training_data():
    """Assert training data is loaded."""
    train.LOCAL = True
    assert len(train.get_training_data()) != 0
