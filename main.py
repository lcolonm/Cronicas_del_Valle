from personaje import crear_personaje
from validaciones import validar_dato


def menu_principal():

    print("⚔️🤺 CRONICAS DEL VALLE 🧙🏼‍♂️✨")
    print("""\n
    [1] Nuevo Juego.
    [2] Cargar Partida.
    [3] Configuración.
    [4] Salir.
    """)

    # VALIDAR DATO Y SELECCIONAR OPCION 
    while True:
        opcion = validar_dato(">> SELECCIONE UNA ACCIÓN: ", 4)

        if opcion == 1:

            print(">> CARGANDO ENTORNO DE JUEGO...")
            crear_jugador = crear_personaje()

            print("\n" + "="*40)

            print("¡PERSONAJE CREADO CON ÉXITO!".center(40))
            print("="*40)
            print(f"Nombre: {crear_jugador['nombre']}")
            print(f"Género: {crear_jugador['genero']}")
            print(f"Clase:  {crear_jugador['clase']}")
            print(f"Vida inicial:   {crear_jugador['stats']['vida']}")
            print(f"Ataque inicial: {crear_jugador['stats']['ataque']}")

            print("="*40 + "\n")
            
            break

        elif opcion == 2:
            print(">> BUSCANDO ARCHIVOS DE GUARDADO...")
        elif opcion == 3:
            print(">> ABRIENDO CONFIGURACIÓN...")
        elif opcion == 4:
            print("CERRANDO JUEGO... ADIÓS.")
            break

menu_principal()