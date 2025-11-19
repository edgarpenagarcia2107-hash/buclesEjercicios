i = float(input("Ingrese la cantidad de estudiantes -> "))
j = int(input("ingrese el codigo del estudiante -> "))
k = float(input("Ingrese la nota del estudiante -> "))
contadorEstudaintes = 0
aprobaron = 0
reprobaron = 0
sumaDefinitiva = 0

while contadorEstudaintes < i:
    input("Ingrese el codigo del estudiante -> ")
    input("ingrese la nota del estudiante -> ")
    
    if k >= 3:
        aprobaron = aprobaron + 1
    else:
        reprobaron = reprobaron + 1
    
    sumaDefinitiva = sumaDefinitiva + k
    contadorEstudaintes = contadorEstudaintes + 1

promedio = sumaDefinitiva / i

print("El promedio de la clase es: ", promedio)
print("La cantidad de estudiantes que aprobaron la clase es: ", aprobaron)
print("La cantidad de estudiantes que reprobaron la clase es: ", reprobaron)