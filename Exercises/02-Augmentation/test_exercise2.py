import numpy as np
import pandas as pd
import skimage.io as io
from tasks import *
import pytest
from sklearn.metrics import accuracy_score

@pytest.fixture(scope="session")
def loaded_data():
    # Load your data once
    imgs = io.imread('ct_tiles.tif')
    labels = pd.read_csv('malignancy.csv').malignancy.values
    return imgs, labels

def test_dataset_subset(loaded_data):
    imgs, labels = loaded_data

    n = 500
    subset_imgs, subset_labels = create_dataset_subset(imgs, labels, n)
    assert subset_imgs.shape[0] == n
    assert subset_labels.shape[0] == n
    assert subset_imgs.shape[1:] == imgs.shape[1:]
    assert (subset_labels.sum()/n > 0.3) and (subset_labels.sum()/n < 0.5)


def test_augment_data(loaded_data):
    imgs, labels = loaded_data

    subset_imgs, subset_labels = create_dataset_subset(imgs, labels, 500)

    augmented_imgs, augmented_labels = augment_data(subset_imgs, subset_labels)
    
    assert augmented_imgs.shape[0] == 2500
    assert augmented_labels.shape[0] == 2500
    assert augmented_imgs.shape[1:] == (64, 64)

    assert (augmented_labels.sum()/2500 > 0.3) and (augmented_labels.sum()/2500 < 0.5)

def test_split_train_test_data(loaded_data):
    imgs, labels = loaded_data
    imgs, labels = create_dataset_subset(imgs, labels, 500)

    (train_imgs, train_labels), (test_imgs, test_labels) = split_train_test_dataset(imgs, labels, 0.8, shuffle=False)

    assert train_imgs.shape[0] == 400
    assert train_labels.shape[0] == 400
    assert test_imgs.shape[0] == 100
    assert test_labels.shape[0] == 100

    assert (train_labels.sum()/400 > 0.3) and (train_labels.sum()/400 < 0.5)
    assert (test_labels.sum()/100 > 0.3) and (test_labels.sum()/100 < 0.5)

def test_train_and_test_kNN(loaded_data):
    imgs, labels = loaded_data
    imgs, labels = create_dataset_subset(imgs, labels, 500)

    (train_imgs, train_labels), (test_imgs, test_labels) = split_train_test_dataset(imgs, labels, 0.8, shuffle=False)

    kNN = train_kNN(train_imgs, train_labels, 1)
    predictions = predict_kNN(kNN, test_imgs)
    assert predictions.shape[0] == 100
    accuracy = evaluate_predictions(test_labels, predictions, accuracy_score)
    assert accuracy > 0.6


def test_train_and_test_kNN_with_augmented_data(loaded_data):
    imgs, labels = loaded_data
    imgs, labels = create_dataset_subset(imgs, labels, 500)

    (train_imgs, train_labels), (test_imgs, test_labels) = split_train_test_dataset(imgs, labels, 0.8, shuffle=False)

    augmented_imgs, augmented_labels = augment_data(train_imgs, train_labels)
    
    kNN = train_kNN(augmented_imgs, augmented_labels, 3)
    predictions = predict_kNN(kNN, test_imgs)
    assert predictions.shape[0] == 100
    accuracy = evaluate_predictions(test_labels, predictions, accuracy_score)
    assert accuracy > 0.7





