# _*_ coding:utf8 _*_

#########################
# PROGRAMME DE DESSIN ###
# AUTEUR : DIOUFYFIRE1 ##
#########################


##########################################
# IMPORTATION DES FONCTIONS EXTERNES

from tkinter import *

##########################################
# DEFINITION LOCALE DE FONCTION

def cercle(x, y, r, coul='black'):
    "Tracé d'un cercle de centre (x,y) et de rayon r"
    can.create_oval(x-r, y-r, x+r, y+r, outline=coul)

def figure_1():
    "Dessiner une cible"
    # destroys the canvas and therefore all of its child-widgets too
    can.delete(ALL)
    # tracer les lignes horizontale et verticale
    can.create_line(100, 0, 100, 200, fill ='blue')
    can.create_line(0, 100, 200, 100, fill='blue')
    # tracer plusieurs cercles concentriques
    rayon = 15
    while rayon < 100:
        cercle(100, 100, rayon)
        rayon += 15

def figure_2():
    "Dessiner un visage simplifié"
    # destroys the canvas and therefore all of its child-widgets too
    can.delete(ALL)
    # Les caractéristiques de chaque cercle sont
    # placées das une liste de listes :
    cc = [[100, 100, 80, 'red'],     # visage
          [70, 70, 15, 'blue'],      # yeux
          [130, 70, 15, 'blue'],
          [70, 70, 5, 'black'],
          [130, 70, 5, 'black'],
          [44, 115, 20, 'red'],      # joues
          [156, 115, 20, 'red'],
          [100, 95, 15, 'purple'],   # nez
          [100, 145, 30, 'purple']]  # bouche

    # on trace tous les cercles à l'aide d'une boucle :
    i = 0
    while i < len(cc):               # parcours de la liste
        el = cc[i]
        cercle(el[0], el[1], el[2], el[3])
        i += 1

##########################################
# CORPS PRINCIPAL

# creation du widget principal ("maitre")
fen = Tk()
# creation des widgets esclaves
can = Canvas(fen, bg='dark orange', height=200, width=200)
can.pack(side=TOP, padx=20, pady=20)
b1 = Button(fen, text='Dessin 1', command=figure_1)
b1.pack(side=LEFT, padx=3, pady=3)
b2 = Button(fen, text='Dessin 2', command=figure_2)
b2.pack(side=RIGHT, padx=3, pady=3)

fen.mainloop()
