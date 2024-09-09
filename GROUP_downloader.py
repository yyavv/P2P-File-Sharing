from socket import *
import json
import os
from datetime import datetime

if not os.path.exists('./rec/'):
    os.mkdir('./rec/')

serverPort = 8000

while True:
    requestedFile = input("Enter file name: ")
    contentFile = open("contents.txt", 'r')
    Json = contentFile.read()
    contentFile.close()

    dict = json.loads(Json)
    isreqfiledownloaded = False

    if requestedFile in dict:
        clientIp = dict[requestedFile]
        clientSocket = socket(AF_INET, SOCK_STREAM)
        
        try:
            clientSocket.connect((clientIp, serverPort))
            request = {
                "requested_content": requestedFile
            }
            requestJson = json.dumps(request)
            clientSocket.send(requestJson.encode())
            print(f"Request sent for {requestedFile}")
            print("Downloading")
            
            with open("./rec/downloaded_" + requestedFile, "wb") as f:
                while True:
                    bytes_read = clientSocket.recv(4096)
                    if len(bytes_read) <= 0:
                        break
                    f.write(bytes_read)
                    isreqfiledownloaded = True

            if isreqfiledownloaded:
                now = datetime.now()
                time = now.strftime("%d/%m/%Y %H:%M:%S")

                with open("download_log.txt", "a") as file:
                    file.write(f"requested file {requestedFile} downloaded from {clientIp} at {time}\n")

                print(f"File {requestedFile} downloaded")
            else:
                print(f"Failed to download  {requestedFile}")
                
        except Exception as e:
            print(f"Error while downloading: {str(e)}")
            continue

        clientSocket.close()
        
    else:
        print(f"File {requestedFile} cannot be downloaded from online peers.")