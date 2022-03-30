import random
aleatorio = random.randint(0,100)
contador = 0
while True:
    numero = int(input("Digite un numero: "))
    contador += 1
    if numero > aleatorio:
        print("\nEl numero es menor.")  
    elif numero < aleatorio:
        print("\nEl numero es mayor.")
    else: 
        print(f"\nAcertaste el numero en {contador} intentos.")
        break