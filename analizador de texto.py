# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 01:38:52 2020

@author: n3ko
"""


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
        

# Vista
    
listando(), print(" la primera palabra es {}".format(list[0]))
print("hay ", count_space(), "espacios en el texto analizado" )
print(x)