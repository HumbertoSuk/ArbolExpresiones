"""
Helper functions.
Funciones helper para ayudar a validar datos
"""
import re


def validar_expresion(expresion):
    """
    Valida que la expresión aritmética solo contenga números, operadores y paréntesis.

    Args:
        expresion (str): La expresión aritmética a validar.

    Returns:
        bool: True si la expresión es válida, False en caso contrario.
    """
    patron = r'^[\d+\-*/^(). ]+$'
    return bool(re.match(patron, expresion))


def eliminar_espacios(expresion):
    """
    Elimina todos los espacios en blanco de la expresión aritmética.

    Args:
        expresion (str): La expresión aritmética con posibles espacios.

    Returns:
        str: La expresión sin espacios.
    """
    return expresion.replace(" ", "")


def balancear_parentesis(expresion):
    """
    Verifica si los paréntesis de la expresión están balanceados.

    Args:
        expresion (str): La expresión aritmética a validar.

    Returns:
        bool: True si los paréntesis están balanceados, False en caso contrario.
    """
    stack = []
    for char in expresion:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


def tokenizar_expresion(expresion):
    """
    Convierte una expresión aritmética en una lista de tokens (números, operadores y paréntesis).

    Args:
        expresion (str): La expresión aritmética a tokenizar.

    Returns:
        list: Una lista de tokens que contiene números, operadores y paréntesis.
    """
    patron = r'\d+\.?\d*|[+*/^()-]'
    return re.findall(patron, expresion)


def es_numero(token):
    """
    Verifica si un token es un número.

    Args:
        token (str): El token a verificar.

    Returns:
        bool: True si el token es un número, False en caso contrario.
    """
    try:
        float(token)
        return True
    except ValueError:
        return False
