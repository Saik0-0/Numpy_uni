import numpy as np
from PIL import Image


def cool(file, mode=0):
    image = np.array(Image.open(file), dtype=np.uint8)
    if mode == 0:
        image = np.hstack((image, np.flip(image, axis=1)))
    elif mode == 1:
        image = np.hstack((np.flip(image, axis=1), image))
    elif mode == 2:
        image = np.vstack((np.flip(image, axis=0), image))
    elif mode == 3:
        image = np.vstack((image, np.flip(image, axis=0)))

    Image.fromarray(image).save('res.png')


cool('img.png', mode=3)