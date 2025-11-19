
N = int(input("Ingrese el primer número (N): "))
M = int(input("Ingrese el segundo número (M): "))

encontrado = False

for i in range(N + 1, M):
    if i % 9 == 0:
        print("El primer número divisible por 9 en el rango es:", i)
        encontrado = True
        break  

if not encontrado:
    print("No hay números divisibles por 9 en el rango dado.")
