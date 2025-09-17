# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 20:47:07 2025

@author: Lenovo
"""

decimal = int("1024")

if decimal == 0:
    print("El número binario es: 0")
    
else:
    binario = ""  
    numero = decimal

    while numero > 0:
        residuo = numero%2          
        binario = str(residuo) + binario  
        numero = numero // 2          

print("El número " + str(decimal) + " en binario es:" + str(binario))

# %%

# Conversión de número binario a decimal usando while

binario = "110101"

decimal = 0    
posicion = 0   


i = len(binario) -1

while i >= 0:
    bit = binario[i]        
    if bit == '1':           
        decimal += 2 ** posicion
    elif bit != '0':
        print("Número binario inválido")
        exit()

    posicion += 1            
    i -= 1                   

print("El número " + binario + " en decimal es: " + str(decimal))