###FER###
# from icecream import ic
# ic.disable()

# proyectos uso ficheros y excel#
# https: // youtu.be/RaEatqpugCk?si = pojxoNS_X8nxCiL9#

from colorama import  Fore, init, Back, Style   
from icecream import ic

init(autoreset=True)  # autoreset = True


def poner_color(tablero, color):
    """Añade el color a cada pieza del tablero"""

    table_col = list(zip(tablero, color))

    retorno = []
    for fila in table_col:
        union = list(zip(*fila))
        retorno.append(union)
    ic(retorno)
    return retorno


def imprimir_tablero(tablero, color):
    """Imprime el tablero de ajedrez con colores"""    
    tablecolor = poner_color(tablero, color)
    print("\n Tablero de ajedrez:")
    print("  a b c d  e f g h")
    
    for ifi, fila in enumerate(tablecolor):
        print(f"{8 - ifi} ", end="")

        for ico, pieza in enumerate(fila):
            
            if ((8 - ifi) + ico) % 2 == 0:
                cuadro_color =  Back.WHITE
            else:
                cuadro_color = Back.YELLOW 

            if pieza[1] == "W":
                print(f"{cuadro_color + Fore.MAGENTA + pieza[0]} ", end="")
            elif pieza[1] == "B":
                print(f"{cuadro_color + Fore.BLUE + pieza[0]} ", end="")
            
            elif pieza[1] == " ":
                print(f"{cuadro_color + pieza[0]} ", end="")
            Style.RESET_ALL
        print(f" {8 - ifi}")

    print("  a b c d  e f g h\n")

    
    
# ________________________________________________________________
if __name__ == "__main__":
    # Definición de un tablero y colores
    tablero = [
        ["R", "N", "B", "Q", "K", "B", "N", "R"],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        ["r", "n", "b", "q", "k", "b", "n", "r"],
    ]

    colores = [
        ["W"] * 8,
        ["W"] * 8,
        [" "] * 8,
        [" "] * 8,
        [" "] * 8,
        [" "] * 8,
        ["B"] * 8,
        ["B"] * 8,
    ]

    tablero_coloreado = poner_color(tablero, colores)

    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    b = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

    tablero = poner_color(a, b)
