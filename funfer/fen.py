def FENamatriz(FEN):
    ''' Recive una posición FEN y 
	   Devuelve una matriz tablero'''
    ta = [[' ' for f in range(8)]for c in range(8)]
    co = [[' ' for f in range(8)]for c in range(8)]  # title
    f = 0
    c = 0

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
    # ic(co)
    # ic(ta)
    return ta, co

#########################
