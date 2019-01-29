import numpy as np
from skimage.color import rgb2gray
from skimage import img_as_float
from numpy import fft


def finder(f: np.ndarray, s: np.ndarray):
    f = rgb2gray(img_as_float(f))
    s = rgb2gray(img_as_float(s))

    f -= np.mean(f)
    s -= np.mean(s)

    r, c = f.shape
    rp, cp = s.shape
    pattern = np.zeros((r, c))
    pattern[:rp, :cp] = s

    corr = np.absolute(fft.ifft2(np.multiply(fft.fft2(f),
                                             np.conj(fft.fft2(pattern)))))
    return np.unravel_index(corr.argmax(), corr.shape)
