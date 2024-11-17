import numpy as np
from PIL import Image


def repair(file):
    image = np.array(Image.open(file))
    fon = image[0, 0]
    image_new = np.where(image != fon, 255 - image, image)
    Image.fromarray(image_new).save('result.png')
