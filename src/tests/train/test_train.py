"""A set of tests for train.py ."""

#import sys
#sys.path.append( 'src/segmentation/train/' )
#sys.path.append( '/segmentation/train/' )
#sys.path.append( './segmentation/train/' )
#from train import get_training_data

#sys.path.append('segmentation/')
#from train.train import get_training_data

#sys.path.append('./')
from segmentation.train.train import get_training_data

def test_get_training_data():
    """Assert training data is loaded."""
    assert len(get_training_data()) != 0
