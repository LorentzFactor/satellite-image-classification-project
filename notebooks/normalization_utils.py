import numpy as np

def crop_image(img):
    crop = np.argwhere(np.sum(img, axis=2) != 0)
    x_min, x_max = np.min(crop[:, 0]), np.max(crop[:, 0])
    y_min, y_max = np.min(crop[:, 1]), np.max(crop[:, 1])
    return img[x_min:x_max, y_min:y_max]