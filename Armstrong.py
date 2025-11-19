num = int(input("ingrese un numero -> "))
if num > 0:
    armstrong = 0
    for i in str(num):
        armstrong = armstrong + int(i)**3
    if armstrong == num:
        print(f"su numero es armstrong")
    else:
        print(f"su numero no es armstrong")