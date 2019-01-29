import numpy as np


def contrast(img, n, min_, max_):
    height = img.shape[0]
    weight = img.shape[1]
    canals = img.shape[2]

    img_ = img * n

    for c in np.arange(canals):
        for h in np.arange(height):
            for w in np.arange(weight):
                if img_[h, w, c] <= min_:
                    img_[h, w, c] = min_
                elif img_[h, w, c] >= max_:
                    img_[h, w, c] = max_
    return img_
