# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 17:28:56 2025

@author: Lenovo
"""
inicio = 'F−G−G'

   
palabra = 'F−G−G'
nuevo = ""
   
for letra in palabra: 
    if letra == "F":
        nuevo = nuevo + 'F−G+F+G−F'
        
    elif letra == "G":
        nuevo = nuevo + "GG"
        
    else :
        nuevo = nuevo + letra

print(nuevo)

import turtle
theta = 120
for x in nuevo:
    if x == 'F' or x == 'G':
        turtle.forward(30)
    elif x == '-':
        turtle.right(theta)
    else:
        turtle.left(theta)

        


        
    
        



