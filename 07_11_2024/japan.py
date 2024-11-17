import numpy as np
from PIL import Image


arr1 = np.array(Image.open(input()))
arr2 = np.array(Image.open(input()))

h, w, _ = arr1.shape
y, x, _ = arr2.shape

fon_arr1 = arr1[0, w - 1]
fon_arr2 = arr2[0, 0]

temp = np.where(arr2 == fon_arr2, fon_arr1, arr2)

arr1[:y, w - x:, ...] = temp

Image.fromarray(arr1.astype(np.uint8)).save('ready.png')
