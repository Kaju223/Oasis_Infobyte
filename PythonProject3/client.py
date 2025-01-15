import socket


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 12345
    client_socket.connect((host, port))
    print("Connected to the server.")

    while True:
        message = input("You: ")
        client_socket.send(message.encode())
        if message.lower() == "exit":
            print("You left the chat.")
            break
        reply = client_socket.recv(1024).decode()
        print(f"Server: {reply}")

    client_socket.close()


if __name__ == "__main__":
    start_client()
