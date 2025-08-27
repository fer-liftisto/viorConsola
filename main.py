
###Fer######################
import sys
from icecream import ic
from colorama import Fore, Back, init
init(autoreset=True)
from funfer import tablas, traduce, fen, colores
# ic.disable()
def una_sola_coma(texto):
    aparicion = texto.count(',')
    texto = texto.replace(',', ':', aparicion - 1)
    return texto


def menu_fen():
    with open('funfer/posiciones_fen.txt', 'r', encoding='utf8') as f:
        texto = f.read()
        una_coma = lambda texto : texto.replace(',',':',texto.count(',') -1) # Si hay más de una coma, solo deja la ultima. Antes de fen
        opciones = [tuple(una_coma(tex).split(',')) for tex in texto.split("\n")]
        ic(opciones)
    
    
    
    print("\nElige una posición FEN para mostrar:\n") #mirar
    for idx, (nombre, _) in enumerate(opciones, 1):
        ic(nombre)
        print(f"{idx}. {nombre}")
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
    tablero, color = fen.FENamatriz(FEN)
    for f in range(8):
        for c in range(8):
            pass
            tablero[f][c] = traduce.traduce(tablero[f][c])
    
    tablas.imprimir_tablero(tablero, color)

# Llama al menú
if __name__ == "__main__":
    ## https: // youtu.be/AMdG7IjgSPM?si = -JYosXsXPQT7igG- ##
    ## https: // youtu.be/AMdG7IjgSPM?si = ww_7gf-Kn_8EO7gl ##
    ic("Python executable path:")
    print(sys.executable)
    menu_fen()