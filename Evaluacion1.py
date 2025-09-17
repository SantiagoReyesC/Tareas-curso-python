# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 23:54:32 2025

@author: Lenovo
"""

'''
A partir del siguiente codigo, generar 50 círculos aleatorios en la región [-100, 100]x[-100, 100]. 
Cuyos radios varian entre 10 a 20 unidades y color varia en {‘red’, ‘blue’, ‘green’, ‘black’}.
'''
import turtle as t
import random as rn

def rand_color():
   colores = ["red", "blue", "green", "black"]
   return rn.choice(colores)
   

def til_circle(angle):
    for i in range(int(360/angle)):
        t.pensize(2)
        t.speed('fastest')
        t.color(rand_color())
        t.circle(rn.randint(10,20))
        t.setheading(t.heading() + angle)
       
til_circle(7.2)

