###FER###
from icecream import ic

def poner_color(tablero, color):
    ''' Añade el color a cada pieza del tablero '''
    
    table_col = list(zip(tablero, color))
    
    retorno=[]
    for fila in table_col:
        union=list(zip(*fila))
        retorno.append(union)
    
    return retorno
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
    