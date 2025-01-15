import socket


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(2)
    print("Server started. Waiting for connections...")

    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    while True:
        message = conn.recv(1024).decode()
        if message.lower() == "exit":
            print("Client has left the chat.")
            break
        print(f"Client: {message}")
        reply = input("You: ")
        conn.send(reply.encode())

    conn.close()
    server_socket.close()


if __name__ == "__main__":
    start_server()
