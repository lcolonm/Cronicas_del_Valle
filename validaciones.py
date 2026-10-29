def validar_dato(mensaje, opcion_max):

    opciones_validas = list(range(1, opcion_max + 1))
    
    while True:
        try:
            opcion = int(input(mensaje))

            if opcion in opciones_validas:
                return opcion
            else:
                print(">> ERROR: Esa opción no está disponible.")

        except ValueError:
            print(f">> ERROR: Ingresé un número válido ({opciones_validas}).")