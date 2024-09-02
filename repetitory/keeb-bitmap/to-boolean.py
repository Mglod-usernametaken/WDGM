from PIL import Image
import numpy as np

obrazek = Image.open("keyboard.png")
print("tryb: ", obrazek.mode)
print("format: ", obrazek.format)
print("rozmiar: ", obrazek.size)

tablica = np.asarray(obrazek)
h, w, d = tablica.shape
output = np.zeros((h, w), dtype=uint8)

for i in range(h):
    for j in range(w):
        sum = tablica[i, j, 0] + tablica[i, j, 1] + tablica[i, j, 2]
        if sum > 120:
            output[i, j] = 255

img_out = Image.fromarray(output, mode="L")
img_out = img_out.convert('1')
img_out.save("boolean-keeb.png")
