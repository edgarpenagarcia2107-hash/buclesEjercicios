
n = int(input("Ingrese un número entero mayor que 1: "))

es_primo = True  

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        es_primo = False  
        break  

if es_primo:
    print(n, "es un número primo.")
else:
    print(n, "NO es un número primo.")
