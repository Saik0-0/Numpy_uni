import numpy as np
from PIL import Image


def colored_squares(*colors_corts, sizes):
    square_size, rows, cols = sizes

    color_indexes = np.arange(rows * cols) % len(colors_corts)
    image = np.array(color_indexes[:cols], dtype=np.uint8)

    for row in range(1, rows):
        image = np.insert(image, image.shape[0], color_indexes[row: row + cols], axis=0)

    image = image.reshape(rows, cols)
    image = np.array(colors_corts, dtype=np.uint8)[image]

    image = np.repeat(image, square_size, axis=0)
    image = np.repeat(image, square_size, axis=1)

    Image.fromarray(image).save('squares.png')


colores = [(249, 82, 188), (244, 159, 255),
           (162, 170, 253), (216, 250, 163), (183, 250, 83)]
colored_squares(*colores, sizes=(20, 5, 7))

