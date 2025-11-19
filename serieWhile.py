num  = int(input("ingres la cantidad de terminos a generar -> "))
contador = 0
while contador < num:
    for i  in range(num):
        numerosImpares = i * 2 + 1
        print(numerosImpares)
        contador += 1