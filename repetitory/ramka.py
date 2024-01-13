from PIL import Image
import numpy as np


w = 500
h = 300
obraz = np.zeros((h,w))
for i in range(5,h-5):
    for j in range(5,w-5):
        obraz [i,j] = 1

obraz = obraz.astype(np.bool_)
obraz = Image.fromarray(obraz)
obraz.show()
obraz.save("ramka.bmp")

