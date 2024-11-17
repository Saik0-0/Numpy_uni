import numpy as np
from PIL import Image


def fly_catcher(file):
    image = np.array(Image.open(file), dtype=np.uint8)
    fon = image[0, 0]

    rows, cols = np.nonzero(np.all(image != fon, axis=-1))
    result = image[rows.min(): rows.max() + 1, cols.min(): cols.max() + 1]

    Image.fromarray(result.astype(np.uint8)).save('fly.png')

fly_catcher('img.png')