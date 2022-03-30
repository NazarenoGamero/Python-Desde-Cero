from tkinter import END




'''
mensaje = "Suceccion de fibonacci"
while num1 != 2584:
    mensaje += " " + str(num1) + " " + str(num2)
    num1 = num1 + num2
    num2 = num1 + num2
print(mensaje)
'''
def fibonacci_sp(n):
    num1 = 0
    num2 = 1

    print("Suceccion de Fibonacci: ", end="")
    while num2 <= n:     
        print(num1,num2, end= " ")
        num1 = num1 + num2
        num2 = num1 + num2

####################################################

def fibonacci_dp(i, cache = {0 : 0,1 : 1}):
    if i in cache:
        return cache[i]
    else:
        cache[i] = fibonacci_dp(i-2) + fibonacci_dp(i-1)  
    return cache[i]

n = int(input("\n\nIngrese el fibonacci que desea obtener: "))
print(f"\nFibonacci: ",end ="")

########################################################### 