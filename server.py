import socket
import time 
# import camera


while True:
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 6666))
    s.listen(2)
    # Accept connections
    client, address = s.accept()
    print("Connected to", address)

    for i in range(10):
    # Receive data and decode using utf-8
        data = client.recv( 1024 ).decode( 'utf-8' )
        print("Received :", repr(data))

        # Send data to client in utf-8
        if ("A" == data):
            reply = "GOOD"
            client.send(reply.encode('utf-8'))
        elif("A" != "GOOD"):
            reply = "FAIL"
            client.send(reply.encode('utf-8'))


    while True:
        if (data== '0'):
            from camera import *
            data = client.recv( 1024 ).decode( 'utf-8' )
            print("Received :", repr(data))
            # time.sleep(1)
            # import encode
        
        elif (data== '2'):
            from camera import capture
            data = client.recv( 1024 ).decode( 'utf-8' )
            print("Received :", repr(data))
            
        
        continue
    


