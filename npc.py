
#1. Fabrica de NPC 
def crear_npc(nombre, rol, vida, defensa, ataque):
    return {
        "nombre": nombre,
        "rol": rol,
        
        "stats": {
            "vida": vida,
            "defensa": defensa,
            "ataque": ataque,
        },

        "dialogos": [],

    }