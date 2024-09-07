"""
Controlador del arbol de expresión
"""
from Modelos.arbol import ArbolDeExpresion
from Screens.arbol_visualizer import ArbolVisualizer
from utils.helpers import balancear_parentesis, eliminar_espacios, validar_expresion


class Controlador:
    """
    Clase Controlador que coordina la interacción entre la vista y el modelo
    de la aplicación de Árbol de Expresión Aritmética. 
    Gestiona la validación de la expresión, la construcción del árbol, 
    y la visualización gráfica.
    """

    def __init__(self, vista):
        """
        Inicializa el controlador y asocia la vista a la clase. 
        Configura los eventos necesarios para interactuar con la vista.

        Args:
            vista (Vista): Instancia de la clase Vista que contiene la interfaz gráfica.
        """
        self.vista = vista
        self.arbol = ArbolDeExpresion()
        self.visualizador = None
        self._configurar_eventos()

    def _configurar_eventos(self):
        """
        Asocia las funciones del controlador con los eventos de la vista,
        como generar el árbol y graficarlo.
        """
        self.vista.configurar_comandos(
            generar_arbol_callback=self.generar_arbol,
            graficar_arbol_callback=self.graficar_arbol
        )

    def generar_arbol(self):
        """
        Valida la expresión ingresada por el usuario, y si es válida, 
        genera el árbol de expresión aritmética. 
        Actualiza los resultados en la vista o muestra errores según corresponda.
        """
        expresion = self.vista.obtener_expresion()

        # Validar la expresión antes de construir el árbol
        if not expresion:
            self.vista.mostrar_error(
                "Error", "Por favor ingrese una expresión aritmética.")
            return

        # Validar si la expresión contiene caracteres válidos
        if not validar_expresion(expresion):
            self.vista.mostrar_error(
                "Error", "La expresión contiene caracteres inválidos.")
            return

        # Verificar si los paréntesis están balanceados
        if not balancear_parentesis(expresion):
            self.vista.mostrar_error(
                "Error", "Los paréntesis no están balanceados.")
            return

        # Limpiar espacios en blanco antes de procesar la expresión
        expresion = eliminar_espacios(expresion)

        try:
            # Construir el árbol de expresión
            self.arbol.construir_arbol(expresion)
            self.visualizador = ArbolVisualizer(self.arbol)
            self._actualizar_vista_resultados()
        except Exception as e:
            self.vista.mostrar_error("Error", f"Expresión no válida: {e}")

    def _actualizar_vista_resultados(self):
        """
        Actualiza la vista con los resultados de los recorridos del árbol 
        (inorden, preorden, postorden) y el resultado de la evaluación de la expresión.
        """
        resultado_inorden = self.arbol.imprimir_inorden(
            self.arbol.raiz).strip()
        resultado_preorden = self.arbol.imprimir_preorden(
            self.arbol.raiz).strip()
        resultado_postorden = self.arbol.imprimir_postorden(
            self.arbol.raiz).strip()
        resultado_evaluacion = str(self.arbol.evaluar_arbol(self.arbol.raiz))

        # Actualizar los campos de resultados en la vista
        self.vista.mostrar_resultados(
            inorden=resultado_inorden,
            preorden=resultado_preorden,
            postorden=resultado_postorden,
            evaluacion=resultado_evaluacion
        )

    def graficar_arbol(self):
        """
        Verifica si el árbol de expresión ha sido generado, 
        y luego llama al visualizador para mostrar el gráfico del árbol.
        Muestra un mensaje de error si el árbol no ha sido generado aún.
        """
        if self.arbol.raiz is None:
            self.vista.mostrar_error("Error", "Primero genere el árbol.")
            return
        self.visualizador.graficar_arbol()
