import numpy as np
from PIL import Image


def marks(file, size, color, *points):
    image = np.array(Image.open(file), dtype=np.uint8)
    for point in points:
        image[point[1] - size // 2: point[1] + size // 2, point[0] - size // 2: point[0] + size // 2] = color

    Image.fromarray(image).save('points.png')


marks('img.png', 20, (255, 192, 0),
      (200, 100), (300, 250), (50, 380))