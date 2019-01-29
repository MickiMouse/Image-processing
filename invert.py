import numpy as np


def invert(image):
    max_intensiy = 255

    height = image.shape[0]
    weight = image.shape[1]
    canals = image.shape[2]

    for c in np.arange(canals):
        for i in np.arange(height):
            for j in np.arange(weight):
                image[i, j, c] = max_intensiy - image[i, j, c]

    return image
