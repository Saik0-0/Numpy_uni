import numpy as np
from PIL import Image


def motley_crew(files):
    images_arr = [[np.array(Image.open(file), dtype=np.uint8) for file in row] for row in files]

    stack_rows_images = [np.hstack(row) for row in images_arr]
    result = np.vstack(stack_rows_images)

    Image.fromarray(result).save('res.png')
