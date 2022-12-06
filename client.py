import socket
from camera import *

host = '192.168.1.60'
port = 6666
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    message = "A"
    s.send(message.encode('utf-8'))
    print("Awaiting the reply...")
    reply = s.recv( 1024 ).decode( 'utf-8' )
    print("Received ", str(reply))

    message = "B"
    s.send(message.encode('utf-8'))
    print("Awaiting the reply...")
    reply = s.recv( 1024 ).decode( 'utf-8' )
    print("Received ", str(reply))
    s.close()
    break






