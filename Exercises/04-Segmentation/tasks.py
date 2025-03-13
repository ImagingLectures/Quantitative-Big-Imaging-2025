import numpy as np
from skimage.io import imread
from skimage.morphology import binary_closing
from scipy.ndimage import median_filter

def dice_coefficient(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Computes the Dice Coefficient (https://en.wikipedia.org/wiki/Dice-S%C3%B8rensen_coefficient) between the ground truth and predicted segmentation masks.
    
    The Dice Coefficient measures the similarity between two binary masks and is defined as:
    
        Dice = 2 * (|A ∩ B|) / (|A| + |B|)
    
    where:
      - A is the set of foreground pixels in the ground truth mask.
      - B is the set of foreground pixels in the predicted mask.
    
    Args:
        y_true (np.ndarray): Binary ground truth mask (0 or 1).
        y_pred (np.ndarray): Binary predicted mask (0 or 1).
    
    Returns:
        float: Dice Coefficient, a value between 0 and 1 (higher is better).
    
    Raises:
        ValueError: If inputs are not the same shape.
    """
    if y_true.shape != y_pred.shape:
        raise ValueError("Input masks must have the same shape.")

    intersection = np.sum(y_true * y_pred)
    denominator = np.sum(y_true) + np.sum(y_pred)

    if denominator == 0:
        return 1.0  # If both masks are empty, consider perfect match

    return 2. * intersection / denominator


def jaccard_index(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Computes the Jaccard Index (Intersection over Union, IoU) between 
    the ground truth and predicted segmentation masks.
    
    The Jaccard Index (https://en.wikipedia.org/wiki/Jaccard_index) is defined as:
    
        IoU = |A ∩ B| / |A ∪ B|
    
    where:
      - A is the set of foreground pixels in the ground truth mask.
      - B is the set of foreground pixels in the predicted mask.
    
    Args:
        y_true (np.ndarray): Binary ground truth mask (0 or 1).
        y_pred (np.ndarray): Binary predicted mask (0 or 1).
    
    Returns:
        float: Jaccard Index, a value between 0 and 1 (higher is better).
    
    Raises:
        ValueError: If inputs are not the same shape.
    """
    if y_true.shape != y_pred.shape:
        raise ValueError("Input masks must have the same shape.")

    intersection = np.sum(y_true * y_pred)
    union = np.sum(y_true) + np.sum(y_pred) - intersection
    return intersection / union if union > 0 else 1.0  # Handle case where both masks are empty


def create_mask() -> np.ndarray:
    """
    Function that loads the teeth dataset and creates a segmentation mask of the data.

    Returns:
        np.ndarray: _description_
    """
    data = imread("teeth_image.tif")

    filter_teeth_data = median_filter(data, (3,3,3))

    threshold = 50 # set the correct threshold here
    thresh_filt_teeth_data = filter_teeth_data > threshold

    thresh_filt_teeth_data = binary_closing(thresh_filt_teeth_data)
    return thresh_filt_teeth_data

    # Create a mask of the data
    raise NotImplementedError("Complete the create_mask() function")