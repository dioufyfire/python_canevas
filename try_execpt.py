#coding:utf-8

"""
type d'exception :  ValueError
                    NameError
                    TypeError
                    ZeroDivisionError
                    OSError
                    AssertionError

"""

age = input ("quel age as tu? ")

try:
    age_caste = int (age)
except
    print("age incorrecte")
else: ##optionnel
    print("age rennseigne est ", age_caste, " ans")
finally: ##optionnel
    print("dans tous les cas, Fin du programme")

#### plusieurs execptions------

nombre1 = 150
nombre2 = input ("quel age as tu? ")

try:
    print("Resultat = {}".format( nombre1 / nombre2))
except ZeroDivisionError:
    print("Vous ne pouvez pas divisier par Zéro")
except ValueError:
    print("Vous ne pouvez pas taper de texte")
except:
    print("Valeur incorrect")