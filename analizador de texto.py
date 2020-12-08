# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 01:38:52 2020

@author: n3ko
"""
from string import ascii_lowercase, ascii_uppercase
from tkinter import filedialog, Tk, Frame, Button, Label, Text, Scrollbar

#test new branch
# View

raiz = Tk()
raiz.title(" analizador de texto FILO")
raiz.resizable(False, False)
#raiz.iconbitmap()      ..... pendiente de disenar un icono
raiz.geometry("708x460")
raiz.config(bg = "black")


pframe = Frame()
pframe.pack(side = "left")
pframe.config(bg = "gray")
pframe.config(width = "400", height = "460")

viewframe = Frame()
viewframe.config(width = "300", height = "460",)
viewframe.config(bg = "green")
viewframe.pack(side = "right")

#global variable
list = []
count =0
result="hola"
error = 0
# logical funtion

def openfile():
    try:
        global temp1
        temp1 = filedialog.askopenfilename(title = "abrir", initialdir="C:\\")
        global file1
        x = open(temp1, "r")
        file1 = x.read()
        temp1.close()
    except:
         error = error + 1
    

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
    for c in file1:
        if c == " ":            
            l += 1
        else:
            continue
    return l

#count the frecuency of any letter
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
    for c in file1:
        m = frecuencia(file1, c)
        if m != 0:
            diccio[c] = m
        else:
            continue
    return diccio

# count Mayus and min
def Mmtamano():
    Count = 0
    count = 0
    for c in file1:
        if c in ascii_lowercase:
            count += 1
        elif c in ascii_uppercase:
            Count += 1
        else:
            continue
    return count, Count



# start the analize (call all funtion for analize the text)

def star_analize():
    visualstadistic.config(state = "normal")
    if error == 0:
        diccio = frecuencia_total()
        lista = Mmtamano()
        space = count_space()
        if space <= 1:
            l = "hay: {0} espacio \n".format(space)
        else:
            l = "hay: {0} espacios \n".format(space)
            visualstadistic.insert("insert", l)
        l = "hay: {0} minusculas y {1} Mayusculas \n".format(lista[0], lista[1])
        visualstadistic.insert("insert", l)
        for c in diccio:
            l = "{0} se repite {1} veces \n".format(c, diccio[c])
            visualstadistic.insert("insert", l)
            visualstadistic.config(state = "disabled")
    else:
        visualstadistic.insert("insert", "ERROR")



#labels in View
welcomelabel = Label(pframe, text = "Welcome to Filo text analizer", fg = "black", font =("Arial", 12), bg = "gray")
welcomelabel.place(x = 70, y = 20)



Bselect = Button (pframe, text = "select file", command = openfile).place(x = 170, y = 50)
Banalize = Button (pframe, text = "analize", command = star_analize).place(x = 180,y = 400)


# viewframe ---------------------------------
visualdatalabel = Label(viewframe, text = "view data").place(x = 120, y = 40)
visualstadistic = Text(viewframe, width = 28, height = 20, bg = "black", fg = "green", font = "Arial")
visualstadistic.config(insertbackground = "green", state = "disabled", bd = 1, relief = "raised", wrap = "word")
visualstadistic.place(x = 20, y = 70)



scrollvartvs = Scrollbar(viewframe, command = visualstadistic.yview)
scrollvartvs.place(x = 277, y = 70, height = 160)
visualstadistic.config(yscrollcommand = scrollvartvs.set)


""" ADVERTENCIA REPARAR RECONOCIMIENTO DE / : y . COMO LETRA """
raiz.mainloop()