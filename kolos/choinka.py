from PIL import Image, ImageOps,ImageChops,ImageFilter, ImageDraw, ImageFont
import textwrap
import numpy as np
import matplotlib.pyplot as plt


print ("start")
obraz = Image.open("obr/obraz1.jpg")
w,h = obraz.size
mask = Image.new("L",(w,h),"black")
draw = ImageDraw.Draw(mask)
points = [(0,int(h/2)),(int(w/2),0),(w,int(h/2)),(int(w/2),h)]

draw.polygon(points, fill="white")

mask.save("mask.bmp")
mas = Image.open("mask.bmp")
wd = Image.open("obr/WD1.jpg")

obraz.paste(wd,(0,0),mas)
obraz.show()
