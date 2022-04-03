#coding:utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import csv

fichierdict= []
with open("Trafic.csv") as fichier:
    reader= csv.DictReader(fichier, delimiter=' ')
    for line in reader:
        fichierdict.append(line)
    print(fichierdict[0])
msg = MIMEMultipart()
msg['FROM']= "fatima@redmail.com"
msg['password']= "P@ssword123"
msg['TO'] = "mohamed@redmail.com"
msg['Subject']= "Rapport Analyse"
corp_message= f"{fichierdict[0]}"
msg.attach(MIMEText(corp_message,'html'))
echange = smtplib.SMTP('mail.redmail.com',587)
echange.starttls()
try:
    echange.login(msg['FROM'], msg['password'])
    echange.sendmail(msg['FROM'], msg['TO'], msg.as_string())
    print("Envoyer avec Succes")
except:
    print("Mauvais compte")
finally:
    echange.quit()
