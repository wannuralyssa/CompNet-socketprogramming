import socket

HOST = "127.0.0.1"
PORT = 12345

# create tcp socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# allow the address to be reused when restarting the server
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind the server to the host and port
server.bind((HOST, PORT))

# listen for incoming connections
server.listen()
print("Calculator server is listening...")

while True:
    # accept a client connection
    conn, addr = server.accept()
    print(f"Connected by {addr}")

    with conn:
        while True:
            # receive the calculation request
            request = conn.recv(1024).decode().strip()
            if not request:
                break

            print("Received:", request)

            try:
                # separate the numbers and operator
                parts = request.split()

                if len(parts) != 3:
                    raise ValueError("Invalid calculation format")

                num1 = float(parts[0])
                operator = parts[1]
                num2 = float(parts[2])

                # perform the calculation
                if operator == "+":
                    result = num1 + num2
                elif operator == "-":
                    result = num1 - num2
                elif operator == "*":
                    result = num1 * num2
                elif operator == "/":
                    if num2 == 0:
                        raise ValueError("Cannot divide by zero")
                    result = num1 / num2
                else:
                    raise ValueError("Invalid operator")

                response = f"Result: {result:g}"

            except ValueError as error:
                response = f"Error: {error}"

            # send the reult back to the client
            conn.sendall(response.encode())
            print("Sent:", response)

    print("Connection closed.")