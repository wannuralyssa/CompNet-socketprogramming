import threading
import socket

host = '127.0.0.1' # local host
port = 12344

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
 # fill up here
    for client in clients:
        client.sendall(message)

def handle(client):
# fill up here
    while True:
        try:
            message = client.recv(1024)
            if not message:
                raise ConnectionError

            broadcast(message)

        except (ConnectionError, OSError):
            if client in clients:
                index = clients.index(client)
                nickname = nicknames.pop(index)
                clients.pop(index)

                broadcast(f"{nickname} left the chat!".encode())

            client.close()
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("NICK".encode())
        nickname = client.recv(1024).decode()

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode())

        client.send("Connected to the server!".encode())

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()
