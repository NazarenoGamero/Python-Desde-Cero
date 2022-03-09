print("-----------------")
print("Cajero Automatico")
print("-----------------\n")
print("1.Ingresar Dinero\n2.Retirar Dinero\n3.Mostrar Dinero\n4.Salir\n")
opcion = int(input("Selecione la accion que quiere realizar: "))
saldo = 1000
while opcion != 4:
    if opcion == 1 :
        saldo += int(input("Ingrese el monto a deseado: "))
    elif opcion == 2 :
        saldo -= int(input("Ingrese el monto a deseado: "))
    elif opcion == 3 :
        print(f"Su monto actual es {saldo}")
    opcion = int(input("Selecione la accion que quiere realizar: "))
print("Adios.")

