from PIL import Image
import numpy as np

obrazek = Image.open ("inicjaly.bmp")
print("---------- informacje o obrazie")
print("tryb:", obrazek.mode)
print("format:", obrazek.format)
print("rozmiar:", obrazek.size)

dane_obrazka = np.asarray(obrazek)
print("---------------- informacje o tablicy obrazu----------------")
print("typ danych tablicy:", dane_obrazka.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy:", dane_obrazka.shape)  # rozmiar tablicy - warto porównac z rozmiarami obrazka
print("liczba elementow:", dane_obrazka.size)  # liczba elementów tablicy
print("wymiar tablicy:", dane_obrazka.ndim)  # wymiar mówi czy to jest talica 1D, 2d, 3D ...
print("rozmiar wyrazu tablicy:", dane_obrazka.itemsize)

obraz_zdanych = Image.fromarray(dane_obrazka)
#obraz_zdanych.show()
print("tryb:",obraz_zdanych.mode)
print("format:",obraz_zdanych.format)
print("rozmiar:",obraz_zdanych.size)

dane_obrazka_int = dane_obrazka.astype(np.uint8)

print(dane_obrazka_int)
obraz_zdanych_int = Image.fromarray(dane_obrazka_int * 128)
obraz_zdanych_int.show()
print("obraz jako int:")
print("tryb:",obraz_zdanych_int.mode)
print("format:",obraz_zdanych_int.format)
print("rozmiar:",obraz_zdanych_int.size)
