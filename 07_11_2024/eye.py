import numpy as np
from PIL import Image


def eye(coord, *colors, fon=(0, 0, 0)):
    image = np.full((300, 400, 3), fon, dtype=np.uint8)

    x_grid, y_grid = np.meshgrid(np.arange(400), np.arange(300))
    distances = np.abs(x_grid - coord[1]) + np.abs(y_grid - coord[0])

    n = len(colors)
    for color in colors[::-1]:
        image[distances < n * 20] = color
        n -= 1

    Image.fromarray(image).save('eye.png')


eye((150, 200),
    (255, 0, 0), (0, 255, 0),
    (0, 0, 255), (255, 255, 255))