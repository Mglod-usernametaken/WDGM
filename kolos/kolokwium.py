from PIL import Image, ImageOps,ImageChops,ImageFilter


import numpy as np
import matplotlib.pyplot as plt


print ("start")
obraz = Image.open("obr/obraz9.jpg")
# obr = obraz.convert("L")

def gethisto(im, name):
    plt.clf()
    hist = im.histogram()
    p=0
    print(hist[p])
    plt.bar(range(256),hist[:])
    plt.savefig(f"{name}.png")

ycbr = obraz.convert("YCbCr")
a,b,c = obraz.split()
#b.show()
w,h = b.size

im = np.asarray(b)
count = 0
for i in range(h):
    for j in range(w):
        if (im[i,j] == 120):
            count +=1

print(count)

