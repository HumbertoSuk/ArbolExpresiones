""" 
Graficador del arbol 
"""
import matplotlib.pyplot as plt
import networkx as nx


class ArbolVisualizer:
    """
    Clase que se encarga de la visualización gráfica de un árbol de expresión utilizando
    matplotlib y networkx. Permite graficar el árbol con una estética personalizada.
    """

    def __init__(self, arbol):
        """
        Inicializa el visualizador con el árbol de expresión.

        Args:
            arbol (ArbolDeExpresion): El árbol de expresión que será visualizado.
        """
        self.arbol = arbol

    def graficar_arbol(self):
        """
        Genera la visualización gráfica del árbol de expresión utilizando un grafo dirigido
        (networkx) y matplotlib. El gráfico es representado con una estética personalizada.
        """
        grafo = nx.DiGraph()
        posiciones = {}
        etiquetas = {}

        # Función interna para agregar nodos y aristas al grafo
        def agregar_nodos_aristas(nodo, x=0, y=0, espaciado=1.5):
            """
            Recorre el árbol recursivamente para añadir nodos y aristas al grafo.

            Args:
                nodo (Nodo): Nodo actual del árbol.
                x (float): Coordenada X del nodo en el gráfico.
                y (float): Coordenada Y del nodo en el gráfico.
                espaciado (float): Espaciado horizontal entre nodos.
            """
            if nodo is not None:
                coord = (x, -y)
                grafo.add_node(coord, label=nodo.valor)
                etiquetas[coord] = nodo.valor
                posiciones[coord] = coord
                # Agregar nodo izquierdo
                if nodo.izq is not None:
                    izquierda = (x - espaciado, -(y + 1))
                    grafo.add_edge(coord, izquierda)
                    agregar_nodos_aristas(
                        nodo.izq, x - espaciado, y + 1, espaciado / 1.5)
                # Agregar nodo derecho
                if nodo.der is not None:
                    derecha = (x + espaciado, -(y + 1))
                    grafo.add_edge(coord, derecha)
                    agregar_nodos_aristas(
                        nodo.der, x + espaciado, y + 1, espaciado / 1.5)

        # Agregar nodos y aristas al grafo
        agregar_nodos_aristas(self.arbol.raiz)

        # Personalizar el tamaño de la figura para hacer la pantalla más corta y ancha
        # Ancho de 12, altura de 6 (mejora la legibilidad horizontal)
        plt.figure(figsize=(12, 6))

        # Establecer un estilo estético oscuro
        plt.style.use('dark_background')

        # Configurar la visualización del grafo
        nx.draw(
            grafo,
            posiciones,
            labels=etiquetas,
            with_labels=True,
            node_size=2500,               # Tamaño más grande para los nodos
            node_color="skyblue",          # Color azul claro para los nodos
            font_size=14,                  # Aumentar tamaño de la fuente
            font_color="black",            # Color de texto oscuro sobre nodos claros
            font_weight="bold",            # Negrita para mayor legibilidad
            edge_color="lightgreen",       # Aristas de color verde claro
            linewidths=3,                  # Grosor de las aristas
            arrows=False                   # Sin flechas en las aristas
        )

        # Mostrar el gráfico
        plt.show()
