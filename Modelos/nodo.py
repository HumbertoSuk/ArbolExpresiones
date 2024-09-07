"""
Nodo
"""


class Nodo:
    """
    Entity Nodo del arbol 
    """

    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
