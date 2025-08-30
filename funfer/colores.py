class ColorIn:
    # Foreground
    F_Default = "\x1b[39m"
    F_Black = "\x1b[30m"
    F_Red = "\x1b[31m"
    F_Green = "\x1b[32m"
    F_Yellow = "\x1b[33m"
    F_Blue = "\x1b[34m"
    F_Magenta = "\x1b[35m"
    F_Cyan = "\x1b[36m"
    F_LightGray = "\x1b[37m"
    F_DarkGray = "\x1b[90m"
    F_LightRed = "\x1b[91m"
    F_LightGreen = "\x1b[92m"
    F_LightYellow = "\x1b[93m"
    F_LightBlue = "\x1b[94m"
    F_LightMagenta = "\x1b[95m"
    F_LightCyan = "\x1b[96m"
    F_White = "\x1b[97m"
    # Background
    B_Default = "\x1b[49m"
    B_Black = "\x1b[40m"
    B_Red = "\x1b[41m"
    B_Green = "\x1b[42m"
    B_Yellow = "\x1b[43m"
    B_Blue = "\x1b[44m"
    B_Magenta = "\x1b[45m"
    B_Cyan = "\x1b[46m"
    B_LightGray = "\x1b[47m"
    B_DarkGray = "\x1b[100m"
    B_LightRed = "\x1b[101m"
    B_LightGreen = "\x1b[102m"
    B_LightYellow = "\x1b[103m"
    B_LightBlue = "\x1b[104m"
    B_LightMagenta = "\x1b[105m"
    B_LightCyan = "\x1b[106m"
    B_White = "\x1b[107m"


class ColorEs:
    # Color de la Letra
    L_PorDefecto = "\x1b[39m"
    L_Negro = "\x1b[30m"
    L_Rojo = "\x1b[31m"
    L_Verde = "\x1b[32m"
    L_Amarillo = "\x1b[33m"
    L_Azul = "\x1b[34m"
    L_Magenta = "\x1b[35m"
    L_Cielo = "\x1b[36m"
    L_GrisClaro = "\x1b[37m"
    L_GrisOscuro = "\x1b[90m"
    L_RojoClaro = "\x1b[91m"
    L_VerdeClaro = "\x1b[92m"
    L_AmarilloClaro = "\x1b[93m"
    L_AzulClaro = "\x1b[94m"
    L_MagentaClaro = "\x1b[95m"
    L_CieloClaro = "\x1b[96m"
    L_Blanco = "\x1b[97m"
    # Color del la Pantalla
    P_PorDefecto = "\x1b[49m"
    P_Negro = "\x1b[40m"
    P_Rojo = "\x1b[41m"
    P_Verde = "\x1b[42m"
    P_Amarillo = "\x1b[43m"
    P_Azul = "\x1b[44m"
    P_Magenta = "\x1b[45m"
    P_Cielo = "\x1b[46m"
    P_GrisClaro = "\x1b[47m"
    P_GrisOscuro = "\x1b[100m"
    P_RojoClaro = "\x1b[101m"
    P_VerdeClaro = "\x1b[102m"
    P_AmarilloClaro = "\x1b[103m"
    P_AzulClaro = "\x1b[104m"
    P_MagentaClaro = "\x1b[105m"
    P_CieloClaro = "\x1b[106m"
    P_Blanco = "\x1b[107m"


# dicionario de Colores
colorDic = {
    # color de la Letra
    "L_Negro": "\x1b[30m",
    "L_Rojo": "\x1b[31m",
    "L_Verde": "\x1b[32m",
    "L_Amarillo": "\x1b[33m",
    "L_Azul": "\x1b[34m",
    "L_Magenta": "\x1b[35m",
    "L_Cielo": "\x1b[36m",
    "L_GrisClaro": "\x1b[37m",
    "L_GrisOscuro": "\x1b[90m",
    "L_RojoClaro": "\x1b[91m",
    "L_VerdeClaro": "\x1b[92m",
    "L_AmarilloClaro": "\x1b[93m",
    "L_AzulClaro": "\x1b[94m",
    "L_MagentaClaro": "\x1b[95m",
    "L_CieloClaro": "\x1b[96m",
    "L_Blanco": "\x1b[97m",
    "L_PorDefecto": "\x1b[39m",
    # color de la Pantalla
    "P_Negro": "\x1b[40m",
    "P_Rojo": "\x1b[41m",
    "P_Verde": "\x1b[42m",
    "P_Amarillo": "\x1b[43m",
    "P_Azul": "\x1b[44m",
    "P_Magenta": "\x1b[45m",
    "P_Cielo": "\x1b[46m",
    "P_GrisClaro": "\x1b[47m",
    "P_GrisOscuro": "\x1b[100m",
    "P_RojoClaro": "\x1b[101m",
    "P_VerdeClaro": "\x1b[102m",
    "P_AmarilloClaro": "\x1b[103m",
    "P_AzulClaro": "\x1b[104m",
    "P_MagentaClaro": "\x1b[105m",
    "P_CieloClaro": "\x1b[106m",
    "P_Blanco": "\x1b[107m",
    "P_PorDefecto": "\x1b[49m",
}

############################
if __name__ == "__main__":

    def colorClase():
        print(ColorEs.L_GrisOscuro, "YUPIII", ColorEs.L_PorDefecto)

        print(ColorEs.L_CieloClaro, "YUPIII", ColorEs.L_PorDefecto)

        print(ColorEs.L_Rojo, ColorEs.P_Azul, "YUPIII", ColorEs.P_PorDefecto)

    #########################
    # colorClase()
    ##########################
    def prueva():
        print(colorDic["L_Rojo"], "hola")
        print(colorDic["L_Verde"], "hola")
        print(colorDic["L_Azul"], "hola")
        print(colorDic["L_PorDefecto"], "hola")

    ###########################
    # prueva()
    ############################
    def prueva1():
        for i in colorDic:
            #  todos los colores disponibles
            print(colorDic[i], "COLORRR")

    ############################
    prueva1()
    ############################

    def color(color, mensaje):
        # pasar el color y el mensaje
        for i in colorDic:
            if i == color:
                print(colorDic[color], mensaje, colorDic["L_PorDefecto"])

    ############################
    # color('L_Amarillo','yupi YUu')
    ##########################

    def colRetornabc(color, mensaje):
        # pasar el color y el mensaje
        for i in colorDic:
            if i == color:
                return colorDic[color], mensaje, colorDic["L_PorDefecto"]

    ############################
    # print(colRetornabc('L_Cielo','colRetorna'))
    ###########################

    def colorRetorna(color, mensaje):
        # pasar el color y el mensaje
        for i in colorDic:
            if i == color:
                return colorDic[color] + mensaje + colorDic["L_PorDefecto"]

    ############################
    # print(colorRetorna('L_Rojo','colorRetorna'))
    ############################
