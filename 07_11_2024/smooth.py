from PIL import Image
import numpy as np


def smooth(cort1, cort2):
    image = np.zeros((200, 200, 3), dtype=np.uint8)

    image_color_r = np.linspace(cort1[0], cort2[0], 200, dtype=np.uint8)
    image_color_g = np.linspace(cort1[1], cort2[1], 200, dtype=np.uint8)
    image_color_b = np.linspace(cort1[2], cort2[2], 200, dtype=np.uint8)

    image[..., 0] = np.tile(image_color_r, (200, 1))
    image[..., 1] = np.tile(image_color_g, (200, 1))
    image[..., 2] = np.tile(image_color_b, (200, 1))

    Image.fromarray(image).save('gradient.png')




smooth((249, 82, 188), (162, 170, 253))
