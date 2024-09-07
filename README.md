# Generador de Árbol de Expresión

Este proyecto es un programa en Python que genera un **árbol de expresión** a partir de una expresión matemática ingresada por el usuario. El programa incluye una interfaz gráfica (GUI) que permite visualizar la estructura jerárquica de la expresión de manera interactiva.

## Funcionalidades

- Entrada de expresiones matemáticas.
- Generación automática de un árbol de expresión.
- Visualización gráfica del árbol.

## Estructura del Proyecto

- **Controllers/**: Lógica de generación y evaluación del árbol.
- **Screens/**: Interfaz gráfica para la interacción del usuario.
- **Modelos/**: Manejo de los datos y análisis de la expresión.
- **utils/**: Helpers y metodos auxiliares.
- **main.py**: Punto de entrada del programa.
- **README.md**: Descripción del proyecto.
- **requirements.txt**: requirimientos del programa.

## Requisitos

- Python 3.x
- Librerías:
  - `tkinter` (para la GUI)
  - `matplotlib` (para la visualización del árbol)
  - `networkx` (Graficacion del arbol)

Para instalar las dependencias, puedes ejecutar:

```bash
pip install -r requirements.txt
```

## Ejecutar

```bash
python main.py
```
