import socket
import threading

HOST = "127.0.0.1"
PORT = 54321

def handle_client(conn, addr):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        
        print(f"Cliente {addr} dice: {data}")
        
        if data.lower() == "exit":
            print(f"El cliente {addr} ha terminado la conexión.")
            break
        
        message = input("Escribir mensaje al cliente: ")
        conn.sendall(message.encode())
        
        if message.lower() == "exit":
            print("Conexión terminada a petición del servidor.")
            break
    
    conn.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("El servidor está escuchando en", (HOST, PORT))
        
        while True:
            conn, addr = s.accept()
            print(f"Conectado desde {addr}")
            
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

start_server()
