# _*_ coding:utf8 _*_

#########################
# PROGRAMME DE DESSIN ###
# AUTEUR : DIOUFYFIRE1 ##
#########################


##########################################
# IMPORTATION DES FONCTIONS EXTERNES

from tkinter import *
from random import randrange

##########################################
# DEFINITION LOCALE DE FONCTION


def cercle(x, y, r, coul='grey'):
    "Tracé d'un cercle de centre (x,y) et de rayon r"
    can.create_oval(x-r, y-r, x+r, y+r, outline=coul,fill='grey')

def carreBlack(x1, y1, x2, y2):
    "Tracé d'un carre de couleur noire"
    can.create_rectangle(x1, y1, x2, y2, fill='black')

def carreWhite(x1, y1, x2, y2):
    "Tracé d'un carre de couleur blanc"
    can.create_rectangle(x1, y1, x2, y2, fill='white')

def traceDamier():
    "Dessiner un damier"
    # destroys the canvas and therefore all of its child-widgets too
    can.delete(ALL)

    x1, y1, x2, y2 = 0, 0, 20, 20
    i = 0
    b = 0
    while i < 200:
        while b < 5:
            alterne = i / 20
            if alterne % 2:
                carreBlack(x1, y1, x2, y2)
                carreWhite(x1+20, y1, x2+40, y2)
            else:
                carreWhite(x1, y1, x2, y2)
                carreBlack(x1+20, y1, x2+40, y2)
            b +=1
            x1, x2 = x1+40, x2+40
        i += 20
        b = 0
        x1, y1, x2, y2 = 0, i, 20, i+20


def trace_pion():
    "Placement de pion aleatoirement sur le damier"
    x = randrange(10,200,20)  # generation aleatoire en 9 et 199 en etapes de 20
    y = randrange(10, 200, 20)
    cercle(x,y+1,4)



##########################################
# CORPS PRINCIPAL

# creation du widget principal ("maitre")
fen = Tk()
# creation des widgets esclaves
can = Canvas(fen, bg='dark orange', height=199, width=199)
can.pack(side=TOP, padx=20, pady=20)
b1 = Button(fen, text='Damier', command=traceDamier)
b1.pack(side=LEFT, padx=3, pady=3)
b2 = Button(fen, text='Pion', command=trace_pion)
b2.pack(side=RIGHT, padx=3, pady=3)

fen.mainloop()
