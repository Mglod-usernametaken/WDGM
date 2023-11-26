from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math

shrimp = Image.open("shrimp.jpg")
mg = Image.open("inicjaly.bmp")

def zakres(w, h):
    return[(i, j) for i in range(w) for j in range(h)]

#-------------------------------------------------------------------
def wstaw_inicjaly(obrazek, inicjal, m, n, r, g, b):
    obraz = obrazek.load()
    ini = np.asarray(inicjal)
    w, h  = obrazek.size
    hi, wi = inicjal.size
    
    for i, j in zakres(wi, hi):
        if 0 == ini[i,j]:
            obraz[j+m,i+n] = (r, g, b)
    obrazek.show()
    return obraz




#-------------------------------------------------------------------
#-------------------------------------------------------------------
wstaw_inicjaly(shrimp, mg, 100,100,255,0,255)

