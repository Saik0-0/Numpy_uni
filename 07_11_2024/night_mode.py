from PIL import Image
import numpy as np


image = np.array(Image.open(input()))

red, green, blue = image[..., 0], image[..., 1], image[..., 2]
rgb = red.sum() + green.sum() + blue.sum()
coef_r = red.sum() / rgb
coef_g = green.sum() / rgb
coef_b = blue.sum() / rgb

result = (red * coef_r + green * coef_g + blue * coef_b).astype(np.uint8)
result = Image.fromarray(result)

result.save("night_mode.png")
