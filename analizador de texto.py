# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 01:38:52 2020

@author: n3ko
"""
from string import ascii_lowercase, ascii_uppercase

x = input(" inserte su texto aqui: \n")

#variables globales
list = []
count =0

# fuciones de analisis de texto -----------------------------------#

def listando():
    count = 0
    for c in x.split(" "):
        count +=1
        list.append(c)
    return(list)

#cuenta los espacios en el texto
def count_space():
    l = 0
    for c in str(x):
        if c == " ":            
            l += 1
        else:
            continue
    return l

#cuenta la frecuencia de cada letra
def frecuencia(text, char):
    count =  0
    for c in text:
        if c == char and c != " ":
            count += 1
        else:
            continue
    return count

def frecuencia_total():
    diccio = {}
    for c in x:
        m = frecuencia(x, c)
        if m != 0:
            diccio[c] = m
        else:
            continue
    return diccio

# conteo letras mayusculas y minusculas
def Mmtamano():
    Count = 0
    count = 0
    for c in x:
        if c in ascii_lowercase:
            count += 1
        elif c in ascii_uppercase:
            Count += 1
        else:
            continue
    return count, Count

#ejecuciones
diccio = frecuencia_total()

    
# Vista
    
listando(), print(" la primera palabra es {}".format(list[0]))
print("hay ", count_space(), "espacios en el texto analizado" )
for c in diccio.keys():
    count = 0
    if c != " ":
        print("la palabra", c, "se repite", diccio.get(c, c))
    else: 
        continue
lista = Mmtamano()
print("hay ", lista[0],"minusculas y ", lista[1], "Mayusculas", "en el texto")

