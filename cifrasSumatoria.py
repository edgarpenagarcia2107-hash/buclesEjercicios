num = int(input("ingrese un numero -> "))
if num > 0:
    length = len(str(num))
    sumatoria = 0
    for i in range(1, length + 1):
        sumatoria = sumatoria + i
    print(f"su numero es positivo, la longitud es -> {length}\
          y la sumatoria es -> {sumatoria}")