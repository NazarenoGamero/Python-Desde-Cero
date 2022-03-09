from tkinter import END


num1 = 0
num2 = 1
'''
mensaje = "Suceccion de fibonacci"
while num1 != 2584:
    mensaje += " " + str(num1) + " " + str(num2)
    num1 = num1 + num2
    num2 = num1 + num2
print(mensaje)
'''

print("Suceccion de Fibonacci: ", end="")
while num2 <= 1597:
    print(num1,num2, end= " ")
    num1 = num1 + num2
    num2 = num1 + num2