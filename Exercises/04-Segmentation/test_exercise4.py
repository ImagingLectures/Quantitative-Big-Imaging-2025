import numpy as np
import pytest
from tasks import *
from skimage.io import imread
from sklearn.metrics import roc_curve, auc

def test_dice_coefficient_identical_masks():
    """Test Dice coefficient for identical masks (should be 1.0)."""
    y_true = np.array([[1, 1, 0], [0, 1, 1]])
    y_pred = np.array([[1, 1, 0], [0, 1, 1]])
    assert dice_coefficient(y_true, y_pred) == 1.0

def test_dice_coefficient_no_overlap():
    """Test Dice coefficient for completely different masks (should be 0.0)."""
    y_true = np.array([[1, 1, 0], [0, 1, 1]])
    y_pred = np.array([[0, 0, 1], [1, 0, 0]])
    assert dice_coefficient(y_true, y_pred) == 0.0

def test_dice_coefficient_partial_overlap():
    """Test Dice coefficient for a partial overlap."""
    y_true = np.array([[1, 0], [1, 1]])
    y_pred = np.array([[1, 1], [1, 0]])
    expected_dice = 2 * 2 / (3 + 3)  # 2 * |intersection| / (|A| + |B|)
    assert np.isclose(dice_coefficient(y_true, y_pred), expected_dice, atol=1e-6)

def test_dice_coefficient_empty_masks():
    """Test Dice coefficient for empty masks (should be 1.0)."""
    y_true = np.zeros((3, 3), dtype=int)
    y_pred = np.zeros((3, 3), dtype=int)
    assert dice_coefficient(y_true, y_pred) == 1.0

def test_dice_coefficient_shape_mismatch():
    """Test that a ValueError is raised for mismatched shapes."""
    y_true = np.zeros((3, 3), dtype=int)
    y_pred = np.zeros((4, 3), dtype=int)
    with pytest.raises(ValueError):
        dice_coefficient(y_true, y_pred)


def test_jaccard_index_identical_masks():
    """Test Jaccard index for identical masks (should be 1.0)."""
    y_true = np.array([[1, 1, 0], [0, 1, 1]])
    y_pred = np.array([[1, 1, 0], [0, 1, 1]])
    assert jaccard_index(y_true, y_pred) == 1.0

def test_jaccard_index_no_overlap():
    """Test Jaccard index for completely different masks (should be 0.0)."""
    y_true = np.array([[1, 1, 0], [0, 1, 1]])
    y_pred = np.array([[0, 0, 1], [1, 0, 0]])
    assert jaccard_index(y_true, y_pred) == 0.0

def test_jaccard_index_partial_overlap():
    """Test Jaccard index for a partial overlap."""
    y_true = np.array([[1, 0], [1, 1]])
    y_pred = np.array([[1, 1], [1, 0]])
    expected_iou = 2 / (3 + 3 - 2)  # |intersection| / |union|
    assert np.isclose(jaccard_index(y_true, y_pred), expected_iou, atol=1e-6)

def test_jaccard_index_empty_masks():
    """Test Jaccard index for empty masks (should be 1.0)."""
    y_true = np.zeros((3, 3), dtype=int)
    y_pred = np.zeros((3, 3), dtype=int)
    assert jaccard_index(y_true, y_pred) == 1.0

def test_jaccard_index_shape_mismatch():
    """Test that a ValueError is raised for mismatched shapes."""
    y_true = np.zeros((3, 3), dtype=int)
    y_pred = np.zeros((4, 3), dtype=int)
    with pytest.raises(ValueError):
        jaccard_index(y_true, y_pred)


def test_create_mask():
    gt = imread("teeth_gt_mask.tif")
    pred = create_mask()
    assert gt.shape == pred.shape

    # Check that the mask is binary
    assert np.all(np.logical_or(pred == 0, pred == 1))

    dice_coefficient_val = dice_coefficient(gt, pred)
    assert dice_coefficient_val > 0.95

    jaccard_index_val = jaccard_index(gt, pred)
    assert jaccard_index_val > 0.90





    
