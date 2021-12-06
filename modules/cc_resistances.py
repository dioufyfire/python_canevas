# _*_ coding:utf8 _*_

############################
# PROGRAMME DE TEST ########
# AUTEUR : DIOUFYFIRE1 #####
# COMPATIBILITY : VER 3.0 ##
############################

##########################################
# DEFINITION DES CLASSES

class Application(object):
    def __init__(self):
        """Constructeur de la fenêtre principale"""
        self.root =Tk()
        self.root.title('Code des couleurs')
        self.dessineResistance()
        Label(self.root, text="Entrez la valeur de la résistance, en ohms :").grid(row=2, column=1, columnspan=3)
        Button(self.root, text = 'Montrer', command =self.changeCouleurs).grid(row =3, column =1)
        Button(self.root, text ='Quitter', command =self.root.quit).grid(row =3, column =3)
        self.entree = Entry(self.root, width =14)
        self.entree.grid(row =3, column =2)
        # Code des couleurs pour les valeurs de zéro à neuf :
        self.cc = ['black', 'brown', 'red', 'orange', 'yellow',
                'green', 'blue', 'purple', 'grey', 'white']
        self.root.mainloop()

    def dessineResistance(self):
        """Cannevas avec un modèle de résistances trois lignes colorées"""
        self.can = Canvas(self.root, width=250, height =100, bg ='ivory')
        self.can.grid(row =1, column =1, columnspan =3, pady =5, padx =5)
        self.can.create_line(10, 50, 240, 50, width=5)    # fils
        self.can.create_rectangle(85, 30, 185, 70, fill='light grey', width=2)
        # Dessin des trois lignes colorées (noires au départ)
        self.ligne = []
        for x in range(90, 155, 24):
            "on memorisera les trois Lignes dans 1 liste"
            self.ligne.append(self.can.create_rectangle(x, 30, x+12, 70, fill='black', width=0))

    def changeCouleurs(self):
        """Affichage des couleurs correspondant à la valeur entrée"""
        self.vich = self.entree.get()    # cette methode renvoie une chaine
        try:
            v=float(self.vich)  # conversion en valeur numérique
        except:
            err=1     # erreur : entrée non numérique
        else:
            err=0

        if err==1 or v < 10 or v > 1e11:
            self.signaleErreur()    # entrée incorrecte ou hors limites
        else:
            li=[0]*3      # liste des 3 codes à afficher, initialiser à zéro
            logv=int(log10(v))        # partie entiere du logarithme
            ordgr=10**logv         # ordre de grandeur
            # extraction du premier chiffre significatif
            li[0] = int(v/ordgr)         # partie entière
            decim = v/ordgr - li[0]         # partie décimale
            # extraction du second chiffre significatif
            li[1] = int(decim*10 + .5)  # +.5 pour arrondir correctement
            # nombre de zéros à accoler aux 2 chiffres significatifs :
            li[2] = logv - 1
            # Coloration des 3 lignes :
            for n in range(3):
                self.can.itemconfigure(self.ligne[n], fill=self.cc[li[n]])

    def signaleErreur(self):
        self.entree.configure(bg='red')
        self.root.after(1000, self.videEntree)

    def videEntree(self):
        self.entree.configure(bg='white')       # colorer le fond du champ
        self.entree. delete(o, len(self.vich))          # après 1 seconde, effacer

                # rétablir le fond blanc
        # enlever les car. présents
### Programme principal:
if __name__ == "__main__":

    ##########################################
    # IMPORTATION DES FONCTIONS EXTERNES

    from math import log10      # logarithmes en base 10
    from tkinter import *

    f=Application()       # instanciation de l'objet application

