print("-----------")
print("CALCULADORA")
print("-----------\n")
print("----------------")
print("Menu de opciones")
print("----------------\n")
print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Div Entera\n6. Exponente\n7. Modulo\n8. Borrar\n9. Salir")
operacion = int(input("\nElija la operacion a ejecutar: "))
while operacion != 9:
    if operacion !=8:
        numero1 = float(input("\nIntrodusca el primer Numero: "))
    while operacion != 8 and operacion != 9:
        numero2 = float(input("\nIntrodusca el segundo Numero: "))
        print("\n")
        if operacion == 1 : 
            numero1 += numero2
            print(numero1)
        elif operacion == 2 : 
            numero1 -= numero2
            print(numero1)
        elif operacion == 3 : 
            numero1 *= numero2
            print(numero1)
        elif operacion == 4 : 
            numero1 /= numero2
            print(numero1)
        elif operacion == 5 : 
            numero1 //= numero2
            print(numero1)
        elif operacion == 6 : 
            numero1 **= numero2 
            print(numero1)
        elif operacion == 7 : 
            numero1 %= numero2
            print(numero1)
        else:
            print("No es un Operacion Valida")
        operacion = int(input("\nElija la operacion a ejecutar: "))
    operacion = int(input("\nElija la operacion a ejecutar: "))
quit()