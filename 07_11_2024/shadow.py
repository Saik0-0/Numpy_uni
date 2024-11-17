import numpy as np
from PIL import Image


def shadow(file, n, p=10):
    image = np.array(Image.open("C:/Users/alexa/OneDrive/Рабочий стол/cat.png"))
    fon = image[0, 0]
    shadow = np.where(image != fon, np.round(image * (1 + p / 100)), fon)
    shadow = shadow.astype(np.uint8)
    shadow[:, n:] = shadow[:, :-n]
    shadow[:, :n] = np.full((image.shape[0], n, 3), fon, dtype=image.dtype)
    shadow[n:, :] = shadow[:-n, :]
    shadow[:n, :] = np.full((n, image.shape[1], 3), fon, dtype=image.dtype)
    res = np.where(image == fon, shadow, image)
    Image.fromarray(res).save('C:/Users/alexa/OneDrive/Рабочий стол/result.png')


shadow(0, 20, 15)
