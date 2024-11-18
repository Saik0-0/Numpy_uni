import numpy as np
from PIL import Image


def waves(file):
    image = np.array(Image.open(file), dtype=np.uint8)
    fon = image[0, 0]
    height, width, _ = image.shape

    new_fon_1_r = np.linspace(fon[0], 255, height // 2, dtype=np.uint8)
    new_fon_1_g = np.linspace(fon[1], 255, height // 2, dtype=np.uint8)
    new_fon_1_b = np.linspace(fon[2], 255, height // 2, dtype=np.uint8)

    new_fon_1_r = np.tile(new_fon_1_r[:, np.newaxis], (1, width))
    new_fon_1_g = np.tile(new_fon_1_g[:, np.newaxis], (1, width))
    new_fon_1_b = np.tile(new_fon_1_b[:, np.newaxis], (1, width))

    new_fon_1 = np.stack([new_fon_1_r, new_fon_1_g, new_fon_1_b], axis=-1)
    new_fon_2 = np.flipud(new_fon_1)
    image[:height // 2, ...] = np.where(image[: height // 2, ...] == fon, new_fon_1, image[: height // 2, ...])
    image[height // 2:, ...] = np.where(image[height // 2:, ...] == fon, new_fon_2, image[height // 2:, ...])

    Image.fromarray(image).save('fairy.png')


waves('img_2.png')

