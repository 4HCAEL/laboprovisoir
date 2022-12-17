import socket

hote = "192.168.1.131"
port = 8000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))

while True:
        print ("{} connected".format( address ))

        response = client.recv(255)
        inp=input("msg: ")
        client.send(inp.encode())
        
        if response != "":
                print (response)
print ("Close")
socket.close()
