from PIL import Image, ImageFilter, ImageChops, ImageOps
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

#--------------------------------------------------

# shlimp = shrimp.convert('L')
# shlimp_emboss = shlimp.filter(ImageFilter.EMBOSS)
# # shlimp_emboss.show()
# print(ImageFilter.EMBOSS.filterargs)
# 
# ImageFilter.EMBOSS.filterargs = ((3,3), 1, 128, (-1, 0, 1, -2, 0, 2, -1, 0, 1))
# shlimp_sobel1 = shlimp.filter(ImageFilter.EMBOSS)
# # shlimp_sobel1.show()
# 
# ImageFilter.EMBOSS.filterargs = ((3,3), 1, 128, (-1, -2, -1, 0, 0, 0, 1, 2, 1))
# shlimp_sobel2 = shlimp.filter(ImageFilter.EMBOSS)
# shlimp_sobel2.show()
# 
# plt.figure(figsize=(32, 16))
# plt.subplot(2,2,1)
# plt.title("tryb L")
# plt.imshow(shlimp)
# plt.axis('off')
# plt.subplot(2,2,2)
# plt.title("Emboss")
# plt.imshow(shlimp_emboss)
# plt.axis('off')
# plt.subplot(2,2, 3)
# plt.title("sobel1")
# plt.imshow(shlimp_sobel1)
# plt.subplot(2,2, 4)
# plt.title("sobel2")
# plt.imshow(shlimp_sobel2)
# plt.axis('off')
# plt.subplots_adjust(wspace=0.05, hspace=0.05)
# plt.savefig("fig2.png")

#--------------------------------------------------

# shrimp_detail = shrimp.filter(ImageFilter.DETAIL)
# detail_diff = ImageChops.difference(shrimp, shrimp_detail)
# 
# shrimp_edge = shrimp.filter(ImageFilter.EDGE_ENHANCE_MORE)
# edge_diff = ImageChops.difference(shrimp, shrimp_edge)
# 
# shrimp_sharpen = shrimp.filter(ImageFilter.SHARPEN)
# sharpen_diff = ImageChops.difference(shrimp, shrimp_sharpen)
# 
# shrimp_smooth = shrimp.filter(ImageFilter.SMOOTH_MORE)
# smooth_diff = ImageChops.difference(shrimp, shrimp_smooth)
# 
# plt.figure(figsize=(32, 16))
# plt.subplot(4,2,1)
# plt.title("DETAIL")
# plt.imshow(shrimp_detail)
# plt.axis('off')
# plt.subplot(4,2,2)
# plt.title("DETAIL diff")
# plt.imshow(detail_diff)
# plt.axis('off')
# plt.subplot(4,2,3)
# plt.title("EDGE_ENHANCE_MORE")
# plt.imshow(shrimp_edge)
# plt.axis('off')
# plt.subplot(4,2,4)
# plt.title("EDGE_ENHANCE_MORE diff")
# plt.imshow(edge_diff)
# plt.axis('off')
# plt.subplot(4,2,5)
# plt.title("SHARPEN")
# plt.imshow(shrimp_sharpen)
# plt.axis('off')
# plt.subplot(4,2,6)
# plt.title("SHARPEN diff")
# plt.imshow(sharpen_diff)
# plt.axis('off')
# plt.subplot(4,2,7)
# plt.title("SMOOTH_MORE")
# plt.imshow(shrimp_smooth)
# plt.axis('off')
# plt.subplot(4,2,8)
# plt.title("SMOOTH_MOREdiff")
# plt.imshow(smooth_diff)
# plt.axis('off')
# plt.subplots_adjust(wspace=0.05, hspace=0.15)
# plt.savefig("fig3.png")
# plt.show()

#--------------------------------------------------
# zadanie 4
#--------------------------------------------------


toof = Image.open("zeby.png")
print(toof.mode)
teef = toof.convert('L')
teef.show()
teefqualized = ImageOps.equalize(teef, mask = None)
teefqualized.show() 
teefqualized.save("equalized.png")

#--------------------------------------------------

teef_detail = teef.filter(ImageFilter.DETAIL)
teef_sharpen = teef.filter(ImageFilter.SHARPEN)
teef_contour = teef.filter(ImageFilter.CONTOUR)

plt.title("zeby format L")
plt.imshow(teef)
plt.axis('off')
plt.subplot(2,3,1)
plt.title("zeby_equalized")
plt.imshow(teefqualized)
plt.axis('off')
plt.subplot(2,3,2)
plt.title("DETAIL")
plt.imshow(teef_detail)
plt.axis('off')
plt.subplot(2,3,3)
plt.title("SHARPEN")
plt.imshow(teef_sharpen)
plt.axis('off')
plt.subplot(2,3,4)
plt.title("CONTOUR")
plt.imshow(teef_contour)
plt.axis('off')
plt.subplot(2,3,5)
plt.subplots_adjust(wspace=0.05, hspace=0.15)
plt.savefig("fig3.png")
plt.show()



