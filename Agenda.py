print("------")
print("Agenda")
print("------\n")

print("\t.:Menu:.\n")
print("1.Agregar Contacto\n2.Borrar Contacto\n3.Ver Contactos\n4.Salir\n")

contactos = {}
while True:
    opcion = int(input("\nElija la opcion que desea: "))
    if opcion == 1:
        nombre = input("\nIntrudusca el Nombre del contacto que desea agregar: ")
        if nombre not in contactos:
            numero = int(input("\nIntrodusca el Numero del contacto: "))
            contactos[nombre] = numero
            print("\nContacto Agregado.")
        else: 
            print("\nEl nombre de contacto ya existe.")
    elif opcion == 2:
        nombre = input("\nIntrudusca el Nombre del contacto que desea borrar: ")
        if nombre in contactos:
            del(contactos[nombre])
            print("\nContacto Eliminado.")
        else:
            print("\nEl contacto no pertence a la agenda.")
    elif opcion == 3:
        print("\nContactos:\n")
        for clave,valor in contactos.items():
            print(f"Nombre:{clave}\tNumero:{valor}")
    elif opcion == 4:
        print("\nAdios.")
        break
    else:
        print("Opcion invalida.")
