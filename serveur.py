import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 8005))
socket.listen(5)
client, address = socket.accept()
print ("{} connected".format( address ))

while True:
        inp=input("msg: ")
        client.send(inp.encode())
        response = client.recv(255)
        print(response.decode())

print ("Close")
client.close()
stock.close()
