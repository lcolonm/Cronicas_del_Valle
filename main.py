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
        elif opcion == 2:
            print(">> BUSCANDO ARCHIVOS DE GUARDADO...")
        elif opcion == 3:
            print(">> ABRIENDO CONFIGURACIÓN...")
        elif opcion == 4:
            print("CERRANDO JUEGO... ADIÓS.")
            break

menu_principal()
