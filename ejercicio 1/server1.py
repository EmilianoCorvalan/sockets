import socket

HOST = "127.0.0.1"
PORT = 54321

def send_socket_info(conn):
    conn.sendall(f"Socket info: {conn.getsockname()}".encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print("El servidor está escuchando en", (HOST, PORT))

while True:
    conn, addr = s.accept()
    print(f"Conectado desde {addr}")
    
    send_socket_info(conn) #Envia informacion al cliente
            