###FER###
#from icecream import ic
from colorama import Style, Fore, Back, init
init(autoreset=True)  # autoreset = True

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
    print("  a b c d  e f g h")
    #print("  +" + "---+"*8)
    # ic(tablecolor)
    for ifi, fila in enumerate(tablecolor):
        print(f"{8-ifi} ", end="")

        for ico, pieza in enumerate(fila):
            # ic(pieza[0])
            if ((8-ifi) + ico) % 2 == 0:
                cuadro_color = Back.LIGHTBLUE_EX
            else:
                cuadro_color = Back.LIGHTRED_EX
            
            if pieza[1] == 'W':
                print(
                    f"{cuadro_color + Fore.GREEN + pieza[0]} ", end="")
            if pieza[1] == 'B':
                print(
                    f"{cuadro_color + Fore.BLACK + pieza[0]} ", end="")
            if pieza[1] == ' ':
                print(
                    f"{cuadro_color + pieza[0]} ", end="")
            print(Style.RESET_ALL, end="")
        print(f" {8-ifi}")
        #print("  +" + "---+"*8)
    print("  a b c d  e f g h\n")
    #print(f"{Back.LIGHTRED_EX + Fore.BLACK + 'yupi'} ")
#________________________________________________________________
if __name__ == "__main__":
    # Definición de un tablero y colores
    tablero = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
               ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
               ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]
    
    colores = [['W'] * 8, ['W'] * 8, [' '] * 8, [' '] * 8,
              [' '] * 8, [' '] * 8, ['B'] * 8, ['B'] * 8]
    
    tablero_coloreado = poner_color(tablero, colores)
    #ic(tablero_coloreado)    

    a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

    b = [['a', 'b', 'c'],
     ['d', 'e', 'f'],
     ['g', 'h', 'i']] 

    tablero= poner_color(a, b)   
    #ic(tablero)
    