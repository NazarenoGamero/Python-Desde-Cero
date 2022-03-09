print("Calcular Factorial: \n")
numero = int(input("Ingrese el numero: "))
factorial = 1
if numero >= 0:
    for i in range(1,numero+1):
        factorial *= i
    print(f"El factorial de {numero} es {factorial}")
else:
    print("No se puede sacar el factorial.")