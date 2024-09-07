"""
    Arbol
"""
import re
from Modelos.nodo import Nodo


class ArbolDeExpresion:
    """
    Clase que representa un Árbol de Expresión Aritmética. 
    Permite construir un árbol a partir de una expresión infija y evaluarlo.
    También proporciona recorridos del árbol (inorden, preorden, postorden).
    """

    OPERADORES = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def __init__(self):
        """
        Inicializa un árbol de expresión con la raíz vacía.
        """
        self.raiz = None

    def construir_arbol(self, expresion):
        """
        Construye un árbol de expresión a partir de una expresión aritmética en notación infija.
        Utiliza un algoritmo basado en pilas para convertir la expresión infija en un árbol.

        Args:
            expresion (str): La expresión aritmética en notación infija que se utilizará para
                             construir el árbol de expresión.

        Raises:
            ValueError: Si se encuentra un operador inválido durante la construcción del árbol.
        """
        tokens = self.tokenizar_expresion(expresion)
        pila_nodos = []
        pila_operadores = []

        for token in tokens:
            if self.es_numero(token):
                nodo = Nodo(float(token))
                pila_nodos.append(nodo)
            elif token == '(':
                pila_operadores.append(token)
            elif token == ')':
                while pila_operadores and pila_operadores[-1] != '(':
                    self.procesar_operador(pila_nodos, pila_operadores.pop())
                pila_operadores.pop()
            elif token in self.OPERADORES:
                while (pila_operadores and pila_operadores[-1] != '(' and
                       self.OPERADORES.get(pila_operadores[-1], 0) >= self.OPERADORES[token]):
                    self.procesar_operador(pila_nodos, pila_operadores.pop())
                pila_operadores.append(token)

        # Procesar cualquier operador restante
        while pila_operadores:
            self.procesar_operador(pila_nodos, pila_operadores.pop())

        # La raíz del árbol es el último nodo en la pila
        self.raiz = pila_nodos.pop()

    def procesar_operador(self, pila_nodos, operador):
        """
        Procesa un operador extrayendo los dos operandos correspondientes de la pila de nodos
        y creando un nodo con el operador como raíz.

        Args:
            pila_nodos (list): Pila que contiene los nodos de los operandos.
            operador (str): El operador que se aplicará a los operandos.
        """
        nodo = Nodo(operador)
        nodo.der = pila_nodos.pop()  # Operando derecho
        nodo.izq = pila_nodos.pop()  # Operando izquierdo
        pila_nodos.append(nodo)

    def tokenizar_expresion(self, expresion):
        """
        Convierte una expresión aritmética en una lista de tokens 
        (números, operadores y paréntesis).

        Args:
            expresion (str): La expresión aritmética a tokenizar.

        Returns:
            list: Lista de tokens que contiene números, operadores y paréntesis.
        """
        patron = r'\d+\.?\d*|[+*/^()-]'
        tokens = re.findall(patron, expresion)
        return tokens

    def es_numero(self, token):
        """
        Verifica si un token es un número.

        Args:
            token (str): El token a verificar.

        Returns:
            bool: True si el token es un número, False si no lo es.
        """
        try:
            float(token)
            return True
        except ValueError:
            return False

    def evaluar_arbol(self, nodo):
        """
        Evalúa recursivamente el árbol de expresión para calcular el resultado aritmético.

        Args:
            nodo (Nodo): El nodo raíz del árbol o subárbol que se va a evaluar.

        Returns:
            float: El resultado de evaluar la expresión representada por el árbol.

        Raises:
            ZeroDivisionError: Si se intenta realizar una división por cero.
            ValueError: Si se encuentra un operador desconocido.
        """
        if nodo.izq is None and nodo.der is None:
            return nodo.valor  # Caso base: Nodo hoja (número)

        # Evaluar los subárboles izquierdo y derecho
        izq_valor = self.evaluar_arbol(nodo.izq)
        der_valor = self.evaluar_arbol(nodo.der)

        # Aplicar el operador en el nodo actual
        if nodo.valor == '+':
            return izq_valor + der_valor
        elif nodo.valor == '-':
            return izq_valor - der_valor
        elif nodo.valor == '*':
            return izq_valor * der_valor
        elif nodo.valor == '/':
            if der_valor == 0:
                raise ZeroDivisionError("Error: División entre cero.")
            return izq_valor / der_valor
        elif nodo.valor == '^':
            return izq_valor ** der_valor
        else:
            raise ValueError(f"Operador desconocido: {nodo.valor}")

    def imprimir_inorden(self, nodo, resultado=""):
        """
        Genera una representación en orden (inorden) de la expresión.

        Args:
            nodo (Nodo): El nodo raíz del árbol o subárbol a recorrer.
            resultado (str): El recorrido acumulado de la expresión.

        Returns:
            str: La expresión aritmética recorrida en inorden.
        """
        if nodo:
            resultado = self.imprimir_inorden(nodo.izq, resultado)
            resultado += f" {nodo.valor} "
            resultado = self.imprimir_inorden(nodo.der, resultado)
        return resultado

    def imprimir_preorden(self, nodo, resultado=""):
        """
        Genera una representación en preorden de la expresión.

        Args:
            nodo (Nodo): El nodo raíz del árbol o subárbol a recorrer.
            resultado (str): El recorrido acumulado de la expresión.

        Returns:
            str: La expresión aritmética recorrida en preorden.
        """
        if nodo:
            resultado += f" {nodo.valor} "
            resultado = self.imprimir_preorden(nodo.izq, resultado)
            resultado = self.imprimir_preorden(nodo.der, resultado)
        return resultado

    def imprimir_postorden(self, nodo, resultado=""):
        """
        Genera una representación en postorden de la expresión.

        Args:
            nodo (Nodo): El nodo raíz del árbol o subárbol a recorrer.
            resultado (str): El recorrido acumulado de la expresión.

        Returns:
            str: La expresión aritmética recorrida en postorden.
        """
        if nodo:
            resultado = self.imprimir_postorden(nodo.izq, resultado)
            resultado = self.imprimir_postorden(nodo.der, resultado)
            resultado += f" {nodo.valor} "
        return resultado
