import numpy as np

def a_times_b_plus_c(a: np.ndarray, b: np.ndarray, c: np.ndarray)-> np.ndarray:
    """
    Implement the function a * b + c for numpy arrays after checking whether the dimensions are right. In case the dimensions are not right, raise a ValueError.

    Args:
        a (np.ndarray): 
        b (np.ndarray): 
        c (np.ndarray): 

    Returns:
        np.ndarray: 
    """
    raise NotImplementedError("Need to implement for task 1.1")

def add_gaussian_noise(a: np.ndarray)-> np.ndarray:
    """
    Implement the function to add Gaussian noise to an image. The noise should have a mean of mu and a standard deviation of sigma.

    Args:
        a (np.ndarray): 
        mu (float): 
        sigma (float): 

    Returns:
        np.ndarray: 
    """
    raise NotImplementedError("Need to implement for task 1.2")

def expsq(x: np.ndarray, sigma: float)-> np.ndarray:
    """
    Implement the function to compute the exponential square of the input x divided by the square of sigma.

    Args:
        x (np.ndarray): 

    Returns:
        np.ndarray: 
    """
    raise NotImplementedError("Need to implement for task 1.3")

def compute_sinc_of_sqrt_in_range(x_range: tuple[int, int], y_range: tuple[int, int]) -> np.ndarray:
    """
    Implement the function to compute the sinc of the square root of the coordinates (x,y) in the ranges x_range and y_range.

    Args:
        x_range (tuple[int, int]): 
        y_range (tuple[int, int]): 

    Returns:
        np.ndarray: 
    """
    raise NotImplementedError("Need to implement for task 2.1")

def get_A_M()->float:
    """
    Return the constant A of Moore's Law.

    Returns:
        float: 
    """
    raise NotImplementedError("Need to implement for task 4.1")

def get_B_M()->float:
    """
    Return the constant B of Moore's Law.

    Returns:
        float: 
    """
    raise NotImplementedError("Need to implement for task 4.1")

def moore_law(year: int)->float:
    """
    Implement the function to compute the number of transistors in a microchip in a given year according to Moore's Law.
    
    Args:
        year (int):

    Returns:
        float: 
    """ 
    A_M = get_A_M()
    B_M = get_B_M()
    raise NotImplementedError("Need to implement for task 4.1")


def load_data()-> np.ndarray:
    """
    Implement the function to load the transistors data from the file transistors.csv.

    Returns:
        np.ndarray: where the first column are the years and the second column the data entries.
    """
    # Downloaded from: https://raw.githubusercontent.com/numpy/numpy-tutorials/refs/heads/main/content/transistor_data.csv
    path = "Exercises/01-Images/transistor_data.csv"
    raise NotImplementedError("Need to implement for task 4.2")

def lstsq(X: np.ndarray, y: np.ndarray)-> np.ndarray:
    """
    Implement the function to compute the least squares solution for the input data X and y.

    Args:
        X (np.ndarray): 
        y (np.ndarray): 

    Returns:
        np.ndarray: 
    """
    raise NotImplementedError("Need to implement for task 4.3")

def fit_moore_law(X: np.ndarray, y: np.ndarray)-> tuple[float, float]:
    """
    Implement the function to fit the Moore's Law model to the data X and y.

    Args:
        X (np.ndarray): 
        y (np.ndarray):

    Returns:
        tuple: (A, B) where A and B are the constants of Moore's Law.
    """
    raise NotImplementedError("Need to implement for task 4.4")

def predict_transistors(year: int)->float:
    """
    Implement the function to compute the number of transistors in a microchip in a given year according to Moore's Law.

    Args:
        year (int):

    Returns:
        float: 
    """
    data = load_data()
    X = ...
    y = ...
    A, B = fit_moore_law(X, y)
    raise NotImplementedError("Need to implement for task 4.5")

