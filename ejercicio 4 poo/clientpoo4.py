import socket

class Client:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port

    def handle_server(self, sock):
        while True:
            message = input("Escribir mensaje al servidor: ")
            sock.sendall(message.encode())
            
            if message.lower() == "exit":
                print("\U0001F6B6 Conexión terminada por el cliente.")
                break
            
            data = sock.recv(1024).decode()
            print(f"Servidor dice: {data}")
            
            if data.lower() == "exit":
                print("El servidor termino la conexion. \U0001F44B")
                break

    def connect_to_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            self.handle_server(s)

if __name__ == "__main__":
    client = Client("127.0.0.1", 54321)
    client.connect_to_server()
    client2 = Client("127.0.0.1", 54321)
    client2.connect_to_server()

    
