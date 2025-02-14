import numpy as np
from tasks import *
import pytest

@pytest.fixture(autouse=True)
def fix_random_seed():
    np.random.seed(42)

def test_a_times_b_plus_c():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = np.array([7, 8, 9])
    result = a_times_b_plus_c(a, b, c)
    expected = np.array([11, 18, 27])
    np.testing.assert_array_equal(result, expected)

    a = np.array([[
                [7, 4, 8, 5, 7],
                [3, 7, 8, 5, 4],
                [8, 8, 3, 6, 5],
                [2, 8, 6, 2, 5],
                [1, 6, 9, 1, 3],],

                [
                [7, 4, 9, 3, 5],
                [3, 7, 5, 9, 7],
                [2, 4, 9, 2, 9],
                [5, 2, 4, 7, 8],
                [3, 1, 4, 2, 8]
                ]])


    b = np.array([[[4, 2, 6, 6, 4],
                [6, 2, 2, 4, 8],
                [7, 9, 8, 5, 2],
                [5, 8, 9, 9, 1],
                [9, 7, 9, 8, 1]],

                [[8, 8, 3, 1, 8],
                [3, 3, 1, 5, 7],
                [9, 7, 9, 8, 2],
                [1, 7, 7, 8, 5],
                [3, 8, 6, 3, 1]]])

    c = np.array([[[3, 5, 3, 1, 5],
                [7, 7, 9, 3, 7],
                [1, 4, 4, 5, 7],
                [7, 4, 7, 3, 6],
                [2, 9, 5, 6, 4]]])

    expected = np.array([[[31, 13, 51, 31, 33],
                        [25, 21, 25, 23, 39],
                        [57, 76, 28, 35, 17],
                        [17, 68, 61, 21, 11],
                        [11, 51, 86, 14, 7]],

                        [[59, 37, 30, 4, 45],
                        [16, 28, 14, 48, 56],
                        [19, 32, 85, 21, 25],
                        [12, 18, 35, 59, 46],
                        [11, 17, 29, 12, 12]]])

    result = a_times_b_plus_c(a, b, c)
    np.testing.assert_array_equal(result, expected)

    a = np.random.randint(1, 10, (1, 5, 5))
    b = np.random.randint(1, 10, (2, 5, 1))
    c = np.random.randint(1, 10, (1, 5, 5))
    result = a_times_b_plus_c(a, b, c)
    assert result.shape == (2, 5, 5)

    with pytest.raises(Exception) as e_info:
        a = np.random.randint(1, 10, (1, 5, 5))
        b = np.random.randint(1, 10, (2, 5, 2))
        c = np.random.randint(1, 10, (1, 5, 5))
        result = a_times_b_plus_c(a, b, c)


def test_add_gaussian_noise():
    a = np.zeros((10, 10))
    result = add_gaussian_noise(a)
    print(result)
    assert result.shape == a.shape
    assert not np.array_equal(result, a)

def test_expsq():
    x = np.array([0, 1, 2])
    sigma = 1.0
    expected = [1., 0.36787944, 0.01831564]
    result = expsq(x, sigma)
    np.testing.assert_array_almost_equal(result, expected)

def test_compute_sinc_of_sqrt_in_range():
    res = compute_sinc_of_sqrt_in_range((-50,50), (-50,50))
    expected = np.load("sinc.npz")['z']
    np.testing.assert_array_almost_equal(res, expected)

def test_get_A_M():
    assert np.isclose(get_A_M(), 0.34657359)

def test_get_B_M():
    assert np.isclose(get_B_M(), -675.376697)

def test_moore_law():
    year = 1971
    expected = 2250
    result = moore_law(year)
    assert np.isclose(result, expected), f"Expected {expected}, but got {result}"

def test_moore_law2():
    year = 2020
    expected = 53384774413.6
    result = moore_law(year)
    assert np.isclose(result, expected), f"Expected {expected}, but got {result}"

def test_lstsq():
    X = np.array([[1, 1], [2, 1], [3, 1]])
    y = np.array([2, 2.5, 3.5])
    expected = np.linalg.lstsq(X, y, rcond=None)[0]
    result = lstsq(X, y)
    np.testing.assert_array_almost_equal(result, expected)

def test_fit_moore_law():
    X = np.array([[1971, 1], [1973, 1]])
    y = np.log(np.array([2250, 4500]))
    A, B = fit_moore_law(X, y)
    assert np.isclose(A, get_A_M())
    assert np.isclose(B, get_B_M())


def test_linear_pred():
    year = 1971
    expected = 1130.5147
    result = predict_transistors(year)
    print(result, expected)
    assert np.isclose(result, expected), f"Expected {expected}, but got {result}"

def test_linear_pred_2():
    year = 1980
    expected = 24467.8
    result = predict_transistors(year)
    assert np.isclose(result, expected), f"Expected {expected}, but got {result}"
