# _*_ coding:utf8 _*_

#########################
# PROGRAMME DE TEST #####
# AUTEUR : DIOUFYFIRE1 ##
#########################


##########################################
# IMPORTATION DES FONCTIONS EXTERNES

from tkinter import *

##########################################
# DEFINITION LOCALE DE FONCTION


##########################################
# CORPS PRINCIPAL

# creation du widget principal ("maitre")
fen1 = Tk()
# creation des widgets esclaves
txt1 = Label(fen1, text ='Premier champ :')
txt2 = Label(fen1, text='Second :')
txt3 = Label(fen1, text='Trosième :')
entr1 = Entry(fen1)
entr2 = Entry(fen1)
entr3 = Entry(fen1)

can1 = Canvas(fen1, bg='grey', height=1000, width=1000)
photo = PhotoImage(file='/Users/a741103/Documents/ONEDRIVE/OneDrive - Atos/OPS/python/learning/canvas1.gif')
item = can1.create_image(500, 500, image =photo)


txt1.grid(row=1, sticky=E)
txt2.grid(row=2, sticky=E)
txt3.grid(row=3, sticky=E)
entr1.grid(row=1, column=2)
entr2.grid(row=2, column=2)
entr3.grid(row=3, column=2)

can1.grid(row=1, column=3, rowspan=3, padx=10, pady=5)

fen1.mainloop()

