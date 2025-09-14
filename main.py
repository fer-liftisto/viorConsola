###Fer######################
import sys
from icecream import ic 

from funfer import tablas, fen, sistema
##########################################################################

def menu_fen():
    otra_vez = True
    while True:
        if  otra_vez:
            menu = "seleccion_archivos.txt"
            que_quieres = fen.seleccionar_nombre_fichero(menu)
        
            print("\nElige una coleccion para mostrar:\n")
            fichero = fen.elelige_una_opcion(que_quieres)
        # fichero = "posiciones_fen.txt"
        opciones = fen.selecionar_fichero_fen(fichero) # lista de tuplas (nombre, FEN)
        otra_vez = False
        print("\nElige una posición FEN para mostrar:\n")  # mirar
        FEN= fen.elige_opcion_mostrar(opciones)
        #  FEN= ["5Br1/6P1/5KBk/8/8/8/8/8", "w", "-", "-", "-", "-"]
        
        tablero, color = fen.FENamatriz(FEN[0])  
        
        tablero = tablas.traduce_ingles_a_piezas(tablero)
        
        tablas.imprimir_tablero(tablero, color)
        
        tablas.a_quien_le_toca_jugar(FEN)
    
        opc= input("Pulsa Cambiar, Salir o una tecla para continuar... ")
        if opc.lower() == 'salir':
            print("Saliendo del programa...")
            break
        elif opc.lower() == 'cambiar':
            otra_vez = True

# Llama al menú
if __name__ == "__main__":
    ## https: // youtu.be/AMdG7IjgSPM?si = -JYosXsXPQT7igG- ##
    ## https: // youtu.be/AMdG7IjgSPM?si = ww_7gf-Kn_8EO7gl ##
    ## https://youtu.be/qh98qOND6MI?si=vbVet84Oksi9VgHY ##

    ## https://youtu.be/nx4E5LWWMvM?si=AR1yPNUb5DzKqlGe ## ruff
    ## https://youtu.be/nx4E5LWWMvM?si=dach21G_p6F-xDUs ## ruff
    
    # Para establecer una regla de error enruff, 
    # descomentar las siguientes líneas en pyproject.toml:
    #[tool.ruff]
    #lint.extend-select = [
    #    'T201'
    #]
    
    
    print(f"\nRuta de ejecucion: {sys.executable}")
    sistema.limpiar_consola()
    menu_fen()
