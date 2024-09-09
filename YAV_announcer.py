import socket
import time
import json

serverPort = 5006
ip = '255.255.255.255'

content_name = input('Enter content name: ')

json_data = {
    'content': content_name
}

json_bytes = json.dumps(json_data).encode('utf-8')

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # indicates ipv4 adressing, says that this is UDP socket, specifies UDP Protocol
server.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1) # socket parameter level, to enable send braodcast messages
while True:
    server.sendto(json_bytes, (ip, serverPort))
    print("JSON data sent")

    time.sleep(60)