import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from skimage.io import imread, imshow
from fft_finder import finder

if __name__ == "__main__":
    first_img = imread('cat.jpg')
    second_img = imread('eye_left.jpg')
    third_img = imread('eye.jpg')

    y, x = finder(first_img, second_img)
    y2, x2 = finder(first_img, third_img)
    ry, cy, canals = second_img.shape
    ry2, cy2, canals2 = third_img.shape

    plt.imshow(first_img)
    plt.show()

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(second_img)
    ax2.imshow(third_img)
    plt.show()

    fig2, ax = plt.subplots(1)
    imshow(first_img)
    rect = Rectangle((x, y), width=cy, height=ry, edgecolor="r", linewidth=1, facecolor='none')
    rect2 = Rectangle((x2, y2), width=cy2, height=ry2, edgecolor="r", linewidth=1, facecolor='none')
    ax.add_patch(rect)
    ax.add_patch(rect2)
    plt.show()
