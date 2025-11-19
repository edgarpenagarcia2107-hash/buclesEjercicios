cantidadNumeros = int(input("Ingrese la cantidad de números: "))

while cantidadNumeros < 0:
    cantidadNumeros = int(input("Ingrese la cantidad de números: "))
    for numero in range(1, cantidadNumeros + 1):
        print(numero, numero * 2, numero * 3)