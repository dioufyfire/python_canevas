# _*_ coding:utf8 _*_

##########################
# PROGRAMME ALERTINNG ####
# INGESTION JOURNALIER ####
# AUTEUR : DIOUFYFIRE1 ##
#########################


##########################################
# IMPORTATION DES FONCTIONS EXTERNES
import subprocess
import datetime
from datetime import date, datetime,  timedelta
import time
import sys
import os
import configparser  # TRAITEMENT FICHIER DE CONFIGURATION
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
##########################################
# DEFINITION LOCALE DE FONCTION


def current_milli_time():
    return round(time.time() * 1000)


##########################################
# CORPS PRINCIPAL
try:
    f = open(sys.argv[1])
    f.close()
except FileNotFoundError:
    print('File does not exist')
    exit()

print("\nConfig filename:", sys.argv[1], "\n")

sender = "sup_bigdata@orange-sonatel.com"
receiver = "Mamadou.DIOUF2@orange-sonatel.com"
threshold = int(sys.argv[2] * 3600000)
#password = input("Type your password and press enter:")

# Reading parameters in file
####
file_container = configparser.ConfigParser(inline_comment_prefixes="#")

### prepend a fake section header to your config file data
with open(sys.argv[1]) as stream:
    # This line does the trick.
    file_container.read_string("[top]\n" + stream.read())
    FLUX = file_container.get('top', 'FLUX')
    DIR_DLK = file_container.get('top', 'DIR_DLK')
    SUFFIXE = file_container.get('top', 'SUFFIXE')
print("CHECK FLUX : ", FLUX, end="\n")

current_datetime = datetime.now() - timedelta(hours=20)
year = current_datetime.year
month = current_datetime.strftime("%m")
day = current_datetime.strftime("%d")
timestamp_now = current_milli_time()

### HDFS=$(hdfs dfs -ls $DIR_DLK/$flux$SUFFIXE/year=$year_x1/month=$month_x1/day=$date_x1  2>/dev/null | wc -l)
command = "hdfs dfs -test -e " + DIR_DLK + "/" + FLUX + SUFFIXE + "/year=" + \
    str(year) + "/month=" + str(month) + "/day=" + \
    str(year) + str(month) + str(day) + ";echo $?"
command1 = "hdfs dfs -stat \"%Y\" " + DIR_DLK + "/" + FLUX + SUFFIXE + "/year=" + \
    str(year) + "/month=" + str(month) + "/day=" + \
    str(year) + str(month) + str(day) + " | tail -1"
try:
    print("TEST EXISTANCE DOSSIER ", str(year), str(month), str(day))
    p = subprocess.Popen(command,
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
except:
    print("ERREUR SUR LA REQUETE HDFS")
    sys.exit(1)

result_test = int(p.stdout.read())

if result_test == 0:
    try:
        print("CONTROLE DE LA DATE DU DOSSIER ",
              str(year), str(month), str(day))
        q = subprocess.Popen(command1,
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
    except:
        print("ERREUR SUR LA REQUETE HDFS")
        sys.exit(1)

result_test1 = q.stdout.read().decode('utf-8')
timestamp_now = int(timestamp_now)
result_test1 = int(result_test1)
compare = timestamp_now - result_test1
print(timestamp_now, end="\n")
print(result_test1, end="\n")
print(compare, end="\n")
if compare > threshold:
    print("L'age du dossier est superieur à 1 heure")

    text = "Veuillez vérifier l'ingestion du flux " + FLUX + \
        "dont le seuil d'alerte a été défini à " + threshold + " HEURES"
    message = MIMEMultipart()

    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = "ALERTE INGESTION FLUX " + FLUX
    msg.attach(MIMEText(text, 'plain'))

    # Create secure connection with server and send email
    #try:
    smtpObj = smtplib.SMTP('10.100.56.56', 25)
    smtpObj.sendmail(sender, receiver, message.as_string())
    #print ("Successfully sent email")
    #except:
    #print ("Error: unable to send email")