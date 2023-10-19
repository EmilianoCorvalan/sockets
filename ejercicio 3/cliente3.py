import socket

HOST = "127.0.0.1"
PORT = 54321

def handle_server(sock):
    while True:
        message = input("Escribir mensaje al servidor: ")
        sock.sendall(message.encode())
        
        if message.lower() == "exit":
            print("Conexión terminada a petición del cliente.")
            break
        
        data = sock.recv(1024).decode()
        print(f"Servidor dice: {data}")
        
        if data.lower() == "exit":
            print("El servidor ha terminado la conexión.")
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    handle_server(s)
