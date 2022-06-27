"""
A set of tests for train.py
"""
import sys
sys.path.append( 'src/segmentation/train/' )
from train import get_training_data

def test_get_training_data():
    assert len(get_training_data()) != 0
