import threading
import socket

host = '127.0.0.1' # local host
port = 12344

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive():
    while True:
        try:
            # fill up here
            message = client.recv(1024).decode()

            if not message:
                raise ConnectionError

            if message == "NICK":
                client.send(nickname.encode())
            else:
                print(message)
        except:
            # fill up here
            print("An error occured!")
            client.close()
            break


def write():
    while True:
        # fill up here
        try:
            message = f"{nickname}: {input('')}"
            client.send(message.encode())
        except (EOFError, OSError):
            client.close()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
