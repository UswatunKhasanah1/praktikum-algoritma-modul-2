# -- coding: utf-8 --
"""
Created on Tue Sep 28 18:10:25 2022

@author: Uswatun Khasanah
"""
import math
t1 = float(input("latitude kota Jakarta Pusat"))
f1 = float(input("longitude kota Jakarta Pusat"))

t2 = float(input("latitude kota Bandung"))
f2 = float(input("longitude kota Bandung"))

dlat = t2 - t1
dlon = f2 - f1

x = math.sin(math.radians(dlat/2)) * 2 + math.cos(math.radians(t1)) * math.cos(math.radians(t2)) * math.sin(math.radians(dlon/2)) * 2

b = 2 * math.asin(math.sqrt(x))

r = 6371.01

print ('\njarak antara dua titik adalah', b*r , 'km')