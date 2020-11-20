# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 01:38:52 2020

@author: n3ko
"""
from string import ascii_lowercase, ascii_uppercase


#global variable
list = []
count =0

# logical funtions -----------------------------------#

def listando():
    for c in x.split(" "): 
        list.append(c)
    return(list)


#funtion for caesa code. Encode and decode.
# jump is the number of jump in the alphabet(not 0 or negative number)
# dec is boolean for decode or encode
diccio = {}
diccioinvert = {}

def funcion_diccio():
    for c, n in zip(ascii_lowercase, range(1, 27)):
        diccio[c] = n
        diccioinvert[n] = c


def caesar_code(text, dec, jump=6):
    texte = ""
    for c in text.lower():
        if c in ascii_lowercase and dec == False and jump >= 1:
               num = diccio.get(c)
               num += jump
               while num > 26:
                     num -= 26
               texte += diccioinvert.get(num)
        elif c in ascii_lowercase and dec == True and jump >= 1:
            num = diccio.get(c)
            num -= jump
            while num <= 0:
                  num += 26
            texte += diccioinvert.get(num)
        else:
            texte = "error"
    return texte



#count the space in the text
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


x = input(" inserte su texto aqui: \n")
    
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
