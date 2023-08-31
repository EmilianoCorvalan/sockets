import socket

HOST = "127.0.0.1"
PORT = 54321

def handle_command(data):
    if data.startswith("/"):
        print("Comando recibido")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("El servidor está escuchando en", (HOST, PORT))
    conn, addr = s.accept()
    with conn:
        print(f"Conectado desde {addr}")
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            handle_command(data)
            conn.sendall(data.encode())