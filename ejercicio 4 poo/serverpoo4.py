import socket
import threading

class Server:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port

    def handle_client(self, conn, addr):
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
        
            print(f"Cliente {addr} dice: {data}")
        
            if data.lower() == "exit":
                print(f"\U0001F6B6 El cliente {addr} termino la conexion.")
                break
        
            message = input("Escribir mensaje al cliente: ")
            conn.sendall(message.encode())
        
            if message.lower() == "exit":
                print("Conexión terminada por el servidor.")
                break
    
        conn.close()

    def start_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()
            print("El servidor está escuchando en", (self.HOST, self.PORT))
        
            while True:
                conn, addr = s.accept()
                print(f"// \u2713 Conectado desde {addr}")
                
                client_thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                client_thread.start()

if __name__ == "__main__":
    server = Server("127.0.0.1", 54321)
    server.start_server()