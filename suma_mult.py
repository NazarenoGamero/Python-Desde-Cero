"""
SUMA Y MULTIPLICACION

Returns:
    RESULTADOS
"""


def generar_lista():
    """Generador de una lista de valores numericos 
    nota: en caso de encontrar string tira excepcion, con la palabra clave listo sale del loop.
    Returns:
        lista: lista de valores numericos
    """
    lista=[]
    while True:
        dato = input('Ingrese numeros para la lista (o el comando "listo" para finalizar): ' )
        if dato == "listo":
            break
        else:
            try:
                lista.append(float(dato))
                print()
            except:
                print("\nNo es un valor valido.\n")
    return lista

def suma(lista):
    """Suma elemeneos de la lista
Args:
    lista (float)): lista de numeros
Returns:
float: resultado
"""
    resultado = 0
    if len(lista)>0:
        for i in lista:
            resultado += i
    else:
        resultado = "No hay numero en la lista."
    print(f"El resultado es {resultado}.")

def mult(lista):
    """multiplicacion elemeneos de la lista

    Args:
        lista (float)): lista de numeros

    Returns:
    float: resultado
    """
    resultado = 1
    if len(lista)>0:
        for i in lista:
            resultado *= i
    else:
        resultado = "No hay numero es la lista."
    print(f"El resultado es {resultado}.")

print("Sumas y Multiplicaciones en de numeros en listas:\n\n")
print("""   ::Menu::
1.SUMAR
2.MULTIPLICAR
3.SALIR
""")
while True:
    opcion = int(input("Elija la opcion: "))
    if opcion == 1:
        suma(generar_lista())
    elif opcion == 2:
        mult(generar_lista())
    elif opcion == 3:
        break
    else:
        print("Opcion no valida, Elija otra opcion.")
    
