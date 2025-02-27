![](../../docs/figures/np_data_3132352_000000.png)
# Exercise for lecture 2 - Data augmentation

## Preparation
- Sync your QBI folder with Github (```git pull```)
- Unpack ```02_Files.zip```
- Start Jupyter

## Objectives
- How to augment images
- Working with a baseline algorithm

## Exercise
1. Evaluate the nearest neighbour baseline "properly" in this notebook.
Complete the functions in `tasks.py` and pass the tests. You will have to:
2. Create a subset of the original datasets with 500 images. Create an augmented data set of 2500 images from the selected subset. Pay attention to obtaining a representative balance between healthy and malign samples. The augmented images should be of size 64,64.
3. Fit a KNNs classifier using 
    1. the original subset of 500 data samples. You should achieve >60% accuracy.
    2. the augmented dataset. You should achieve >70% accuracy.
    > Note: You will have to play with the number, type and hyperparameters of the augmentations and the kNN classifier.
    > Note: You will have to implement the functions to train, predict and evaluate the kNN model.
4. Compare the performance using the confusion matrix. Plot it on this notebook.

> Tip: Solve each of the tasks first on the notebook, so it is easier to see the input and output of the functions. Check the file `test_exercise2.py` and the docstrings of each function to get more information on how to implement them.
