print("----------------------")
print("Sistema Vacional Rappi")
print("----------------------\n")
nombre = input("Introdusca su nombre: ")
clave = int(input("\n-'1' para Atencion al cliente\n-'2' para Logistica\n-'3' para Gerencia\nIntrodusca su clave de trabajo: "))
antiguedad = int(input("\nIntrodusca su antiguedad(en años): "))
print("\n")
if clave == 1:
    if antiguedad == 1:
        print(nombre + " le corresponden 6 dias de vacaciones.")
    elif 2 <= antiguedad <= 6:
        print(nombre + " le corresponden 14 dias de vacaciones.")
    elif 6 < antiguedad:
        print(nombre + " le corresponden 20 dias de vacaciones.")
    else:
        print(nombre + " a usted NO le corresponden vacaciones.")
elif clave == 2:
    if antiguedad == 1:
        print(nombre + " le corresponden 7 dias de vacaciones.")
    elif 2 <= antiguedad <= 6:
        print(nombre + " le corresponden 15 dias de vacaciones.")
    elif 6 < antiguedad:
        print(nombre + " le corresponden 22 dias de vacaciones.")
    else:
        print(nombre + " a usted NO le corresponden vacaciones.")
elif clave == 3:
    if antiguedad == 1:
        print(nombre + " le corresponden 10 dias de vacaciones.")
    elif 2 <= antiguedad <= 6:
        print(nombre + " le corresponden 20 dias de vacaciones.")
    elif 6 < antiguedad:
        print(nombre + " le corresponden 30 dias de vacaciones.")
    else:
        print(nombre + " a usted NO le corresponden vacaciones.")
else:
    print("No es una clave valida.")

print("Fin.")