import numpy as np
from PIL import Image


def turn(file, angle):
    image = np.array(Image.open(file), dtype=np.uint8)
    image = np.rot90(image, - angle // 90)

    Image.fromarray(image).save('ready.png')


turn('img.png', 270)