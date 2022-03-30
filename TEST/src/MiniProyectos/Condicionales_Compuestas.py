print("Sistema para calcular promedio de un alumno.")
nombre = input("Indique su nombre: ")
notaMatematica = float(input("Indique su nota de matematica: "))
notaLengua = float(input("Indique su nota de lengua: "))
notaFisica = float(input("Indique su nota de fisica: "))
promedio = (notaMatematica + notaFisica + notaLengua) / 3
promedioCon2Decimales = (notaFisica + notaMatematica + notaLengua) / 3

if promedio >= 7:
    print(nombre + " has aprobado con ", promedio)
    print(nombre + " has aprobado con ", round(promedio,2))
else:
    print(nombre + " has reprobado con ", promedio)
    print(nombre + " has reprobado con ", round(promedio, 2))
print("FIN.")