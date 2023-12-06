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
def filtruj_inicjaly(obrazek, inicjal, m, n, factor):
    obraz = obrazek.load()
    ini = np.asarray(inicjal)
    w, h  = obrazek.size
    hi, wi = inicjal.size
    
    for i, j in zakres(wi, hi):
        if 0 == ini[i,j]:
            (r,g,b) = obraz[j+m,i+n]
            r = int(255* np.log(1+(r/factor)))
            g = int(255* np.log(1+(g/factor)))
            b = int(255* np.log(1+(b/factor)))
          #  r = 255 
          #  g = 255 
          #  b = 255 
            obraz[j+m,i+n] = (r,g,b)
    obrazek.show()
    return obrazek

#-------------------------------------------------------------------
def transformacja_logarytmiczna(obrazek):
    obraz = obrazek.load()
    w,h = obrazek.size
    for i,j in zakres(w,h):
        for k in obraz[i,j]:
            k = 255* np.log(1+k/255)

#-------------------------------------------------------------------
def rysuj_kwadrat_srednia(obraz, m,n,k):
    if 0 == k%2:
        print("nieprawidłowa wartość K w rysuj_kwadrat_srednia. pomijam.")
        return 1
    obrazek = obraz.load()
    zakres = int((k-1)/2)
    print("zakres = ",zakres)
    red = green = blue = 255
    print("green = ",green)
    
    for i in range (m-zakres, m+zakres):
        for j in range (n-zakres, n+zakres):
            (r,g,b) = obrazek[i, j]
            if red > r:
                red = r
            if green > g:
                green = g
            if blue > b:
                blue = b

    for i in range (m-zakres, m+zakres):
        for j in range (n-zakres, n+zakres):
            obrazek[i,j] = (red,green,blue)
    print("red = ",red)
    print("green = ",green)
    print("blue = ",blue)
    obraz.show()
    return obraz

#-------------------------------------------------------------------

#-------------------------------------------------------------------


# obrazek1 = wstaw_inicjaly(shrimp, mg,1820,1230, 255,0,255)
# obrazek1.save("obraz1.png")
# obrazek2 = filtruj_inicjaly(shrimp, mg,200,200, 255)
# obrazek2.save("obraz2.png")
# obrazek2 = filtruj_inicjaly(shrimp, mg,200,200, 125)
# obrazek2.save("obraz2-enhanced.png")
obrazek3 = rysuj_kwadrat_srednia(shrimp, 200,200,51)
obrazek31 = rysuj_kwadrat_srednia(obrazek3, 369,69,21)
obrazek32 = rysuj_kwadrat_srednia(obrazek31, 575,75,77)
obrazek32.save("obraz3.png")
