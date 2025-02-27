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
    # raise NotImplementedError("Need to implement for task 2.1")
    indices = np.random.choice(len(data), n, replace=False)  # Randomly select n images
    selected_images = data[indices]
    selected_labels = labels[indices]
    return selected_images, selected_labels


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
    # raise NotImplementedError("Need to implement for task 2.2")

    transform = A.Compose([
        A.HorizontalFlip(p=0.5),
        A.RandomBrightnessContrast(p=0.1),
        A.RandomCrop(width=64, height=64),
    ])

    aug_images = []
    aug_labels = []
    for im, label in zip(data, labels):
        for _ in range(5):
            transformed = transform(image=im)["image"]
            aug_images.append(transformed)
            aug_labels.append(label)

    aug_images = np.array(aug_images)
    aug_labels = np.array(aug_labels)

    return aug_images, aug_labels

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

    if shuffle:
        indices = np.random.permutation(len(data))
        data = data[indices]
        labels = labels[indices]

    n = int(len(data) * percentage)
    train_data, test_data = data[:n], data[n:]
    train_labels, test_labels = labels[:n], labels[n:]

    return (train_data, train_labels), (test_data, test_labels)


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
    # raise NotImplementedError("Need to implement for task 2.3")
    kNN = KNeighborsClassifier(n_neighbors=k)
    data = data.reshape(data.shape[0], -1)
    kNN.fit(data, labels)
    return kNN

def predict_kNN(kNN: KNeighborsClassifier, data: np.ndarray) -> np.ndarray:
    """
    Implement the function to predict the labels of the data using the trained kNN classifier.

    Args:
        kNN (KNeighborsClassifier): 
        data (np.ndarray): 

    Returns:
        np.ndarray: 
    """
    # raise NotImplementedError("Need to implement for task 2.3")
    data = data.reshape(data.shape[0], -1)
    return kNN.predict(data)

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
    # raise NotImplementedError("Need to implement for task 2.3")
    return metric(ground_truth, labels)