
###Fer######################
from icecream import ic
from colorama import Fore, Back, init
init(autoreset=True)
from funfer import tablas, traduce, fen, colores
# ic.disable()
def menu_fen():
    with open('funfer/posiciones_fen.txt', 'r', encoding='utf8') as f:
        texto = f.read()
        opciones = [tuple(tex.split(',')) for tex in texto.split("\n")]
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
    menu_fen()