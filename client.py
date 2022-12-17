import socket

hote = "192.168.1.131"
port = 8000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print "Connection on {}".format(port)

socket.send("Hey my name is Olivier!")

print "Close"
socket.close()
