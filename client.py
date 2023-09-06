import socket

HOST = "127.0.0.1"
PORT = 54321

def send_receive_data(sock, data):
    sock.sendall(data.encode())
    response = sock.recv(1024).decode()
    return response

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input("Ingrese un mensaje: ")
        if message.lower() == 'exit':
            break
        response = send_receive_data(s, message)
        if message.startswith('/'):
            print(f"Respuesta del servidor al comando '{message}': {response}")
        print(f"Respuesta del servidor: {response}")