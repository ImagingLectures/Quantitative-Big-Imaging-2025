# Skeletons 
- [Streets and roots](07-Skeletons.ipynb). Analyzing thin structures in 2D and 3D images using skeletons.

# Tasks

## Working with skeletons in 2D
Analyse the street skeleton using the binary code kernels from the lecture.

Mainly copying from the lecture:
1. Load image and segment it
2. Create the skeleton
2. Prune it using the width criterion
3. Convolve skeleton by 4- and 8-connected masks.
4. Extract skeleton from resulting image

Task
1. Identify directions of end points
2. Count how many different junction points there are.
3. What happens to the codes at the loop in the lower end when you use different connectivities.


## Working with skeletons in 3D
Analyse the root network in terms of 
1. Distance between branches
2. Turtosity
3. Root segment position
4. Root segment angle in the vertical direction.