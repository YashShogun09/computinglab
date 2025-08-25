import socket

def mitm_proxy():
    # Listen for client here
    mitm_host = '127.0.0.1'
    mitm_port = 9000

    # Server address to forward to
    server_host = '127.0.0.1'
    server_port = 9001

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((mitm_host, mitm_port))
    s.listen(1)
    print("MITM Proxy listening...")

    client_conn, client_addr = s.accept()
    print(f"Client connected: {client_addr}")

    # Connect to the real server
    server_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_conn.connect((server_host, server_port))

    while True:
        # Receive from client
        client_data = client_conn.recv(1024)
        if not client_data:
            break

        print(f"MITM intercepted (client -> server): {client_data.decode()}")

        # Optionally modify message
        modified_data = client_data.decode().replace("Hello", "Hi")  # Example modification
        print(f"MITM modifies message to: {modified_data}")

        # Send modified message to server
        server_conn.sendall(modified_data.encode())

        # Receive from server
        server_data = server_conn.recv(1024)
        if not server_data:
            break

        print(f"MITM intercepted (server -> client): {server_data.decode()}")

        # Forward server response to client
        client_conn.sendall(server_data)

    client_conn.close()
    server_conn.close()

if __name__ == "__main__":
    mitm_proxy()
