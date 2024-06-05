#Libraray in pyhton

#1. Math library
import math as mt
print(mt.cos(45))
print(mt.cbrt(8))
print(mt.sqrt(256))
print(mt.log10)

#2. Random Library
import random as rd
x = [1,2,3,4,5,6,7,8,9]
print(rd.random()*100)
print(rd.randint(0,1000))
rd.shuffle(x)
print(x)

#3. functools
import functools as ft
print(ft.reduce(lambda x,y:x*y,x))

#4. itertools

import itertools as it
print(dict(it.permutations(range(3),2)))
