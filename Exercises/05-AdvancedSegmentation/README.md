# Exercises for lecture 5 - Advanced segmentation

## Learning Objectives
- Explore and evaluate simple segmentation algorithms
- Explore and evaluate advanced methods for segmentation

## Preparation
- Accept assignment: **THERE IS NO GITHUB ASSIGNMENT FOR THIS EXERCISE**
- Clone your student repository (```git clone```)
- Run `uv sync` and check everything is correct with `uv run hello.py`
- Start Jupyter


# Exercise
1. Basic segmentation
    1. Download the [electron microscopy dataset](https://www.epfl.ch/labs/cvlab/data/data-em/) from https://documents.epfl.ch/groups/c/cv/cvlab-unit/www/data/%20ElectronMicroscopy_Hippocampus/testing.tif
    2. Following the notebook `segmentation_intro.ipynb`, find the best segmentation pipeline to segment the mitochondria. 
    3. Evaluate the performance of your pipeline with the given ground truth labels.
    4. Which kind of errors occur? Why?
2. SAM-based segmentation on 3Dslicer.
    1. Follow the instructions in the [MEDSAM 3DSLicer plugin repository](https://github.com/bowang-lab/MedSAMSlicer?tab=readme-ov-file) to install 3Dslicer and the plugin.
    2. Using the previously downloaded dataset, locate the mitochondria by selecteing regions of interest. Refer to the instruction on the repository if needed. 
    3. Which kind of errors occur? Why?
    4. What problems do you find by segmenting the data using this pipeline.
3. CNN segmentation
    1. Download the [entire dataset](https://www.epfl.ch/labs/cvlab/data/data-em/) (both training and test subsets). 
    2. Following the notebook `cnn_segmentation_intro.ipynb`, create a dataloader (with augmentations if necessary) and a training pipeline.
    3. Train and evaluate the performance of the model.
    4. Which kind of errors occur? Why? 
    5. How does it compare to the basic segmentation approach?
    > Note: If you do not have a GPU on your machine, you can find the same notebook on Google Collab: [URL](https://colab.research.google.com/github/qubvel/segmentation_models.pytorch/blob/main/examples/binary_segmentation_intro.ipynb)
