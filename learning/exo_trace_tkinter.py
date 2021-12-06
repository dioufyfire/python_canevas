# _*_ coding:utf8 _*_

#########################
# PROGRAMME DE TEST #####
# AUTEUR : DIOUFYFIRE1 ##
#########################


##########################################
# IMPORTATION DES FONCTIONS EXTERNES

from tkinter import *
from random import randrange

##########################################
# DEFINITION LOCALE DE FONCTION

def drawline():
    "Tracé d'une ligne dans le canevas can1"
    global x1, x2, y1, y2, coul
    can1.create_line(x1,y1,x2,y2,width=2,fill=coul)
    y2, y1 = y2+10, y1-10  # decalage de chaque coté pour formé un tour



def changecolor():
    "Changement aleatoire de couleur du tracé"
    global coul
    pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
    c = randrange(8)                  #generation aleatoire en 0 et 7
    coul = pal[c]


def resetAll():
    can1.delete('all')  # destroys the canvas and therefore all of its child-widgets too
    global x1, x2, y1, y2
    x1, x2, y1, y2 = 20, 160, 160, 20

##########################################
# CORPS PRINCIPAL

x1, x2, y1, y2 = 20, 160, 160, 20   #coordonnnees de ligne
coul = 'dark green'
# creation du widget principal ("maitre")
fen1 = Tk()
# creation des widgets esclaves
can1 = Canvas(fen1, bg='dark grey', height=200, width=200)
can1.pack(side=LEFT)
bou1 = Button(fen1, text='Quitter', command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text='Tracer une ligne', command=drawline)
bou2.pack()
bou3 = Button(fen1, text='Autre couleur', command=changecolor)
bou3.pack()
bou4 = Button(fen1, text='Effacer', command=resetAll)
bou4.pack()

fen1.mainloop()

fen1.destroy()
