from PIL import Image  # Python Imaging Library
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt
import math

#------------------------------------------------------------
def rysuj_kola(h,w,m,n, gestosc=1):
    tab1 = np.ones((h,w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab1[i,j] = (math.sqrt((i-n)**2 + (j-m)**2)*gestosc)%256

    tab_show = Image.fromarray(tab1)
    return tab_show

#------------------------------------------------------------

def rysuj_pionowe(h,w, grub):
    tab1 = np.ones((h,w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if j%(2*grub) >= grub:
                tab1[i,j] = i*256/h

    tab_show = Image.fromarray(tab1)
    return tab_show

#------------------------------------------------------------

im1 = Image.open("shrimp.jpg")  # wczytywanie obrazu
# im1.show()
print("tryb", im1.mode)
print("format", im1.format)
print("rozmiar", im1.size)

w = 1920
h = 1280
im_tab = np.asarray(im1)

#------------------------------------------------------------

T = np.array(im1)
t_r = T[:, :, 0]
im_r =  Image.fromarray(t_r)
# im_r.show()
# im_r.save("im_r.jpg")

t_g = T[:, :, 1]
im_g =  Image.fromarray(t_g)
# im_g.show()
# im_g.save("im_g.jpg")

t_b = T[:, :, 2]
im_b =  Image.fromarray(t_b)
# im_b.show()
# im_b.save("im_b.jpg")

#------------------------------------------------------------

im_merg1 = Image.merge('RGB', (im_r, im_g, im_b))

r, g, b = im1.split()
# r.show()
# g.show()
# b.show()
# 
# im_merg2 = Image.merge('RGB',(r,g,b))
# 
# diff_im = ImageChops.difference(im_merg2,im_merg1)
# # diff_im.show()
# 
# im_3 = Image.merge('RGB',(g,b,r))
# # im_3.show()
# im_3.save("im3.jpg")
# im_3.save("im3.png")
# 
# im3jpg = Image.open("im3.jpg")
# im3png = Image.open("im3.png")
# 
# diff_3 = ImageChops.difference(im3png,im3jpg)
# #dif_3.show()
# #------------------------------------------------------------
# plt.figure(figsize=(32, 16))
# plt.subplot(2,2,1) 
# plt.imshow(im_merg1)
# plt.axis('off')
# plt.subplot(2,2,2)
# plt.imshow(im_merg2, "gray")
# plt.axis('off')
# plt.subplot(2,2,3)
# plt.imshow(diff_im, "gray")
# plt.axis('off')
# plt.subplots_adjust(wspace=0.05, hspace=0.05)
# #plt.savefig('fig1.png')
# #plt.show()
# 
# 
# #------------------------------------------------------------
# 
# plt.figure(figsize=(32, 16))
# plt.subplot(2,2,1) 
# plt.imshow(im3jpg)
# plt.axis('off')
# plt.subplot(2,2,2)
# plt.imshow(im3png, "gray")
# plt.axis('off')
# plt.subplot(2,2,3)
# plt.imshow(diff_3, "gray")
# plt.axis('off')
# plt.subplots_adjust(wspace=0.05, hspace=0.05)
# plt.savefig('fig2.png')
# #plt.show()
# #------------------------------------------------------------
# 
# 
# 
# kola = rysuj_kola(1280,1920, 1200,300)
# paski = rysuj_pionowe(1280,1920, 100)
# #im_r im_g im_b - tablice poszczególnych kolorów
# im_4_1 = Image.merge('RGB', (kola, im_g, im_b))
# im_4_2 = Image.merge('RGB', (im_r, im_g, paski))
# im_4_3 = Image.merge('RGB', (paski, kola, im_g))
# 
# 
# plt.figure(figsize=(32, 16))
# plt.subplot(2,2,1) 
# plt.imshow(im_4_1)
# plt.axis('off')
# plt.subplot(2,2,2)
# plt.imshow(im_4_2, "gray")
# plt.axis('off')
# plt.subplot(2,2,3)
# plt.imshow(im_4_3, "gray")
# plt.axis('off')
# plt.subplots_adjust(wspace=0.05, hspace=0.05)
# plt.savefig('fig3.png')
# #plt.show()
# 
# #------------------------------------------------------------
# 


kwadrat = Image.open("kwadrat.png")  
kwadrat = kwadrat.convert("L")
kwadrat_tab = np.asarray(kwadrat)
trojkat = Image.open("trojkat.png")  
trojkat = trojkat.convert("L")
trojkat_tab = np.asarray(trojkat)
kolo = Image.open("kolo.png")  
kolo = kolo.convert("L")
kolo_tab = np.asarray(kolo)

print("tryb", kolo.mode)
print("format", kolo.format)
print("rozmiar", kolo.size)
w,h =kolo.size
im51= Image.merge('RGB', (kwadrat, trojkat, kolo))
im52= Image.merge('RGB', (kwadrat, kolo, trojkat))
im54= Image.merge('RGB', (trojkat, kwadrat, kolo))
im53= Image.merge('RGB', (trojkat, kolo, kwadrat))
im55= Image.merge('RGB', (kolo, kwadrat, trojkat))
im56= Image.merge('RGB', (kolo, trojkat, kwadrat))


plt.figure(figsize=(32, 16))

plt.subplot(2,3,1) 
plt.imshow(im51)
plt.axis('off')
plt.subplot(2,3,2) 
plt.imshow(im52)
plt.axis('off')
plt.subplot(2,3,3) 
plt.imshow(im53)
plt.axis('off')
plt.subplot(2,3,4) 
plt.imshow(im54)
plt.axis('off')
plt.subplot(2,3,5) 
plt.imshow(im55)
plt.axis('off')
plt.subplot(2,3,6) 
plt.imshow(im56)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig4.png')
plt.show()


