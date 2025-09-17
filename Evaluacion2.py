# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 01:12:01 2025

@author: Lenovo
"""

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [1.23, 2.13, 1.42, -0.69, 4.29, 3.64, 9.30, 10.62, 7.42, 8.40, 12.30, 10.30]
#media de x
sumx = 0
sumy = 0
for i in x:
    sumx = sumx + i
medx = sumx/len(x)
#media de y
for j in y:
    sumy = sumy + j
medy = sumy/len(y)


v = len(x)

nxy = v*medx*medy 

sumarriba = 0
for i in range(v):
    sumarriba = sumarriba + x[i]*y[i]

sumx2 = 0
for i in range(v):
    sumx2 = sumx2 + x[i]**2
    
sumx1 = 0 
for i in range(v):
    sumx1 = sumx1 + x[i]

B1 = (sumarriba-nxy)/(sumx2-(sumx1)**2/v) 

B0 = medy - (B1*medx)

print(B1)
print(B0)
