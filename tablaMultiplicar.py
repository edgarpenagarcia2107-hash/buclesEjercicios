tabla = int(input("Tabla a repasar (1-20): "))
correctas = 0

for i in range(1, 11):
    r = int(input(f"{tabla} x {i} = "))
    if r == tabla * i:
        print("Correcto")
        correctas += 1
    else:
        print("Incorrecto. Resultado:", tabla * i)

if correctas <= 5:
    valoracion = "Insuficiente"
elif correctas <= 7:
    valoracion = "Aceptable"
elif correctas <= 9:
    valoracion = "Sobresaliente"
else:
    valoracion = "Excelente"

print("Aciertos:", correctas, "-", valoracion)