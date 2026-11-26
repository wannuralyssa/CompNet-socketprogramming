import socket

HOST = "127.0.0.1" # local host IP
PORT = 9549 # port number

# generate server socket to connect
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind socket with host and port number
server.bind((HOST, PORT))

# server socket listens and waits for connection request
server.listen(5)
print(f"Listening ...")

while True:
    # accept the socket and address tyring to connect
    conn, addr = server.accept()
    print(f"Connected by {addr}")

    # receive and store it as name
    name = conn.recv(1).decode()
    print(f"Client name: {name}")

    # receive and store as message
    message = conn.recv(1024).decode()
    print(f"Client message: {message}")

    # receive and store it as message
    response = f"Hello {name}! Your message was received."
    conn.send(response.encode())

    # close the TCP connection
    conn.close()
    print("Connection closed.")