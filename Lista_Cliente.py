print(''' 
--------------
Lista Clientes
--------------

        ::Menu::

1. Agregar cliente.
2. Mostrar todos los clientes.
3. Mostrar cliente por DNI
4. Borrar cliente.
5. Salir.
''')

clientes = []
def pedirdatoscliente():
    nombre = str(input("\nIngrese el nombre del cliente: "))
    apellido = str(input("\nIngrese el apellido del cliente: "))
    dni = int(input("\nIngrese el DNI del cliente: "))
    return nombre,apellido,dni

def addcliente(nombre,apellido,dni):
    clientes.append({'Nombre':nombre,'Apellido':apellido,'DNI':dni})

def printCliente(cliente):
    print(f"\nNombre: {cliente['Nombre']} ; Apellido: {cliente['Apellido']} ; DNI: {cliente['DNI']}")

def buscarCliente(dni):
    for i in clientes:
        if i['DNI'] == dni:
            printCliente(i)
            return True
    return False

def mostrarTodosClientes():
    print("\nClientes: ")
    for i in clientes:
        printCliente(i)

def borrarCliente(dni):
    for i in clientes:
        if i['DNI'] == dni:
            clientes.remove(i)
            return True
    return False

while True:
    opcion = int(input("\nIndique la accion que quiere realizar: "))
    if opcion == 1:
        nombre,apellido,dni = pedirdatoscliente()
        addcliente(nombre,apellido,dni)
    elif opcion == 2:
       mostrarTodosClientes() 
    elif opcion == 3:
        dnicli = int(input("\nIndique el DNI del cliente que desea buscar: "))
        if buscarCliente(dnicli):
            print("",end="")
        else:
            print("No se encontro al cliente.")
    elif opcion == 4:
        dnicli = int(input("\nIndique el DNI del cliente que desea borrar: "))
        if borrarCliente(dnicli):
            print("\nCliente Eliminado.")
        else:
            print("No se encontro al cliente.")
    elif opcion == 5:
        print("Adios.")
        break
    else:
        print("\nOpcion no valida.")

