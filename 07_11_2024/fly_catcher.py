import numpy as np
from PIL import Image


def fly_catcher(file):
    image = np.array(Image.open(file), dtype=np.uint8)
    fon = image[0, 0]

    image_2 = np.argwhere((image != fon).any(axis=-1))
    y_min, x_min = image_2.min(axis=0)
    y_max, x_max = image_2.max(axis=0)

    result = image[y_min:y_max + 1, x_min:x_max + 1]

    Image.fromarray(result.astype(np.uint8)).save('fly.png')


fly_catcher('img.png')