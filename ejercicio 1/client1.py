import socket

HOST = "127.0.0.1"
PORT = 54321

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    # Recibir información del socket
    socket_info = s.recv(1024).decode()
    print("Conexion exitosa al socket.")
    print(socket_info)