from PIL import Image
import numpy as np
import math


obrazek = Image.open ("inicjaly.bmp")

#----------------------------------------------------------
def rysuj_ramke(obraz, grub):
    tab_obrazu = np.asarray(obraz)
    h, w = tab_obrazu.shape

    tab1 = np.zeros((h,w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if i in range(0,grub):
                tab1[i,j] = 0
            elif i in range(h-grub, h):
                tab1[i,j] = 0

            elif j in range(0,grub):
                tab1[i,j] = 0
            elif j in range(w-grub, w):
                tab1[i,j] = 0
            else: 
                tab1[i,j] = tab_obrazu[i,j]

    tab2 = tab1.astype(np.bool_)
    tab_show = Image.fromarray(tab2)
    return tab_show

#----------------------------------------------------------
def rysuj_same_ramki(h, w, grub):
    tab1 = np.ones((h,w), dtype=np.uint8)
    for x in range(0,h,2*grub):
        for i in range(x,h-x):
            for j in range(x,w-x):
                if i in range(x,grub+x):
                    tab1[i,j] = 0
                elif i in range(h-grub-x, h-x):
                    tab1[i,j] = 0

                elif j in range(x,grub+x):
                    tab1[i,j] = 0
                elif j in range(w-grub-x, w-x):
                    tab1[i,j] = 0

    tab2 = tab1.astype(np.bool_)
    tab_show = Image.fromarray(tab2)
    return tab_show

#----------------------------------------------------------
def rysuj_pionowe(h,w, grub):
    tab1 = np.ones((h,w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if j%(2*grub) >= grub:
                tab1[i,j] = 0

    tab2 = tab1.astype(np.bool_)
    tab_show = Image.fromarray(tab2)
    return tab_show

#----------------------------------------------------------
def wypelnij_dopunktu(h,w,m,n):
    tab1 = np.ones((h,w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if (i<m and j<n):
                tab1[i,j] = 0
            elif (i>m and j>n):
                tab1[i,j] = 0

    tab2 = tab1.astype(np.bool_)
    tab_show = Image.fromarray(tab2)
    return tab_show

#----------------------------------------------------------
#funkcja pokoloruj_odleglosciami tworzy koncentryczne gradienty 
#rozchodzace sie od punktu (n,m).
#ich gestosc mozemy regulowac parametrem gestosc

def pokoloruj_odleglosciami(h,w,m,n, gestosc=1):
    tab1 = np.ones((h,w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab1[i,j] = (math.sqrt((i-n)**2 + (j-m)**2)%gestosc)

    tab2 = tab1.astype(np.bool_)
    tab_show = Image.fromarray(tab2)
    return tab_show

#----------------------------------------------------------

#
#ramka = rysuj_ramke(obrazek, 5)
#ramka.save("ramka_5.bmp")
#
#ramka = rysuj_ramke(obrazek, 10)
#ramka.save("ramka_10.bmp")
#
#ramka = rysuj_same_ramki(320,480,10)
#ramka.save("obraz1.bmp")
#
#ramka = rysuj_pionowe(320,480,10)
#ramka.save("obraz2.bmp")
#
#ramka = wypelnij_dopunktu(320,480,100,50)
#ramka.save("obraz3.bmp")
#
#funkcja pokoloruj_odleglosciami tworzy koncentryczne gradienty 
#rozchodzace sie od punktu (m,n).
#ich gestosc mozemy regulowac parametrem gestosc

ramka = pokoloruj_odleglosciami(320,480,100,50,10) 
ramka.save("obraz4.bmp")
ramka.show()
