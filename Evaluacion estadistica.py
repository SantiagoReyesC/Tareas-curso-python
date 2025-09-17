# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 16:56:52 2025

@author: Lenovo
"""
#DATOS
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [1.23, 2.13, 1.42, -0.69, 4.29, 3.64, 9.30, 10.62, 7.42, 8.40, 12.30, 10.30]

#MEDIA ARITMETICA

sumx = 0
for i in x:
    sumx = sumx + i
    
medx = sumx/len(x)

print(medx)

#Varianza
sumarriba = 0

for i in x:
    sumarriba = sumarriba + (i-medx)**2

var = sumarriba/(len(x)-1)
print(var)

#desviación std
import math
s = math.sqrt(var)
print(s)


#Medida de asimetria

sumasimetria = 0
for i in x:
    sumasimetria = sumasimetria + (i-medx)**3
    
numerador = sumasimetria/len(x)
sim = numerador/(s**3)
print(sim)

#medida de kurtosis

sumkurt = 0
for i in x:
    sumkurt = sumkurt + (i-medx)**4
    
numkurt = sumkurt/len(x)

kurtosis = (numkurt/(s**4))-3

print(kurtosis)