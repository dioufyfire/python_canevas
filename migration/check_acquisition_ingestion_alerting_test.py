# _*_ coding:utf8 _*_

##########################
# PROGRAMME ALERTINNG ####
# INGESTION JOURNALIER ####
# AUTEUR : DIOUFYFIRE1 ##
#########################


##########################################
# IMPORTATION DES FONCTIONS EXTERNES
#########################################
import subprocess
import datetime
from datetime import date, datetime,  timedelta
import time
import sys, os
import configparser # TRAITEMENT FICHIER DE CONFIGURATION
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

##########################################
# DEFINITION LOCALE DE FONCTION
#########################################

def current_milli_time():
    return round(time.time() * 1000)

#INIT CONFIG
logging.basicConfig(filename='/home/sddesigner/dlk/scripts/logs/check_acq_ingestion_alerting.log', level=logging.INFO, format='%(asctime)s %(levelname)s --- %(message)s')

### TRICK FOR LOG IN CONSOLE AND FILE AT SAME TIME
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter(' %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger().addHandler(console)

##########################################
# MAIN
##########################################
try:
    f = open(sys.argv[1])
    f.close()
except FileNotFoundError:
    print('File does not exist')
    exit(1)

#VARIABLES DEFINITION
sender = "sup_bigdata@orange-sonatel.com"
receiver = "Mamadou.DIOUF2@orange-sonatel.com"
receiver_cc = "Mamadou.DIOUF2@orange-sonatel.com"
logging.debug('Receivers : %s, %s, Sender: %s', receiver, receiver_cc, sender)
interval = int(sys.argv[2])
threshold = interval * 3600000
reminder = 3


# Reading parameters in file
####
file_container = configparser.ConfigParser(inline_comment_prefixes="#")
### prepend a fake section header to your config file data
with open(sys.argv[1]) as stream:
    file_container.read_string("[top]\n" + stream.read())  # This line does the trick.
    if file_container.has_option('top', 'FLUX'):
        FLUX = file_container.get('top','FLUX')
        FLUX = FLUX.strip('"')
    else:
        FLUX = file_container.get('top','flux')
        FLUX = FLUX.strip('"')

    if file_container.has_option('top','DIR_PARENT'):
        DIR_PARENT = file_container.get('top','DIR_PARENT')
        DIR_PARENT = DIR_PARENT.strip('"')
    else:
        DIR_PARENT = file_container.get('top','dir_parent')
        DIR_PARENT = DIR_PARENT.strip('"')

    if file_container.has_option('top', 'SUFFIXE'):
        SUFFIXE = file_container.get('top','SUFFIXE')
        SUFFIXE = SUFFIXE.strip('"')
    else:
        SUFFIXE = file_container.get('top','suffixe')
        SUFFIXE = SUFFIXE.strip('"')

logging.info('##### CHECK FLUX : %s', FLUX)
logging.info('Config filename: %s', sys.argv[1])
## current_datetime = datetime.now() - timedelta(days=1)
current_datetime = datetime.now()
year = current_datetime.year
#DUMMY DATA
#year = "2021"
month = current_datetime.strftime("%m")
#DUMMY DATA
#month = "12"
day = current_datetime.strftime("%d")
#DUMMY DATA
#day = "09"
timestamp_now = current_milli_time()

### HDFS=$(hdfs dfs -ls $DIR_DLK/$flux$SUFFIXE/year=$year_x1/month=$month_x1/day=$date_x1  2>/dev/null | wc -l)
command = "hdfs dfs -test -e " + DIR_PARENT + "/" + FLUX + SUFFIXE + "/" + FLUX + SUFFIXE + "_" + str(year) + str(month) + str(day) + ";echo $?"
command1 = "hdfs dfs -stat \"%Y\" " + DIR_PARENT + "/" + FLUX + SUFFIXE + "/" + FLUX + SUFFIXE + "_" + str(year) + str(month) + str(day) + " | tail -1"
logging.debug('%s', command)
logging.debug('%s', command1)
try:
    logging.info('TEST EXISTANCE DOSSIER %s-%s-%s', year, month, day)
    p = subprocess.Popen(command,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT)
except:
    logging.warn("Erreur lors du controle d'existance")
    sys.exit(1)

result_test = int(p.stdout.read())

if not result_test:
    logging.info("CONTROLE DE LA DATE DU DOSSIER %s-%s-%s ", str(year), str(month), str(day))
    q = subprocess.Popen(command1,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT)
else:
    logging.info("DOSSIER %s-%s-%s INEXISTANT", str(year), str(month), str(day))
    sys.exit(1)

result_test1 = q.stdout.read().decode('utf-8')
timestamp_now = int(timestamp_now)
result_test1 = int(result_test1)
compare = timestamp_now - result_test1

file_tmp_pwd="/home/sddesigner/dlk/scripts/tmp/" + FLUX + "_" + str(year) + str(month) + str(day)
try:
    f = open(file_tmp_pwd, 'r')
    contents = f.read()
    retry_old = contents['retry']
    timestamp_old = contents['timestamp']
    contents.update({'timestamp' : timestamp_now})
    f.close()
    logging.info("Premier controle deja executé")
    exit(1)
except FileNotFoundError:
    logging.info("Premier controle d'existance reussi")
    f = open(file_tmp_pwd, "w")
    dict1 = {'retry' : 1, 'timestamp' : timestamp_now}
    str1 = repr(dict1)
    f.write("dict1 = " + str1)
    file1.close()
    if f.mode=='r':
        contents= f.read()
    f.close()

logging.info('TIMESTAMP NOW : %s - TIMESTAMP LAST MODIFIED : %s -  DIFFERENCE : %s', result_test, result_test1, compare)

if compare > threshold:
    logging.info("L'age du dossier est superieur à 1 heure")
    text = "Veuillez vérifier l'ingestion du flux " + FLUX + "dont le seuil d'alerte a été défini à " + str(interval) + " HEURE(S)"
    message = MIMEMultipart()

    message['From'] = sender
    message['To'] = receiver
    message['Cc'] = receiver_cc
    message['Subject'] = "ALERTE INGESTION FLUX " + FLUX
    message.attach(MIMEText(text, 'plain'))

    try:
        smtpObj = smtplib.SMTP('10.100.56.56', 25)
        smtpObj.sendmail(sender, receiver, message.as_string())
        logging.info("Successfully sent email")
    except:
        logging.info("Error: unable to send email")
else:
    logging.info("L'age du dossier est inférieur à 1 heure. Pas d'alerte")
