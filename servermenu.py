import socket

HOST = "127.0.0.1"
PORT = 54321

def handle_command(data):
    if data.startswith('/'):
        data = data[1:]    #Elimina el '/' inicial.
        command_parts = data.split() #Genera una lista por cada string separado por un espacio.
        if command_parts:
            command = command_parts[0]
            if command != "exit" and command != "direccion" and command != "login" and command != "mute" and command != "todos":
                return data 
            return switch(command)
        else:
            return data
    else:
        return data

def switch(command):
    if command == "exit":
       return salir(command)
    elif command == "direccion":
       return direccion(command)
    elif command == "login":
       return usuario(command)
    elif command == "mute":
       return mute(command)
    elif command == "todos"
       return todos(command)

def salir(command):
    print(f"Selecciono {command}")
    return "Comando 'exit' ejecutado con exito."
def direccion(command):
    print(f"Selecciono {command}")
    return "Comando 'direccion' ejecutado con exito."
def usuario(command):
    print(f"Selecciono {command}")
    return "Comando 'usuario' ejecutado con exito."
def mute(command):
    print(f"Selecciono {command}")
    return "Comando 'mute' ejecutado con exito."
def todos(command):
    print(f"Selecciono {command}")
    return "Comando 'todos' ejecutado con exito."

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