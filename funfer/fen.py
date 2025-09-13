
import sys
import os
from icecream import ic

def FENamatriz(FEN):
    """Recive una posición FEN y
    Devuelve una matriz tablero"""
    ta = [[" " for f in range(8)] for c in range(8)]
    co = [[" " for f in range(8)] for c in range(8)]  # title
    f = 0
    c = 0

    for i in FEN:
        if i.isnumeric():
            c += int(i)

        elif i.isalpha():
            ta[f][c] = i
            if i.islower():
                co[f][c] = "B"
            else:
                co[f][c] = "W"
            c += 1

        elif i == "/":
            f += 1
            c = 0
    # ic(co)
    # ic(ta)
    return ta, co
##############################################################################
def resource_path(relative_path):
    """Obtiene la ruta absoluta al recurso, compatible con PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

####################################################################################
def selecionar_fichero_fen(fichero):
    """Selecciona un fichero de posiciones FEN y devuelve su contenido"""
    fen_path = resource_path(fichero)
    if os.path.exists(fen_path):
        with open(fen_path, "r", encoding="utf8") as f:
            texto = f.read().strip() # quita espacios al inicio y final
            una_coma = lambda tex: tex.replace(",", ":", tex.count(",") - 1)  # Si hay más de una coma, solo deja la ultima. Antes de fen
            opciones = [tuple(una_coma(tex).split(",")) for tex in texto.split("\n")]
        return opciones   
    else:
        print("No se encuentra el archivo posicione")

def elige_opcion_mostrar(opciones):
    try:
        for idx, (nombre, _) in enumerate(opciones, 1):
            print(f"{idx}. {nombre}")  # muestra opciones

    except ValueError:
        print(
            "\nError al leer las opciones. Asegúrate de que el archivo está correctamente formateado.\n"
        )
        return

    while True:
        # Validar la entrada del usuario
        try:
            eleccion = int(input("\nIntroduce el número de la opción: "))
            if 1 <= eleccion <= len(opciones):
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce un número válido.")

    _, FEN = opciones[eleccion - 1]
    # fen= ' 5r1k/1pr1qpp1/p2Nb3/2P1P3/1P2QR2/6Rp/6P1/7K w'
    return FEN.strip().split(" ")
    
########################################################################################################## 

def seleccionar_nombre_fichero(fichero):
    """Selecciona un fichero de posiciones FEN y devuelve su contenido"""
    fen_path = resource_path(fichero)
    if os.path.exists(fen_path):
        with open(fen_path, "r", encoding="utf8") as f:
            opciones = f.read().strip() # quita espacios al inicio y final
            opciones = [opt for opt in opciones.split("\n")]
        return opciones
   
    else:
        print("No se encuentra el archivo posicione")

############################################################################################
def elelige_una_opcion(opciones):
    try:
        for idx, nombre in enumerate(opciones, 1):
            print(f"{idx}. {nombre}")  # muestra opciones

    except ValueError:
        
        print(
            "\nError al leer las opciones. Asegúrate de que el archivo está correctamente formateado.\n"
        )
        return

    while True:
        # Validar la entrada del usuario
        try:
            eleccion = int(input("\nIntroduce el número de la opción: "))
            if 1 <= eleccion <= len(opciones):
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce un número válido.")

    return opciones[eleccion - 1].strip()

             
###############################################################################