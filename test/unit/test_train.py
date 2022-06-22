"""
A set of tests for train.py
"""
import sys
sys.path.append( 'src/customer-segmentation/train/' )
from train import get_training_data, configure_pipeline

def test_get_training_data():
    assert len(get_training_data()) != 0 

def test_configure_pipeline():
    pipeline = configure_pipeline(4, 286)
    assert len(pipeline.steps) == 2
