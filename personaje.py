from interfaz import genero_pj
from validaciones import validar_dato, validar_texto

CATALOGO_CLASES = {
    
    # vida base: 100, 
    # ataque base: 10, 
    # defensa base: 10

    "Tanque": {
        "stats": {
        "vida": 200,
        "ataque": 5,
        "defensa": 15,
        },
        "rama_habilidades": [],
        "caminos_evolucion": [],
    },

    "Guerrero": {
    "stats": {
    "vida": 100,
    "ataque": 15,
    "defensa": 10,
    },
    "rama_habilidades": [],
    "caminos_evolucion": [],
    },

    "Arquero": {
        "stats": {
        "vida": 50,
        "ataque": 25,
        "defensa": 5,
        },
        "rama_habilidades": [],
        "caminos_evolucion": [],
        },
    
    "Clerigo": {
        "stats": {
        "vida": 90,
        "ataque": 6,
        "defensa": 9,
        },
        "rama_habilidades": [],
        "caminos_evolucion": [],
        },

}

def menu_genero():

    genero_pj()

    # 1. Guardamos la opción numérica del usuario
    opcion = validar_dato(">> SELECCIONE UNA ACCIÓN: ", 3)

    # Mapeamos la opción a una llave de texto
    if opcion == 1:
        genero = "Femenino"
    elif opcion == 2:
        genero = "Masculino"
    else:
        genero = "No Binario"

    return genero

def menu_clase():

    # 1. Guardamos la opción numérica del usuario
    opcion = validar_dato(">> SELECCIONE UNA ACCIÓN: ", 4)
    
    if opcion == 1:
        return "Tanque"
    elif opcion == 2:
        return "Guerrero"
    elif opcion == 3:
        return "Arquero"
    else:
        return "Clerigo"

def crear_personaje():

    nombre = validar_texto(">> INGRESA TU NOMBRE: ")

    genero = menu_genero()
    clase = menu_clase()
    datos_clase = CATALOGO_CLASES[clase]

    jugador = {
        "nombre": nombre,
        "genero": genero,
        "clase": clase,
        "stats": datos_clase["stats"],
        "rama_habilidades": datos_clase["rama_habilidades"], 
        "inventario": [],
    }
    
    return jugador

