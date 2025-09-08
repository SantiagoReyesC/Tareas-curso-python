# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 14:51:31 2025

@author: Lenovo
"""

palabra = 'F'
nuevo = ""
   
for letra in (palabra): 
    if letra == "F":
        nuevo = nuevo + 'F+G'
        
    elif letra == "G":
        nuevo = nuevo + "FG"
        
    else :
        nuevo = nuevo + letra
        
nuevo3 = ""       
for i in nuevo2: 
    if i == "F":
        nuevo3 = nuevo3 + 'F+G'
         
    elif i == '+':
        nuevo3 = nuevo3 + i        
         
    else :
        nuevo3 = nuevo3 + "FG"
              

print(nuevo2)

import turtle
theta = 90
for x in nuevo3:
    if x == 'F' or x == 'G':
        turtle.forward(30)
    else:
        turtle.right(theta)
   