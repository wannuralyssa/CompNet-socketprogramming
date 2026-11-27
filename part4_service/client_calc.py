import socket

HOST = "127.0.0.1"
PORT = 12345

# create a tcp socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect tp the calculator server
client.connect((HOST, PORT))
print("Connected to the Calculator Server!")
print("Enter calculations such as 10 + 5")
print("Type 'quit' to exit.")

while True:
    # get calculation from the user
    request = input("\nEnter calculation: ")

    if request.lower() == "quit":
        print("Disconnecting from the server...")
        break
    try:
        # send the calculation to the server
        client.sendall(request.encode())

        # receive the result from the server
        response = client.recv(1024).decode()

        print(response)
    except OSError:
        print("Connection to server lost.")
        break

# close the connection
client.close()
print("Client disconnected.")