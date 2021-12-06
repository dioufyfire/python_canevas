# _*_ coding:utf8 _*_

###############################
# COMPILATION DE FONCTION #####
# POUR LA MANIPULATION DES ####
# DES FICHIERS              ###
# AUTEUR : DIOUFYFIRE1 ########
###############################

def filtre(source, destination):
    "recopier un fichier en éliminant les lignes de remarques"
    fs = open(source, 'r')
    fd = open(destination, 'W')
    while 1:
        txt = fs.readline()
        if txt =='':
            break
        if txt[0] != '#':
            fd.write(txt)
    fs.close()
    fd.close()
    return

def existe(fname):
    "Controle de lExistance d'un fichier"
    try:
        f = open(fname, 'r')
        f.close()
        return 1
    except:
        return 0