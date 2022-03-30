from xml.dom.pulldom import PROCESSING_INSTRUCTION


def sumar(numero):
    if numero == 0:
        resultado = 0
    else:
        resultado = sumar(numero//10) + (numero%10)
    return resultado

print(sumar(123))
#print(sumar(-123))
print(sumar(0))