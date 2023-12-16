from PIL import Image, ImageFilter, ImageChops
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import math

shrimp = Image.open("shrimp.jpg")

# shrimp_blur = shrimp.filter(ImageFilter.BLUR)
# shrimp_blur.show()
# shrimp_blur.save("shrimp_bl.png")

# print(ImageFilter.BLUR.filterargs)
# ((5, 5), 16, 0, (1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1))
# shrimp_kernel_blur = shrimp.filter(ImageFilter.Kernel(size=(5,5), scale=16, offset=0, kernel=(1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1)))
# shrimp_kernel_blur.show()
# shrimp_kernel_blur.save("shrimp_k_bl.png")
# shrimp_diff = ImageChops.difference(shrimp_blur, shrimp_kernel_blur)
# shrimp_diff.show()
# shrimp_diff.save("shrimp_diff.png")

# plt.figure(figsize=(32, 16))
# plt.subplot(1,3,1)
# plt.title("blur")
# plt.imshow(shrimp_blur)
# plt.axis('off')
# plt.subplot(1,3,2)
# plt.title("kernel_blur")
# plt.imshow(shrimp_kernel_blur)
# plt.axis('off')
# plt.subplot(1,3, 3)
# plt.title("rożnica")
# plt.imshow(shrimp_diff)
# plt.axis('off')
# plt.subplots_adjust(wspace=0.05, hspace=0.05)
# plt.savefig("fig1.png")
# plt.show()
