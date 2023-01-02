import socket
import time 
# import camera

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6666))
s.listen(10)

while True:
    #Accept any address that is connected to the server
    clientsocket, address = s.accept()
    #Print result
    print(f"Connection from {address} has been established!")
    #Send message to client
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    continue
    
    #break
#print("end")

#msg = s.recv(1024)
#print(msg.decode("utf-8"))
