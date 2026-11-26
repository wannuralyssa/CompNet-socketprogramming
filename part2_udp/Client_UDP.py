import socket

HOST = "127.0.0.1" # local host IP
PORT = 9909 # port number

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("Hello Server!".encode(), (HOST,PORT))
response, address = client.recvfrom(1024)
print("Server response:", response.decode())

client.close()







