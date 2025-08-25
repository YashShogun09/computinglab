import socket

def server():
    host = '127.0.0.1'
    port = 9001

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print("Server listening...")

    conn, addr = s.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Server received: {data.decode()}")
        response = "Message received"
        conn.sendall(response.encode())

    conn.close()

if __name__ == "__main__":
    server()
