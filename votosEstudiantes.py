android = 0
ios = 0

n = int(input("¿Cuántos estudiantes van a votar?: "))

for i in range(n):
    codigo = input("Digite su código: ")
    voto = input("Elija plataforma (Android / iOS): ").lower()

    if voto == "android":
        android += 1
    elif voto == "ios":
        ios += 1
    else:
        print("Plataforma inválida. El voto NO se contará.\n")

print(" RESULTADOS ")
print("Votos Android:", android)
print("Votos iOS:", ios)

if android > ios:
    print("La plataforma elegida es ANDROID.")
elif ios > android:
    print("La plataforma elegida es iOS.")
else:
    print("Hay un EMPATE. Se deberá usar otro mecanismo de elección.")