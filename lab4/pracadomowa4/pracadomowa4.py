from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from random import randint

#----------------------------------------------------
def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

#----------------------------------------------------
def zlicz_roznice_srednia_RGB(obraz, wsp): # wsp - współczynnik określający dokładność oceny
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
                if np.mean(t_obraz[i, j, :]) > wsp:    
                    zlicz = zlicz + 1 
    procent = zlicz/(h*w)
    return zlicz, procent

#----------------------------------------------------
def zlicz_roznice_suma_RGB(obraz, wsp): # wsp - współczynnik określający dokładność oceny
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
                if sum(t_obraz[i, j, :]) > wsp: # poniżej równoważne sformułowania tego warunku
                # if (t_obraz[i, j, 0] + t_obraz[i, j, 1] + t_obraz[i, j, 2]) > wsp:
                # if t_obraz[i, j, 0] > wsp or  t_obraz[i, j, 1] > wsp or t_obraz[i, j, 2] > wsp: 
                    zlicz = zlicz + 1 
    procent = zlicz/(h*w)
    return zlicz, procent

#----------------------------------------------------
def generuj_histogram(im):
    hist = im.histogram()
    p = 0
    print(hist[p])
    print(hist[256 + p])
    print(hist[2*256 + p])
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.show()
    #plt.savefig("histogram1.png")

#----------------------------------------------------
def odkoduj(im1,im2):
    t_1 = np.asarray(im1)
    t_2 = np.asarray(im2)
    h, w, d = t_1.shape
    secret = np.zeros((h,w), dtype=np.uint8)
    # for i,j in h,w 
    # sumuj r+g+b w t_1 i t_2
    # diff umieść w secret[i,j]
    for i in range(h):
        for j in range(w):
            t1 = int(t_1[i,j,0]+t_1[i,j,1]+t_1[i,j,2])
            t2 = int(t_2[i,j,0]+t_2[i,j,1]+t_2[i,j,2])
            secret[i,j] = t2-t1
    sec_img = Image.fromarray(secret)
    sec_img.show()

#----------------------------------------------------
# im3jpg = Image.open("im3.jpg")
# im3png = Image.open("im3.png")
# 
# diff_3 = ImageChops.difference(im3png,im3jpg)
# diff_3.show()
# diff_3.save("diff.png")

diff = Image.open("diff.png")
statystyki(diff)

# generuj_histogram(diff)
# #generuj_histogram(im3jpg)
# 
# zlicz, procent = zlicz_roznice_srednia_RGB(diff, 5)
# print('liczba niepasujących pikseli = ' , zlicz)
# print('procent niepasujących pikseli = ' , procent)
# 
# zlicz, procent = zlicz_roznice_suma_RGB(diff, 5)
# print('liczba niepasujących pikseli = ' , zlicz)
# print('procent niepasujących pikseli = ' , procent)
# 


obraz = Image.open("shrimp.jpg")
obraz.save("obraz1.jpg")
obraz1 = Image.open("obraz1.jpg")
obraz.save("obraz2.jpg")
obraz2 = Image.open("obraz2.jpg")
obraz.save("obraz3.jpg")
obraz3 = Image.open("obraz3.jpg")
obraz.save("obraz4.jpg")
obraz4 = Image.open("obraz4.jpg")
obraz.save("obraz5.jpg")
obraz5 = Image.open("obraz5.jpg")

# obraz5.show()
#diff5 = ImageChops.difference(obraz, obraz5)
# diff5.show()
#generuj_histogram(diff5)
#ststystyki(diff5)

zakodowany1 = Image.open("zakodowany1.bmp")
zakodowany2 = Image.open("zakodowany2.bmp")
odkoduj(zakodowany1, zakodowany2)


