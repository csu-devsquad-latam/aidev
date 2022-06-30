"""A set of tests for train.py ."""

import sys
sys.path.append('segmentation/')
#from train.train import get_training_data
from training import train
#sys.path.append('./')
#from segmentation.train.train import get_training_data

def test_get_training_data():
    """Assert training data is loaded."""
    train.LOCAL = True
    #assert len(get_training_data()) != 0
    assert len(train.get_training_data()) != 0
