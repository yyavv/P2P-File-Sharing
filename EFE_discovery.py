from socket import *
import json
from socket import socket, AF_INET, SOCK_DGRAM, IPPROTO_UDP, SOL_SOCKET, SO_BROADCAST
import json

contentDiscovery = {}
ip='192.168.43.184'
serverPort = 5006

print("Server is ready to discover")

while True:
    serverSocket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
    serverSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    serverSocket.bind((ip, serverPort))
    
    message, (clientAddress, clientPort) = serverSocket.recvfrom(2048)
    print('Received {} bytes from {}'.format(len(message), clientAddress))
    receivedMessage = json.loads(message)

    contentName = receivedMessage.get('content')

    if contentName not in contentDiscovery:
        contentDiscovery[contentName] = clientAddress

    with open("contents.txt", "w") as contentFile:
        json.dump(contentDiscovery, contentFile)
    
    print("Available contents are:\n", contentDiscovery)
    print("You can find contents details in contents.txt")