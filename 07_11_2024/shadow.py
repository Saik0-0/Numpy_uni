import numpy as np
from PIL import Image


def shadow(file, n, p=10):
    image = np.array(Image.open(file))
    fon = image[0, 0]

    result = np.where(image != fon, image * (1 + p / 100), image)
    result = result.astype(np.uint8)

    result = np.roll(np.roll(result, n, axis=0), n, axis=1)

    result = np.where(image == fon, result, image)
    Image.fromarray(result).save('shift.png')


shadow('img.png', 20, p=15)