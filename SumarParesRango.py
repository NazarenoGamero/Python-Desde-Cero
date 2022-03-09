a=int(input("Ingrese donde empieza el rango: "))
b=int(input("Ingrese donde termina el rango: "))

suma = 0

for i in range(a,(b+1)):
    if i%2==0:
        suma+=i
print("El resultado es ",suma,".")