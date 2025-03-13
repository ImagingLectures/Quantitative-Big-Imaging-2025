# Exercise for lecture 4 - Image Segmentation

## Learning Objectives
- Explore a basic segmentation pipeline with filtering and thresholding
- Evaluate the quality of the segmentation when a ground truth is available

## Preparation
- Accept assignment: https://classroom.github.com/a/kMf68qK6
- Clone your student repository (```git clone```)
- Run `uv sync` and check everything is correct with `uv run hello.py`
- Start Jupyter

## Exercise
1. Evaluate on images the SNR according to different definitions
2. Tune the parameters of different filters in different noise conditions to achieve a target MSE.

# Exercise
Notebook `04-Fossil.ipynb` has shown you how to apply a threshold on an image to segment it into a bilevel image. The performance of the threshold was improved by applying a filter that reduced the noise levels in the image. Now you can try this workflow on a different image.

 1. Repeat the same analysis to the teeth fossil data (```teeth_image.tif```)
 2. Adjust the threshold and angles to try and see the gut structure better
 3. Improve the filters by using more advanced techniques and windows (bonus for non-local means)

In `tasks.py` you will have to implement to common metrics to evalaute segmentation masks:
- [Dice coefficient](https://en.wikipedia.org/wiki/Dice-S%C3%B8rensen_coefficient)
- [Jaccard index](https://en.wikipedia.org/wiki/Jaccard_index)

First, you will have to read about the metrics and implement them to pass the corresponding tests.
Then, you will have to implement a basic segmentation pipeline on the dataset `teeth_image.tif` that achieves a `dice_coefficient > 0.95` and a `jaccard_index > 0.95`
