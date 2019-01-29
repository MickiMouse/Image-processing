import matplotlib.pyplot as plt
from simple_contrast import contrast
from fft_for_image import fft_vs_noise
from threshold import threshold
from invert import invert
from skimage.io import imread, imshow
from skimage import img_as_float
import warnings

warnings.filterwarnings('ignore')

if __name__ == "__main__":
    img = imread('train.jpg')
    img = img_as_float(img)

    f, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow((img - 0.2) * 2)
    ax2.imshow(contrast(img - 0.2, 2, 0, 1))
    plt.show()

    img = imread('plane.jpg')
    imshow(img)
    imshow(invert(img))
    plt.show()

    img = imread('forest.jpg')
    imshow(img)
    imshow(threshold(img, 50))
    plt.show()

    img = plt.imread('img_with_noise.jpg')

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(img)
    ax2.imshow(fft_vs_noise(img))
    plt.show()
