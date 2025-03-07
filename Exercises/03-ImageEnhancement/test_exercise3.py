from tasks import *
import pytest


def test_snr_known_noise():
    image = np.array([[1, 2], [3, 4]])
    noise = np.array([[0.1, 0.2], [0.3, 0.4]])
    assert snr_known_noise(image, noise) == 20.0
    image = np.array([[1, 2, 3], [4, 5, 6]])
    noise = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])
    assert snr_known_noise(image, noise) == 20.0
    image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    noise = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]])
    assert snr_known_noise(image, noise) == 20.0

def test_snr_mean_std():
    image = np.full((10, 10), 100)  # Uniform image
    assert snr_mean_std(image) == float('inf')  # No variation, should return inf
    
    image = np.array([[1, 2], [3, 4]])
    assert np.isfinite(snr_mean_std(image))  # Ensure it returns a finite number

def test_snr_power_linear():
    image = np.full((10, 10), 100)
    assert snr_power_linear(image) == float('inf')
    
    image = np.array([[1, 2], [3, 4]])
    assert np.isfinite(snr_power_linear(image))

def test_psnr():
    image = np.full((10, 10), 100)
    assert psnr(image, 255) == float('inf')
    
    image = np.array([[1, 2], [3, 4]])
    assert np.isfinite(psnr(image, 255))

def test_snr_known_noise():
    image = np.full((10, 10), 100)
    noise = np.full((10, 10), 10)
    assert np.isfinite(snr_known_noise(image, noise))
    
    with pytest.raises(ZeroDivisionError):
        snr_known_noise(image, np.zeros((10, 10)))  # Noise is zero, should raise error or return inf

def test_snr_with_known_phantom():
    np.random.seed(0)
    # Create a phantom where signal and noise are known
    signal = np.full((10, 10), 50, dtype=np.uint8)  # Known signal intensity
    noise = np.random.normal(0, 5, (10, 10))  # Known Gaussian noise with std=5
    image = signal + noise
    
    expected_snr_mean_std = 9.98
    expected_snr_power_linear = 99.62
    expected_snr_known_noise = 8.85
    expected_psnr = 34.08
    
    assert np.isclose(snr_mean_std(image), expected_snr_mean_std, atol=1e-1)
    assert np.isclose(snr_power_linear(image), expected_snr_power_linear, atol=1e-1)
    assert np.isclose(snr_known_noise(signal, noise), expected_snr_known_noise, atol=1e-1)
    assert np.isclose(psnr(image, 255), expected_psnr, atol=1e-1)


def test_snr_second_region_image_a():
    assert np.isclose(snr_second_region_image_a(), 3.48, atol=1e-1)

def test_snr_image_b():
    print(snr_image_b())
    assert np.isclose(snr_image_b(), 2.52, atol=1e-0)

def test_snr_image_c():
    assert np.isclose(snr_image_c(), 8.42, atol=1e-0)

def test_filter_gaussian_noise():
    original_img=np.mean(imread('data/testpattern.png'),2)/255.
    filtered_image = filter_image_gaussian_noise()
    assert mse(original_img, filtered_image) < 0.015

def test_filter_poisson_noise():
    original_img=np.mean(imread('data/testpattern.png'),2)/255.
    filtered_image = filter_image_gaussian_noise()
    assert mse(original_img, filtered_image) < 6