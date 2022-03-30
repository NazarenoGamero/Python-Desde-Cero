lista=[]
valor = int(input("Ingrese un valor a la lista: "))
while valor !=0:
    lista.append(valor)
    valor = int(input("Ingrese otro un valor a la lista: "))    
lista.sort()    
print(f"Lista Ordenada: {lista}")


