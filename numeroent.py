
n = int(input("Ingrese un número entero: "))


signo = -1 if n < 0 else 1

n = abs(n)


invertido = 0


while n > 0:
    digito = n % 10          
    invertido = invertido * 10 + digito  
    n = n // 10            


invertido *= signo

print("Número invertido:", invertido)
