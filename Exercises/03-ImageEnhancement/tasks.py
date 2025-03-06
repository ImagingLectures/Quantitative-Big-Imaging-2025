import numpy as np
from skimage.io import imread

def mse(img1,img2):
    return np.mean((img1-img2)**2)

def snr_mean_std(image: np.ndarray) -> float:
    """Compute SNR as mean divided by standard deviation."""
    raise NotImplementedError("Implement me!")

def snr_power_linear(img: np.ndarray) -> float:
    """Compute SNR as signal power (mean squared) over noise power (variance)."""
    raise NotImplementedError("Implement me!")

def psnr(img: np.ndarray, max_val: float = 255.0) -> float:
    """
    Compute the Peak Signal-to-Noise Ratio (PSNR) of an image.

    PSNR is defined as:

    .. math::
        PSNR = 10 \\log_{10} \\left(\\frac{\\max(I)^2}{\\sigma^2} \\right)

    where:
        - \\( \\max(I) \\) is the maximum possible pixel value (e.g., 255 for 8-bit images).
        - \\( \\sigma^2 \\) is the variance of the image, assumed to represent noise.

    Parameters:
        img (np.ndarray): Input image.
        max_val (float, optional): Maximum pixel value. Defaults to 255.

    Returns:
        float: PSNR value in decibels (dB). Returns `inf` if the variance is zero.
    """
    raise NotImplementedError("Implement me!")


def snr_known_noise(image: np.ndarray, noise: np.ndarray) -> float:
    """Calculate the Signal-to-Noise Ratio (SNR) of an image using a known noise image.

    Parameters:
        image (np.ndarray): The input image.
        noise (np.ndarray): The noise image.

    Returns:
        float: The SNR value in dBs.

    Raises:
        ZeroDivisionError: If the sum of noise squared is zero.
    """
    raise NotImplementedError("Implement me!")


def snr_second_region_image_a() -> float:
    """
    Identify a constant region on the sample and compute the snr as the mean divided by the standard deviation.

    Returns:
        float: SNR value for the selected region.
    """
    raise NotImplementedError("Implement me!")
    

def snr_image_b() -> float:
    """
    Identify a constant region outside of the sample and compute the snr as the mean divided by the standard deviation.

    Returns:
        float: SNR value for the selected region.
    """
    raise NotImplementedError("Implement me!")

def snr_image_c() -> float:
    """
    Identify a constant region outside of the sample and compute the snr as the mean divided by the standard deviation.

    Returns:
        float: SNR value for the selected region.
    """
    raise NotImplementedError("Implement me!")

def filter_image_gaussian_noise() -> np.ndarray:
    """
    Filter the image to reduce the noise.

    Returns:
        np.ndarray: The filtered image.
    """
    original_img=np.mean(imread('data/testpattern.png'),2)/255.
    SNR=2
    noised_image = original_img/original_img.max() + 1.0/SNR*np.random.normal(0,1,size=original_img.shape)
    raise NotImplementedError("Implement me!")

def filter_image_poisson_noise() -> np.ndarray:
    """
    Filter the image to reduce the noise.

    Returns:
        np.ndarray: The filtered image.
    """
    original_img=np.mean(imread('data/testpattern.png'),2)/255.
    SNR=2
    noised_image = original_img/original_img.max() + 1.0/SNR*np.random.poisson(5,size=original_img.shape)
    raise NotImplementedError("Implement me!")