from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math

shrimp = Image.open("shrimp_small.jpg")
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
def filtruj_inicjaly(obrazek, inicjal, m, n):
    obraz = obrazek.load()
    ini = np.asarray(inicjal)
    w, h  = obrazek.size
    hi, wi = inicjal.size
    
    for i, j in zakres(wi, hi):
        if 0 == ini[i,j]:
            (r,g,b) = obraz[j+m,i+n]
            r = int(255* np.log(1+(r/255)))
            g = int(255* np.log(1+(g/255)))
            b = int(255* np.log(1+(b/255)))
          #  r = 255 
          #  g = 255 
          #  b = 255 
            obraz[j+m,i+n] = (r,g,b)
    obrazek.show()
    return obraz
#-------------------------------------------------------------------
def transformacja_logarytmiczna(obrazek):
    obraz = obrazek.load()
    w,h = obrazek.size
    for i,j in zakres(w,h):
        for k in obraz[i,j]:
            k = 255* np.log(1+k/255)
#-------------------------------------------------------------------
# obrazek1 = wstaw_inicjaly(shrimp, mg,1820,1230, 255,0,255)
# obrazek1.save("obraz1.png")
obrazek2 = filtruj_inicjaly(shrimp, mg,200,200)
obrazek2.save("obraz2.png")
