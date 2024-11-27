import numpy as np
from PIL import Image


def quasars(file, r, m):
    image = np.array(Image.open(file), dtype=np.uint8)
    height, width, _ = image.shape
    result = image.copy()

    for rows in range(height):
        for cols in range(width):
            row_min = max(rows - r, 0)
            row_max = min(rows + r + 1, height)
            col_min = max(cols - r, 0)
            col_max = min(cols + r + 1, width)
            if np.sum(image[row_min:row_max, col_min:col_max]) > m:
                result[row_min:row_max, col_min:col_max] = [255, 0, 0]

    return Image.fromarray(result)
