import numpy as np
from PIL import Image


def transition(file1, file2):
    image1 = np.array(Image.open(file1))
    image2 = np.array(Image.open(file2))
    h, w, _ = image1.shape

    image_res = np.zeros(image1.shape)

    image_res[:, :w // 3, :] = image1[:, :w // 3, :]
    image_res[:, 2 * w // 3:, :] = image2[:, 2 * w // 3:, :]
    temp = np.array([np.linspace(99, 1, w // 3) / 100]).reshape((w // 3, 1))
    coefficients = np.hstack((temp, temp, temp))
    image_res[:, w // 3:2 * w // 3, :] = (image1[:, w // 3:2 * w // 3, :] * coefficients +
                                          image2[:, w // 3:2 * w // 3, :] * (1 - coefficients))

    Image.fromarray(image_res.astype(np.uint8)).save("pic.png")


transition(1, 2)
