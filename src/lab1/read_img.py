import numpy as np
import PIL
from PIL import Image

img = Image.open("resources/whu.png")
rgb = img.convert("RGB")
rgb.save("whu3.png")
grey = rgb.convert("L")
grey.save("grey.png")
binary_img = rgb.convert("1")
binary_img.save("bin.png")

# def func(pix):
#     breakpoint()
#     print(pix)
#     return 0
# tmp = rgb.point(func)
breakpoint()