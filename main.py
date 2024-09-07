"""
@Author: Humberto Lopez
@Author: Kevin 
@Author: 

Ejecucion del programa principal
"""
import tkinter as tk
from Controllers.controller_arbol import Controlador
from Screens.view import Vista


def main():
    """
    Ejecuta la vista con el controlador
    """
    root = tk.Tk()
    vista = Vista(root)
    controlador = Controlador(vista)
    root.mainloop()


if __name__ == "__main__":
    main()
