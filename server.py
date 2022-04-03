#coding:utf-8
import json
import socket
import mysql.connector as MC

'''
    recuperation de nom, pwd, mail de user
    se connecte à la bd por verifier les identifiant
    si existant accept la connexion et envoi au client message de connexion reussi
    sinon envoi message erreur d'identifiant
'''
def VerificationInfoBd():
    #connexion a la bd
    try:
        connexion = MC.connect(host='localhost', database='vmail', user='root', password='root')
        curseur = connexion.cursor()
        req = "select * from mailbox"
        curseur.execute(req)
        resultat = curseur.fetchall()
        return resultat
    except MC.Error as err:
        print(err)
    finally:
        connexion.close()

def inscription(mail_add:str,pwd:str):
    try:
        connexion = MC.connect(host='localhost', database='vmail', user='root', password='root')
        curseur = connexion.cursor()
        req = "insert into mailbox(username,password) values('"+mail_add+"','"+pwd+"')"
        curseur.execute(req)
        connexion.commit()
    except MC.Error as err:
        print(err)
    finally:
        connexion.close()


host= ''
port = 5566
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creation de socket
        # Demarrae de server
server.bind((host, port))
print("Demarrage de server....")
while True:
    server.listen(5) #server ecoute sur le port '5566'
    conn, addr = server.accept()

    #Demande d'info aux client
    messagesend = f"veillez entrer vos identifiants"
    messagesend = messagesend.encode("utf8")
    conn.sendall(messagesend)
    print("En attente d'info client")

    #Reception de l'action souhaiter par le client
    Action = conn.recv(1024)
    Action = Action.decode("utf8")

    # Echange d'info cote server avec client
    messagerecv = conn.recv(1024)  # reception de donne avec param de buffer 1024
    messagerecv = messagerecv.decode("utf8")
    data = json.loads(messagerecv)
    if Action == "0":
        inscription(data[0],data[1])
        messagesend_1 = f"Compte Crée avec succes, Veillez vous connecter à votre compte sur le lien http://mail.redmail.com/mail ."
        messagesend_1 = messagesend_1.encode("utf8")
        conn.sendall(messagesend_1)
        break
    elif Action == "1":
        # verification info
        info = VerificationInfoBd()
        for element in info:
            if element[0] == data[0]:
                messagesend_1 = element[1].encode("utf8")
                conn.sendall(messagesend_1)

                result = conn.recv(1024)
                result = result.decode("utf8")
                if result == "1":
                    # Envoi de message de connxion reussi
                    messagesend_2 = f"Identifiant correct, Veillez vous connecter à votre compte sur le lien http://mail.redmail.com/mail ."
                    messagesend_2 = messagesend_2.encode("utf8")
                    conn.sendall(messagesend_2)
                else:
                    # Envoi de message de connxion echoue
                    messagesend_2 = f"Identifiant Incorrect"
                    messagesend_2 = messagesend_2.encode("utf8")
                    conn.sendall(messagesend_2)
        break
    else:
        messagesend_4 = f"Vous avez tapez le mauvais numero"
        messagesend_4 = messagesend_4.encode("utf8")
        conn.sendall(messagesend_4)

conn.close()
server.close()
