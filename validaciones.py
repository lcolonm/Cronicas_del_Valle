# Valida que la opcion escrita este dentro del rango disponible
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

def validar_texto(mensaje):
    while True:
        # Solo usamos .strip() para quitar espacios extra.
        texto = input(mensaje).strip()
        
        if texto: # Si el texto no está vacío
            return texto
        else:
            print(">> ERROR: El campo no puede quedar vacío. Intenta de nuevo.")

# Automatización de la acción a hacer si la opcion es correcta
def condicion_cumplida():
    pass # Se aprendera en modulo 4... tiste 😓