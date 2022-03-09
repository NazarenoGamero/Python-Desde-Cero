print("-----------------")
print("Cajero Automatico")
print("-----------------\n")
print("\t::MENU::\n")
print("1.Ingresar Dinero\n2.Retirar Dinero\n3.Mostrar Dinero\n4.Salir\n")
opcion = int(input("Selecione la accion que quiere realizar: "))
saldo = 1000
while True:
    if opcion == 1 :
        saldo += int(input("Ingrese el monto a deseado: "))
        print(f"\nSu monto actual es '{saldo}' \n")
    elif opcion == 2 :
        retiro = int(input("Ingrese el monto a deseado: "))
        if retiro <= saldo:
            saldo -= retiro
            print(f"\nSu monto actual es '{saldo}' \n")
        else:
            print("Dinero en la cuenta insuficiente para el 'retiro'.\n")
    elif opcion == 3 :
        print(f"\nSu monto actual es '{saldo}' \n")
    elif opcion == 4:
        print("Adios.")
        break
    else:
        print("\nOpcion NO valida.\n")
    opcion = int(input("Selecione la accion que quiere realizar: "))


