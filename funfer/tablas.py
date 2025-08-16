###FER###
from icecream import ic
from colorama import Fore, Back, Cursor, init
init() #autoreset = True

def poner_color(tablero, color):
    ''' Añade el color a cada pieza del tablero '''
    
    table_col = list(zip(tablero, color))
    
    retorno=[]
    for fila in table_col:
        union=list(zip(*fila))
        retorno.append(union)
    
    return retorno


def imprimir_tablero(tablero, color):

    # ic(tablero)
    # ic(color)
    tablecolor = poner_color(tablero, color)
    print("\n  Tablero de ajedrez:")
    print("    a   b   c   d   e   f   g   h")
    print("  +" + "---+"*8)
    # ic(tablecolor)
    for ifi, fila in enumerate(tablecolor):
        print(f"{8-ifi} |", end="")

        for ico, pieza in enumerate(fila):
            # ic(pieza[0])
            if ((8-ifi) + ico) % 2 == 0:
                cuadro_color = Back.BLUE
            else:
                cuadro_color = Back.RED
            
            if pieza[1] == 'W':
                print(cuadro_color +
                      f" {Fore.GREEN + pieza[0]} "+ Back.RESET + Fore.RESET + "|", end="")
            if pieza[1] == 'B':
                print(cuadro_color +
                      f" {cuadro_color + Fore.CYAN + pieza[0]} "+ Back.RESET + Fore.RESET + "|", end="")
            if pieza[1] == ' ':
                print(cuadro_color +
                      f" {cuadro_color + pieza[0]} " + Back.RESET + Fore.RESET + "|", end="")

        print(f" {8-ifi}")
        print("  +" + "---+"*8)
    print("    a   b   c   d   e   f   g   h")

#________________________________________________________________
if __name__ == "__main__":
    # Definición de un tablero y colores
    tablero = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
               ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
               ['.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.'],
               ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
               ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]
    
    colores = [['W'] * 8, ['W'] * 8, ['.'] * 8, ['.'] * 8,
              ['.'] * 8, ['.'] * 8, ['B'] * 8, ['B'] * 8]
    
    tablero_coloreado = poner_color(tablero, colores)
    ic(tablero_coloreado)    

    a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

    b = [['a', 'b', 'c'],
     ['d', 'e', 'f'],
     ['g', 'h', 'i']] 

    tablero= poner_color(a, b)   
    ic(tablero)
    