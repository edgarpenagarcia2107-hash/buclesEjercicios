
N = int(input("Ingrese un número entero positivo: "))


a, b = 0, 1

print("Serie de Fibonacci hasta", N, ":")

while a <= N:
    print(a, end=", ")
    a, b = b, a + b
