# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 01:38:52 2020

@author: n3ko
"""
from string import ascii_lowercase, ascii_uppercase, ascii_letters
from tkinter import filedialog, Tk, Frame, Button, Label, Text, Scrollbar, Checkbutton, IntVar, Entry, StringVar

#test new branch
# View

raiz = Tk()
raiz.title(" analizador de texto S.T.A.E")
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
viewframe.config(bg = "brown")
viewframe.pack(side = "right")

#global variable

result="hola"
#switches
switchart=IntVar()
switchmayus=IntVar()
switchdec=IntVar()
jumpnump = StringVar()
# logical funtion

def openfile():
    try:
        global temp1
        temp1 = filedialog.askopenfilename(title = "abrir", initialdir="C:\\")
        global file1
        x = open(temp1, "r")
        file1 = x.read()
        x.close()
    except:
        print("archivo no seleccionado")
    

#funtion for caesa code. Encode and decode.
# jump is the number of jump in the alphabet(not 0 or negative number)
# dec is boolean for decode or encode
diccio = {}
diccioinvert = {}

def funcion_diccio():
    for c, n in zip(ascii_lowercase, range(1, 27)):
        diccio[c] = n
        diccioinvert[n] = c

def cypher_dec():
    try:
        if switchdec.get() == 1:
            x = jumpnump.get()
            x = int(x)
            resultcypher = caesar_code(file1, 1, x)
            new = open(temp1 + "cypher", "w")
            new.write(resultcypher)
           #visual change
            visualstadistic.config(state = "normal")
            visualstadistic.delete(1.0, "end")
            visualstadistic.insert("insert", "texto sin cifrar \n")
            visualstadistic.insert("insert", file1 + "\n \n")
            visualstadistic.insert("insert", "texto cifrado \n")
            visualstadistic.insert("insert", resultcypher + "\n")
            visualstadistic.config(state = "disabled")
            new.close()
        else: 
            x = jumpnump.get()
            x = int(x)
            resultcypher = caesar_code(file1, 0, x)
            new = open(temp1 + "decypher", "w")
            new.write(resultcypher)
            #visual change
            visualstadistic.config(state = "normal")
            visualstadistic.delete(1.0, "end")
            visualstadistic.insert("insert", "texto cifrado \n")
            visualstadistic.insert("insert", file1 + "\n \n")
            visualstadistic.insert("insert", "texto descifrado \n")
            visualstadistic.insert("insert", resultcypher)
            visualstadistic.config(state = "disabled")
            new.close()
    except:
        print("error cypher text")
        x = jumpnump.get()
        x = int(x)
        print(x)
        print(type(x))

def caesar_code(text, dec, jump=6):
    funcion_diccio()
    texte = ""
    for c in text.lower():
        if dec == 1 and jump >= 1 and c != " " and c in ascii_letters:
            num = diccio.get(c)
            num = num + jump
            while num > 26:
                num -= 26
            texte += diccioinvert.get(num)
        elif dec == 0 and jump >= 1 and c != " " and c in ascii_letters:
            num = diccio.get(c)
            num = num - jump
            while num <= 0:
                num += 26
            texte += diccioinvert.get(num)
        elif c == " " or c not in ascii_letters:
            texte += c
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
    
    try:
        if file1 == None:
            raise ImportError
        else:    
            visualstadistic.config(state = "normal")
            visualstadistic.delete(1.0, "end")
            diccio = frecuencia_total()
            lista = Mmtamano()
            space = count_space()
            if space <= 1:
                l = "hay: {0} espacio \n".format(space)
            else:
                l = "hay: {0} espacios \n".format(space)
            visualstadistic.insert("insert", l)
            if switchmayus.get() == 1:
                l = "hay: {0} minusculas y {1} Mayusculas \n".format(lista[0], lista[1])
                visualstadistic.insert("insert", l)
            else:
                pass
            if switchart.get() == 1:
                for c in diccio:
                    l = "{0} se repite {1} veces \n".format(c, diccio[c])
                    visualstadistic.insert("insert", l)
            else:
                pass
            visualstadistic.config(state = "disabled")
    except:
        visualstadistic.config(state = "normal")
        visualstadistic.delete(1.0, "end")
        visualstadistic.insert("insert", "ningun archivo seleccionado")
        visualstadistic.config(state = "disabled")


#labels in View
welcomelabel = Label(pframe, text = "Welcome to S.T.A.E created by @N3kosempai", fg = "black", font =("Arial", 12), bg = "gray")
welcomelabel.place(x = 30, y = 20)

Label(pframe, text = "number of jump in cypher", fg = "black", font =("Arial",10), bg = "gray").place(x = 230, y = 300)

Button (pframe, text = "select file", command = openfile).place(x = 150, y = 50)

Checkbutton(pframe, text = "Contar caracteres", variable = switchart, onvalue = 1, offvalue = 0).place(x = 30, y = 380)
Checkbutton(pframe, text = "Contar May & min", variable = switchmayus, onvalue = 1, offvalue = 0).place(x = 30, y = 350)
Checkbutton(pframe, text = "cypher or decypher", variable = switchdec, onvalue = 1, offvalue = 0).place(x = 240, y = 380) 

Button(pframe, text = "analize", command = star_analize).place(x = 65,y = 420)
#cypher
jumpentry = Entry(pframe, textvariable = jumpnump, justify = "center").place(x = 240, y = 325)

Button(pframe, text = "cypher", command = cypher_dec).place(x = 280, y = 420)

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
try:
    del globals()["file1"]
except:
    print("error en el borrado de variable")