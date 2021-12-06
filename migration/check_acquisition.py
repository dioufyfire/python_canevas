# _*_ coding:utf8 _*_

############################
# PROGRAMME DE TEST ########
# AUTEUR : DIOUFYFIRE1 #####
# COMPATIBILITY : VER 3.0 ##
############################


##########################################
# IMPORTATION DES FONCTIONS EXTERNES

import sys, os
import configparser # TRAITEMENT FICHIER DE CONFIGURATION
from elasticsearch import Elasticsearch
from datetime import date, datetime,  timedelta


##########################################
# DEFINITION LOCALE DE FONCTION



##########################################
# CORPS PRINCIPAL

# Arguments passed checking
####
try:
    f = open(sys.argv[1])
    f.close()
except FileNotFoundError:
    print('File does not exist')
    exit()

print("\nConfig filename:", sys.argv[1],"\n")

# Reading parameters in file
####
file_container = configparser.ConfigParser(inline_comment_prefixes=";")
file_container.read(sys.argv[1])
flux = file_container.get('section_1', 'flux')
ipelastic = file_container.get('section_1', 'ipelastic')
index = file_container.get('section_1', 'index')

# Variables definition
now = datetime.now() - timedelta(hours=10)
d4 = now.strftime("%Y%m%d%H")  # %H:%M:%S
timestamp = datetime.timestamp(now)
print("timestamp =", timestamp)
print("now =", now)
print("d4 =", d4)
dossier = '*' + flux + '_' + d4
print(dossier)
print("FLUX ON CHECK : ", flux)

# Check folder with Elastic
####
urlElastic = "http://" + ipelastic + ":9200"
es = Elasticsearch([urlElastic])
query_body = {
    "query": {
        "wildcard": {
            "absolute.hdfs.path": {
                "value": dossier
                }
            }
        }
    }
#res = es.search(index="log_dlk", body=query_body)
#print(res)
res = es.count(index="log_dlk", body=query_body)
print(res['count'])
