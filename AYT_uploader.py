from socket import *
import json
from datetime import datetime

ip='192.168.43.184'
port = 8000
serverAdress=(ip,port)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(serverAdress)
serverSocket.listen(5)

print('Server is ready to upload')


while True:
    connection , (address,port) = serverSocket.accept()
    print(f"Connection from {address} ")
    jsonReq =  connection.recv(4096).decode()

    requestedFile = json.loads(jsonReq)
    print(f"Request for {requestedFile['requested_content']}")

    filename = requestedFile['requested_content']
    print("Uploading")
    with open(filename,'rb') as file:
        l = file.read(4096)
        while (l):
            connection.send(l)
            l = file.read(4096)

        # connection.sendall(file.read())
    print(f"File {filename} uploaded")
    
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")

    with open("upload_log.txt","a") as file:
        file.write(f"File {filename} sended to {address} at {time} \n")

    connection.close()