valorX = int(input("Ingrese el máximo valor para x: "))

while valorX < 0:
    valorX = int(input("Ingrese el máximo valor para x: "))

for x in range(0, valorX + 1, 2):
    funcion = x**3 + x**2 - 5
    print("Para x =", x, "f(x) =", funcion)