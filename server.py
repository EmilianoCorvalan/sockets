import socket

HOST = "127.0.0.1"
PORT = 54321

def handle_command(data):
    if data.startswith("/"):
        print("Comando recibido")
        return "Comando recibido"
    else:
        return data

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  #AF_INET corresponde a IPv4 y SOCKSTREAM a TCP
    s.bind((HOST, PORT))
    s.listen()
    print("El servidor está escuchando en", (HOST, PORT))
    conn, addr = s.accept() #conn es un objeto socket y addr la direccion.
    with conn:  #se inicia bloque with para que el recurso socket 'conn' se cierre cuando termine el bloque.
        print(f"Conectado desde {addr}")
        while True:
            data = conn.recv(1024).decode() #se recibe data del cliente (hasta 1024bytes aca) y los decodifica para almacenarlos en la variable.
            if not data:
                break
            response = handle_command(data)
            conn.sendall(response.encode())
            