dato="/comando par1 par2"
if dato.startswith('/'):
    dato = dato[1:]
print(dato.split())
comando = dato[0]
def switch(comando):
    if comando == "exit":
        salir(comando)
    elif comando == "direccion":
        direccion()
    elif comando == "login":
        usuario()
    elif comando == "mute":
        mute()
    elif comando == "todos":
        todos()

def salir(comando):
    print("salir")
def direccion():
    print("direccion")
def usuario():
    print("usuario")
def mute():
    print("mute")
def todos():
    print("todos")