import socket

HOST = "127.0.0.1" # local host IP
PORT = 9909 # port number

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print("UDP server is ready...")

message, address = server.recvfrom(1)
print("Client message:", message.decode())
print("Client address:", address)

server.sendto("Hello Client!".encode(), address)

server.close()