import socket

hote = "192.168.1.131"
port = 8005

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))

while True:
        response = socket.recv(255)
        print (response.decode())
        inp=input("msg: ")
        socket.send(inp.encode())
        

print("Close")
socket.close()
