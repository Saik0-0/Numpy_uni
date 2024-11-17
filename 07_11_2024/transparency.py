from PIL import Image
import numpy as np


def transparency(image_path, rect):
    image = Image.open(image_path)
    image_arr = np.array(image, dtype=np.uint8)

    x1, y1, x2, y2 = rect

    window = image_arr[y1:y2, x1:x2]
    height, width = window.shape[:2]

    alpha_layer = np.linspace(255, 0, width, dtype=np.uint8)
    alpha_layer = np.tile(alpha_layer, (height, 1))

    window[..., 3] = alpha_layer

    image_arr[y1:y2, x1:x2] = window
    Image.fromarray(image_arr).save('window.png')


