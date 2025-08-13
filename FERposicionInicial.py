###Fer######################
from icecream import ic
# ic.disable()
def FENamatriz(FEN):
    ''' Recive una posición FEN y 
	   Devuelve una matriz tablero'''
    ta=[[' ' for f in range(8)]for c in range(8)]
    co = [[' ' for f in range(8)]for c in range(8)] #title
    f=0
    c=0
    
    for i in FEN:
        if i.isnumeric():
            c += int(i)
        
        elif i.isalpha():
            ta[f][c] = i
            if i.islower():
                co[f][c] = 'B'
            else:
                co[f][c] = 'W'
            c += 1
            
        elif i == '/':
            f += 1
            c = 0
    #ic(co)
    #ic(ta)
    return ta, co

#########################		
def traduce(f):
		''' Traduce de carácter a símbolo '''
		# '♟♜♞♝♛♚' #
		
		f= f.replace('R','♜')
		f= f.replace('N','♞')
		f= f.replace('B','♝')
		f= f.replace('Q','♛')
		f= f.replace('K','♚')
		f= f.replace('P','♟')
		
		f= f.replace('r','♜')
		f= f.replace('n','♞')
		f= f.replace('b','♝')
		f= f.replace('q','♛')
		f= f.replace('k','♚')
		f= f.replace('p','♟')
			
		return f
		

def imprimir_tablero(tablero, color):
    
    #ic(tablero)
    #ic(color)
    tablecolor = list(zip(tablero, color))
    print("\n  Tablero de ajedrez:")
    print("    a   b   c   d   e   f   g   h")
    print("  +" + "---+"*8)
    ic(tablecolor)
    for i, fila in enumerate(tablecolor):
        print(f"{8-i} |", end="")  
        ic(fila)
        filacol= list(zip(fila))  # Transponer para iterar por piezas y colores
        for pieza in filacol:
            ic(pieza[0])
            if pieza[0] == 'W':
                print(f" {pieza[0]} |", end="")
        print(f" {8-i}")
        print("  +" + "---+"*8)
    print("    a   b   c   d   e   f   g   h")

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
    tablero, color = FENamatriz(FEN)
    for f in range(8):
        for c in range(8):
            tablero[f][c] = traduce(tablero[f][c])
    
    imprimir_tablero(tablero, color)

# Llama al menú
if __name__ == "__main__":
    menu_fen()