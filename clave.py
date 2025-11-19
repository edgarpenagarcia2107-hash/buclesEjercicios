
clave_correcta = "python123"


intentos = 0

while intentos < 3:
    clave = input("Ingrese la clave: ")
    intentos += 1

    if clave == clave_correcta:
        print(" Acceso permitido.")
        break
    else:
        print(" Clave incorrecta. Intento", intentos, "de 3.")


if intentos == 3 and clave != clave_correcta:
    print(" Acceso denegado. Ha superado el número máximo de intentos.")
