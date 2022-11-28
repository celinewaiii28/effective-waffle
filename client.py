import socket

host = '192.168.1.60'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((socket.gethostname(), 6666))
s.connect((host, 6666))

while True:
    msg = s.recv(1024)
    print(msg.decode("utf-8"))

    continue
