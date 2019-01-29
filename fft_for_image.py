from numpy import fft
import numpy as np
from skimage.color import rgb2gray


def fft_vs_noise(x: np.ndarray):
    x = rgb2gray(x)
    fft_img = fft.fft2(x)

    fil = fft_img.copy()
    r, c = fil.shape
    keep_fraction = 0.06
    fil[int(r*keep_fraction):int(r*(1-keep_fraction))] = 0
    fil[:, int(c*keep_fraction):int(c*(1-keep_fraction))] = 0

    img_ = fft.ifft2(fil).real
    return img_
