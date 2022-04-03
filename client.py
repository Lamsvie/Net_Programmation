import socket
import json
adresseIP = "192.168.10.1"
port=50000
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect((adresseIP , port))
print("Connecté au serveur")
print("Taper FIN pour terminer la conversation. ")
message=""
while message.upper() != "FIN":
    message = input("> ")
    
    if message == "START" :
        action = "START"
       
    elif message == "MOYENNE":
	action = "MOYENNE"

    elif message == "STOP":
        action = "STOP"

        data = { "action" : action }
        sendData = json.dumps(data)
        client.sendall(sendData.encode("utf-8"))

        response = client.recv(255)
        print("le resultat est :" , response.decode("utf-8"))
        
        exit(0)
print("Connexion fermé")
client.close()
