# Exercises
## Objectives
- The main goal is for the students to get familiar with the practical implementation of the topics covered during the lectures. 
- Interactive jupyter notebooks are provided to run code snippets with no need of coding
- Code exercises are proposed for those who want to get their hands into the code, which are evaluated with unit tests (either locally or with the autograder on Github) to give feedback to the students. 
- Exercises are optional and are not graded.

## List of exercises
While exercises can be solved locally, they have complementary Github classroom assigments. Students can join the assigment with the following URLs:
- Exercise 1: https://classroom.github.com/a/CokEhI-7
- Exercise 2: https://classroom.github.com/a/Zz9PEnY2
- Exercise 3: Coming soon... 
- Exercise 4: Coming soon... 
- Exercise 5: Coming soon... 
- Exercise 6: Coming soon... 
- Exercise 7: Coming soon... 
- Exercise 8: Coming soon... 
- Exercise 9: Coming soon... 

## Setup

You will need:
- A Github account
- [Python](https://www.python.org/downloads/) 3.11 or higher. You can check your python version running `python --version`. 
- [git](https://git-scm.com/) for version control 
- [uv](https://docs.astral.sh/uv/getting-started/installation/) for python packages and environments management.
- Basic usage of the terminal and jupyter notebooks and a basic understanding of python and linear algebra.
- [OPTIONAL] [Visual studio code](https://code.visualstudio.com/)
- [OPTIONAL] Sign up for the [Github Student developer pack](https://education.github.com/) which provides useful tools such as Github Copilot.


The usual workflow goes as follows:
1. Accept the assigment corresponding to the exercise using the above URLs
2. Clone the newly minted repository: `git clone <REPO URL>` and `cd` into the repo directory.
3. Run `uv sync` to create a virtual environment with all necessary libraries.
4. Test you can run `uv run hello.py`
5. Now you can open the notebook on your favorite IDE (e.g. Visual Studio) and select `.venv` as kernel.
6. You can also complete the exercises. To test whether the implementation is correct you can run the tests locally with `uv run pytest .`
7. Submit your solution to the repository on Github. You will need to:
    1. Select the modified files you want to include, usually all of them: `git add .`
    2. Create a checkpoint of the current changes with a descriptive message: `git commit -m <YOUR MESSAGE>`. e.g.: `git commit -m "exercise completed"`
    3. Upload the new commit to your repository: `git push origin main`.

We recommend checking out the introductory videos to `git` if you are not yet familiar: https://git-scm.com/doc or the sections of the [git book](https://git-scm.com/book/en/v2) that are relevant for you.

### Alternative setups
While the setup described above is the recommended one, here we will list other potential ways of configuring a setup that could work.

#### Conda environment
You will need:
- A Github account
- [git](https://git-scm.com/) for version control 
- [Miniconda](https://docs.anaconda.com/miniconda/) for environment management
- Basic usage of the terminal and jupyter notebooks and a basic understanding of python and linear algebra.
- [OPTIONAL] [Visual studio code](https://code.visualstudio.com/)
- [OPTIONAL] Sign up for the [Github Student developer pack](https://education.github.com/) which provides useful tools such as Github Copilot.

The usual workflow goes as follows:
1. Accept the assigment corresponding to the exercise using the above URLs
2. Clone the newly minted repository: `git clone <REPO URL>` and `cd` into the repo directory.
3. Create a new environment with `conda create -n <NAME OF ENV>` e.g. `conda create -n qbi-ex1`.
4. Activate the environemnt with `conda activate <NAME OF ENV>`
5. Install the necessary libraries with `pip install -e .`
6. Test you can run `python hello.py`
7. Now you can open the notebook on your favorite IDE (e.g. Visual Studio) and select the environemnt you created as kernel.
8. You can also complete the exercises. To test whether the implementation is correct you can run the tests locally with `pytest .`
9. Submit your solution to the repository on Github. You will need to:
    1. Select the modified files you want to include, usually all of them: `git add .`
    2. Create a checkpoint of the current changes with a descriptive message: `git commit -m <YOUR MESSAGE>`. e.g.: `git commit -m "exercise completed"`
    3. Upload the new commit to your repository: `git push origin main`.
