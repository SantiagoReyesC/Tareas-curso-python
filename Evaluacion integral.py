# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 17:39:41 2025

@author: Lenovo
"""

'''
Calcular la integral siguiente en el intervalo [-1,3].
'''
def fun(x):
    return 2-((x-2)**2)
  
a = -1
b = 3
nint = 1000  
delx = (b-a)/nint


integral = 0 
x = a
for _ in range(nint):
    
    integral = integral + delx*fun(x)
    x = x + delx
    
print(integral)

