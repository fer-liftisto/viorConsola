
###Fer######################
#from icecream import ic
from colorama import Fore, Back, init
init(autoreset=True)
from funfer import tablas, traduce, fen, colores
# ic.disable()
def menu_fen():
    opciones = [
        ("Karo_Cann", 'rnbqkbnr/pp1ppppp/2p5/8/4P3/8/PPPP1PPP/RNBQKBNR'),
        ("Lima-Quinn (Erevan, 1996)", '1r6/1b2kPp1/pp1nP1Bp/3q4/PP6/8/5QPP/4R1K1'),
        ("Mate en 2", '1Rbkrn2/2p1p3/p2n4/2N3Nq/Q5p1/P7/1P6/K1B5'),
        ("Torhallsson-Chavez (Erevan,1996)", '4rr1k/4qp1p/4p1p1/3pP1Rb/pp1N1Q2/7B/PPP4P/2K2R2'),
        ("Posición inicial", 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
    ]
    print("\nElige una posición FEN para mostrar:\n") #mirar
    for idx, (nombre, _) in enumerate(opciones, 1):
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