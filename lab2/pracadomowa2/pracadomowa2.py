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
#funkcja rysuj_kola tworzy okregi 
#rozchodzace sie od punktu (n,m).
#ich gestosc mozemy regulowac parametrem grubosc

def rysuj_kola(h,w,m,n, grubosc):
    tab1 = np.ones((h,w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab1[i,j] = math.sqrt((i-n)**2 + (j-m)**2)%grubosc

    tab2 = tab1.astype(np.bool_)
    tab_show = Image.fromarray(tab2)
    return tab_show

#----------------------------------------------------------
# funkcja rysuj_kola_l tworzy koncentryczne gradienty 
# rozchodzace sie od punktu (n,m).
# ich gestosc mozemy regulowac parametrem gestosc

def rysuj_kola_l(h,w,m,n, gestosc=1):
    tab1 = np.ones((h,w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab1[i,j] = (math.sqrt((i-n)**2 + (j-m)**2)*gestosc)%256

    tab_show = Image.fromarray(tab1)
    return tab_show

#----------------------------------------------------------
def negatyw(obrazek):
    tab1 = np.asarray(obrazek)
    h,w = tab1.shape
    tab2 = np.zeros((h,w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab2[i,j] = 255 - tab1[i,j]
    
    tab_show = Image.fromarray(tab2)
    return tab_show

#----------------------------------------------------------
# funkcja rysuje pionowe linie
# białe linie są gradientem przez całą wysoność obrazka

def rysuj_pionowe_l(h,w, grub):
    tab1 = np.ones((h,w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if j%(2*grub) >= grub:
                tab1[i,j] = i*256/h 

    tab_show = Image.fromarray(tab1)
    return tab_show

#----------------------------------------------------------
def negatyw_rgb(obrazek):
    tab1 = np.asarray(obrazek)
    h,w,t = tab1.shape
    tab2 = np.zeros((h,w,t), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab2[i,j,0] = 255 - tab1[i,j,0]
            tab2[i,j,1] = 255 - tab1[i,j,1]
            tab2[i,j,2] = 255 - tab1[i,j,2]
    
    tab_show = Image.fromarray(tab2)
    return tab_show

#----------------------------------------------------------
def kolorowe_inicjaly(obraz,grub):
    tab_obrazu = np.asarray(obraz)
    h, w = tab_obrazu.shape
    
    tab1 = np.zeros((h,w,3), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if (tab_obrazu[i,j] == 0):
                if i%(2*grub) <= grub: 
                    tab1[i,j,0] = 128
                    tab1[i,j,1] = 0
                    tab1[i,j,2] = 128
                else:
                    tab1[i,j,0] = 90
                    tab1[i,j,1] = 255
                    tab1[i,j,2] = 32
            else:
                tab1[i,j,:] = 255
    tab_show = Image.fromarray(tab1)
    return tab_show

#----------------------------------------------------------
# funkcja rysuje kolorowe pionowe pasy o szerokości grub
# kolor zmienia sięnastępująco:
# R po wysokości od 0 do 255
# G po wysokości od 255 do 0
# B po serokości od 0 do 255

def rysuj_pionowe_rgb(h,w, grub):
    tab1 = np.ones((h,w,3), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if j%(2*grub) >= grub:
                tab1[i,j,0] = i*256/h 
                tab1[i,j,1] = 255-(i*256/h)
                tab1[i,j,2] = j*256/w 

    tab_show = Image.fromarray(tab1)
    return tab_show

#----------------------------------------------------------
def rysuj_kola_rgb(h,w,m,n, gestosc=1):
    tab1 = np.ones((h,w,3), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab1[i,j,0] = (math.sqrt((i-n)**2 + (j-m)**2)*gestosc)%256
            tab1[i,j,1] = (i*256)/h
            tab1[i,j,2] = (j*256)/w

    tab_show = Image.fromarray(tab1)
    return tab_show


#----------------------------------------------------------
#ramka = rysuj_ramke(obrazek, 5)
#ramka.save("ramka_5.bmp")
#
#ramka = rysuj_ramke(obrazek, 10)
#ramka.save("ramka_10.bmp")
#
#ramka = rysuj_same_ramki(320,480,16)
#ramka.save("obraz1.bmp")
#
#ramka = rysuj_pionowe(320,480,10)
#ramka.save("obraz2.bmp")
#
#ramka = wypelnij_dopunktu(320,480,100,50)
#ramka.save("obraz3.bmp")
#
## funkcja rysuj_kola tworzy okregi 
## rozchodzace sie od punktu (m,n).
## ich gestosc mozemy regulowac parametrem grubosc
#
#ramka = rysuj_kola(320,480,100,50,44) 
#ramka.save("obraz4.bmp")
#
#ramka = rysuj_kola_l(320,480,100,250,3) 
#ramka.save("obraz4_2.bmp")
#
#ramka = negatyw(ramka)
#ramka.save("obraz4_2N.bmp")
#
## funkcja rysuje pionowe linie
## białe linie są gradientem przez całą wysoność obrazka
#
#ramka = rysuj_pionowe_l(320,480,10)
#ramka.save("obraz2_2.bmp")
#
#ramka = negatyw(ramka)
#ramka.save("obraz2_2N.bmp")
#
#ramka = rysuj_kola_rgb(320,480, 100,200)
#ramka.save("obraz4_2.png")
#ramka.save("obraz4_2.jpg")
#
#ramka = rysuj_kola_rgb(320,480, 100,200)
#ramka = negatyw_rgb(ramka)
#ramka.save("obraz4_2N.png")
#ramka.save("obraz4_2N.jpg")
#
#ramka = rysuj_pionowe_rgb(320,480, 10)
#ramka.save("obraz2_2.png")
#ramka.save("obraz2_2.jpg")
#
#ramka = rysuj_pionowe_rgb(320,480, 10)
#ramka = negatyw_rgb(ramka)
#ramka.save("obraz2_2N.png")
#ramka.save("obraz2_2N.jpg")
#

ramka = kolorowe_inicjaly(obrazek, 10)
ramka.save("obraz3.png")
ramka.save("obraz3.jpg")

ramka.show()


