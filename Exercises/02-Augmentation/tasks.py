from typing import Callable
import numpy as np
import albumentations as A
from sklearn.neighbors import KNeighborsClassifier

def create_dataset_subset(data: np.ndarray, labels: np.ndarray, n: int) -> tuple[np.ndarray, np.ndarray]:
    """
    Implement the function to create a subset of the dataset with n samples maintaining the distribution of labels.

    Args:
        data (np.ndarray): 
        labels (np.ndarray): 
        n (int): 

    Returns:
        tuple[np.ndarray, np.ndarray]: 
    """
    raise NotImplementedError("Need to implement for task 2.1")
    

def augment_data(data: np.ndarray, labels: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Implement the function to augment the dataset by applying the following transformations:
    - RandomCrop
    - HorizontalFlip
    - VerticalFlip
    - RandomBrightnessContrast
    - ShiftScaleRotate

    Args:
        data (np.ndarray): 
        labels (np.ndarray): 

    Returns:
        tuple[np.ndarray, np.ndarray]: 
    """
    raise NotImplementedError("Need to implement for task 2.2")



def split_train_test_dataset(data: np.ndarray, labels: np.ndarray, percentage: float = 0.8, shuffle: bool = False) -> tuple[tuple[np.ndarray, np.ndarray], tuple[np.ndarray, np.ndarray]]:
    """
    Implement the function to split the dataset into training and testing sets.

    Args:
        data (np.ndarray): 
        labels (np.ndarray): 
        percentage (float): 
        shuffle (bool):

    Returns:
        tuple[tuple[np.ndarray, np.ndarray], tuple[np.ndarray, np.ndarray]]: 
    """
    raise NotImplementedError("Need to implement for task 2.3")



def train_kNN(data: np.ndarray, labels: np.ndarray, k: int) -> np.ndarray:
    """
    Implement the function to train kNN classifiers.

    Args:
        data (np.ndarray): 
        labels (np.ndarray): 
        k (int): 

    Returns: predictions
        np.ndarray 
    """
    raise NotImplementedError("Need to implement for task 2.3")
    

def predict_kNN(kNN: KNeighborsClassifier, data: np.ndarray) -> np.ndarray:
    """
    Implement the function to predict the labels of the data using the trained kNN classifier.

    Args:
        kNN (KNeighborsClassifier): 
        data (np.ndarray): 

    Returns:
        np.ndarray: 
    """
    raise NotImplementedError("Need to implement for task 2.3")
    

def evaluate_predictions(ground_truth: np.ndarray, labels: np.ndarray, metric: Callable) -> float:
    """
    Implement the function to evaluate the predictions using the given metric.

    Args:
        ground_truth (np.ndarray): 
        labels (np.ndarray): 
        metric (Callable): 

    Returns:
        float: 
    """
    raise NotImplementedError("Need to implement for task 2.3")
    