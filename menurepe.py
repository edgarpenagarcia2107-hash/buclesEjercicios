while True:

    print("\n--- MENÚ DE OPERACIONES ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    
    opcion = input("Seleccione una opción (1-3): ")

    if opcion == "1":
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        resultado = n1 + n2
        print("El resultado de la suma es:", resultado)

    # Opción 2 → Restar
    elif opcion == "2":
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        resultado = n1 - n2
        print("El resultado de la resta es:", resultado)

   
    elif opcion == "3":
        print("Saliendo del programa... Hasta luego")
        break


    else:
        print("Opción inválida. Intente nuevamente.")
