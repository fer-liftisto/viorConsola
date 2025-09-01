
import os
def limpiar_consola():
    """Limpia la consola en Windows, Linux y macOS."""
    # Para Windows
    if os.name == "nt":
        os.system("cls")
    # Para Linux y macOS
    else:
        os.system("clear")
