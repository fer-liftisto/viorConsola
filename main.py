###Fer######################
import sys
import os
from icecream import ic 

from funfer import tablas, traduce, fen, sistema




def una_sola_coma(texto):
    aparicion = texto.count(",")
    texto = texto.replace(",", ":", aparicion - 1)
    return texto


def menu_fen():
    fen_path = resource_path("mate_en_una.txt")
    if os.path.exists(fen_path):
        with open(fen_path, "r", encoding="utf8") as f:
            texto = f.read().strip() # quita espacios al inicio y final
            una_coma = lambda tex: tex.replace(",", ":", tex.count(",") - 1)  # Si hay más de una coma, solo deja la ultima. Antes de fen
            opciones = [tuple(una_coma(tex).split(",")) for tex in texto.split("\n")]
            
    else:
        print("No se encuentra el archivo posiciones_fen.txt")
        return
    
    print("\nElige una posición FEN para mostrar:\n")  # mirar
    
    try:
        for idx, (nombre, _) in enumerate(opciones, 1):
            print(f"{idx}. {nombre}")
    
    except ValueError:
        sistema.limpiar_consola()
        print("\nError al leer las opciones. Asegúrate de que el archivo está correctamente formateado.\n")
        return
    
    while True:
        try:
            eleccion = int(input("\nIntroduce el número de la opción: "))
            if 1 <= eleccion <= len(opciones):
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    _, FEN = opciones[eleccion - 1]
    ic(FEN)
    FEN = FEN.strip().split(" ")
    ic(FEN)
    tablero, color = fen.FENamatriz(FEN[0])
    
    for f in range(8):
        for c in range(8):
            tablero[f][c] = traduce.traduce(tablero[f][c])
    
    tablas.imprimir_tablero(tablero, color)
    
    # A quien le toca jugar
    try:
        if FEN[1] == "w":
            print("Juegan las blancas\n")
        if FEN[1] == "b":
            print("Juegan las negras\n")
    except IndexError:
        pass
    #    
    input("Pulsa una tecla para continuar...")

def resource_path(relative_path):
    """Obtiene la ruta absoluta al recurso, compatible con PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Llama al menú
if __name__ == "__main__":
    ## https: // youtu.be/AMdG7IjgSPM?si = -JYosXsXPQT7igG- ##
    ## https: // youtu.be/AMdG7IjgSPM?si = ww_7gf-Kn_8EO7gl ##
    ## https://youtu.be/qh98qOND6MI?si=vbVet84Oksi9VgHY ##

    ## https://youtu.be/nx4E5LWWMvM?si=AR1yPNUb5DzKqlGe ## ruff
    ## https://youtu.be/nx4E5LWWMvM?si=dach21G_p6F-xDUs ## ruff
    
    # Para establecer una regla de error enruff, 
    # descomentar las siguientes líneas en pyproject.toml:
    #[tool.ruff]
    #lint.extend-select = [
    #    'T201'
    #]
    
    
    print(f"\nRuta de ejecucion: {sys.executable}")
    menu_fen()
