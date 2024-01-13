from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def szary(w,h):
    tab = np.zeros((h,w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i,j] = (3i-j)%256
    return tab

obrazek_1 = Image.open("obraz1.jpg")
tablica = np.asarray(obrazek_1)
h,w,dep = tablica.shape
mac = szary(w,h)
macka = Image.fromarray(mac)
r,g,b = obrazek_1.split()

one = Image.merge('RGB',(macka,g,b))
two = Image.merge('RGB',(r,macka,b))
three = Image.merge('RGB',(r,g,macka))


# one.show()
# two.show()
# three.show()

plt.figure(figsize=(32, 16))
plt.subplot(1,3,1)
plt.imshow(one)
plt.axis('off')
plt.subplot(1,3,2)
plt.imshow(two)
plt.axis('off')
plt.subplot(1,3,3)
plt.imshow(three)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('mix.png')
plt.show()
