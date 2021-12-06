# _*_ coding:utf8 _*_

#########################
# PROGRAMME DE DESSIN ###
# AUTEUR : DIOUFYFIRE1 ##
#########################


##########################################
# IMPORTATION DES FONCTIONS EXTERNES

from tkinter import *
from math import *

##########################################
# DEFINITION LOCALE DE FONCTION

# Action à executer lorsque l'utilisateur tape sur "Enter"
def evaluer(event):
    chaine.configure(text = "Résultat = " + str(eval(entree.get())))

##########################################
# CORPS PRINCIPAL

# creation du widget principal ("maitre")
fen = Tk()
# creation des widgets esclaves
entree = Entry(fen,background='grey')
entree.bind("<Return>", evaluer)
chaine = Label(fen)
entree.pack()
chaine.pack()

fen.mainloop()
