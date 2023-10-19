import socket

HOST = "127.0.0.1"
PORT = 54321

def handle_client(conn):
    while True:
        data = conn.recv(1024).decode()
        print(f"Cliente dice: {data}")
        
        if data.lower() == "exit":
            print("El cliente termino la conexion.")
            break
        
        message = input("Escribir mensaje al cliente: ")
        conn.sendall(message.encode())
        
        if message.lower() == "exit":
            print("Conexion terminada a petición del servidor.")
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("El servidor esta escuchando en", (HOST, PORT))
    conn, addr = s.accept()
    with conn:
        print(f"Conectado desde {addr}")
        handle_client(conn)
