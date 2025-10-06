# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 22:32:13 2025

@author: Lenovo
"""
#FIGURA 1

import matplotlib.pyplot as plt
import numpy as np

def rota(x=0, teta=0):
  rota = np.array([[np.cos(teta), -np.sin(teta)], [np.sin(teta), np.cos(teta)]])
  prod = np.dot(rota,x)
  return prod
    
t = np.arange(-6, 6, 0.0001)
x = 2.5*((np.sin(-5*t))**2)*(2**(np.cos(np.cos(4.28*(2.3*t)))))
y = 2.5*((np.sin(np.sin(-5*t))))*(np.cos(4.28*2.3*t)**2)
    
xy = np.array([x, y]).transpose()

xyn = np.array([rota(point, np.pi/2) for point in xy])

xynn = np.array([rota(point, np.pi/2) for point in xyn])

xynnn = np.array([rota(point, np.pi/2) for point in xynn])

plt.plot(xy[:, 0], xy[:, 1], 'r-')

plt.plot(xyn[:, 0], xyn[:, 1], 'r-')

plt.plot(xynn[:, 0], xynn[:, 1], 'r-')

plt.plot(xynnn[:, 0], xynnn[:, 1], 'r-')

plt.show()
plt.close()

plt.show()

#%%

#FIGURA 2

import matplotlib.pyplot as plt
import numpy as np

def rota(x=0, teta=0):
  rota = np.array([[np.cos(teta), -np.sin(teta)], [np.sin(teta), np.cos(teta)]])
  prod = np.dot(rota,x)
  return prod

t = np.arange(-3, 3, 0.00001)
x = 7*((np.sin(7.32*t))/(1+(np.cos(1.42*t))**2))
y = 7*np.cos(1.42*t)*((np.sin(7.32*t))**4)

xy = np.array([x, y]).transpose()

xyn = np.array([rota(point, np.pi/2) for point in xy])

xynn = np.array([rota(point, np.pi/2) for point in xyn])

xynnn = np.array([rota(point, np.pi/2) for point in xynn])

plt.plot(xy[:, 0], xy[:, 1], 'r-')

plt.plot(xyn[:, 0], xyn[:, 1], 'b-')

plt.plot(xynn[:, 0], xynn[:, 1], 'g-')

plt.plot(xynnn[:, 0], xynnn[:, 1], 'y-')

plt.show()
plt.close()

plt.show()