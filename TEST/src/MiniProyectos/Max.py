print("--------------------")
print("Determinar el mayor.")
print("--------------------")
numero_uno = int(input("\nIntrodusca el Primer Numero: "))
numero_dos = int(input("\nIntrodusca el Segundo Numero: "))
numero_tres = int(input("\nIntrodusca el Tercer Numero: "))
print("\n")
if numero_uno > numero_dos and numero_uno > numero_tres :
    print("El ",numero_uno," es el mas grande.")
elif numero_dos > numero_tres:
    print("El ",numero_dos," es el mas grande.")
else:
    print("El ",numero_tres," es el mas grande.")
print("\nFin.")


