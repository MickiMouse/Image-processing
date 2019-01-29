import numpy as np


def threshold(img, border):
    height = img.shape[0]
    weight = img.shape[1]
    canals = img.shape[2]

    for c in np.arange(canals):
        for i in np.arange(height):
            for j in np.arange(weight):
                if img[i, j, c] > border:
                    img[i, j, c] = 255
                else:
                    img[i, j, c] = 0
    return img
