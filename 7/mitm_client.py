import socket

def client():
    host = '127.0.0.1'
    port = 9000  # Connects to MITM proxy

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    message = "Hello Server, this is the client!"
    print(f"Client sending: {message}")
    s.sendall(message.encode())

    data = s.recv(1024)
    print(f"Client received: {data.decode()}")

    s.close()

if __name__ == "__main__":
    client()
