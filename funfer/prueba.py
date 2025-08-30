opciones = [
    ("Karo_Cann", "rnbqkbnr/pp1ppppp/2p5/8/4P3/8/PPPP1PPP/RNBQKBNR"),
    ("Lima-Quinn (Erevan, 1996)", "1r6/1b2kPp1/pp1nP1Bp/3q4/PP6/8/5QPP/4R1K1"),
    ("Mate en 2", "1Rbkrn2/2p1p3/p2n4/2N3Nq/Q5p1/P7/1P6/K1B5"),
    (
        "Torhallsson-Chavez (Erevan,1996)",
        "4rr1k/4qp1p/4p1p1/3pP1Rb/pp1N1Q2/7B/PPP4P/2K2R2",
    ),
    ("Posición inicial", "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"),
]

if __name__ == "__main__":
    # <cont + shiff + p> y luego buscar ruff para ver las opciones de ruff
    # Opciones_fen es una lista de tuplas de dos elementos (nombre y fen)
    ############################################################################    
    def visualizar1(opciones_fen):
        return "\n".join(
            [f"{nombre}, {fen}" for nombre, fen in opciones_fen]
        )  ###FER###

    def visualizar2(opciones_fen):
        return "\n".join([" , ".join(linea) for linea in opciones_fen])  ####FER###

    visualizar3 = lambda opciones_fen: "\n".join([f"{nombre}, {fen}" for nombre, fen in opciones_fen])  ###FER###

    print(visualizar3(opciones))
    print("_" * 50)

    texto = visualizar1(opciones)
    print(texto)
    print("_" * 50)

    texto = visualizar2(opciones)
    print(texto)

    print("*" * 50)

    def visualiza_lista(lista_opciones):
        print("opciones = [")
        for i, valor in enumerate(lista_opciones, 1):
            if len(lista_opciones) > i:
                print(valor, ",")
            else:
                print(valor)
        print("]")

    ############################################################################
    lista_opciones = [tuple(tex.split(",")) for tex in texto.split("\n")]
    print(lista_opciones)
    visualiza_lista(lista_opciones)

    print("*" * 50)
# texto = ", ".join(opciones[0] + opciones[1] + opciones[2] + opciones[3] + opciones[4]).strip(', ')

# print("\x1b[36m" + texto + "\x1b[0m")  # Reset color
# print("\n".join(texto))
