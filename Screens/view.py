"""
    Views de la interfaz gráfica de la aplicación de Árbol de Expresión Aritmética.
"""
import tkinter as tk
from tkinter import messagebox


class Vista:
    """
    Clase Vista que gestiona la interfaz gráfica de la aplicación de Árbol de Expresión Aritmética.
    """

    def __init__(self, root):
        """
        Inicializa la vista, configura la ventana principal y crea los widgets de la interfaz.

        Args:
            root (Tk): La ventana principal de Tkinter.
        """
        self.root = root
        self._configurar_ventana()
        self._crear_widgets()

    def _configurar_ventana(self):
        """
        Configura la ventana principal de la aplicación con título, tamaño y color de fondo.
        """
        self.root.title("Generador de Árbol de Expresión Aritmética")
        self.root.geometry("600x600")
        self.root.configure(bg='#2E2E2E')

    def _crear_widgets(self):
        """
        Crea los widgets de la interfaz gráfica como etiquetas, campos de texto y botones.
        """
        self._crear_label("Ingrese la expresión aritmética:")
        self.entry = self._crear_entry()
        self.generate_button = self._crear_boton("Generar Árbol", "#4CAF50")
        self.result_text_inorden = self._crear_resultado("Resultado Inorden:")
        self.result_text_preorden = self._crear_resultado(
            "Resultado Preorden:")
        self.result_text_postorden = self._crear_resultado(
            "Resultado Postorden:")
        self.result_text_evaluacion = self._crear_resultado(
            "Resultado Evaluación:")
        self.graph_button = self._crear_boton("Graficar Árbol", "#2196F3")

    def _crear_label(self, texto):
        """
        Crea una etiqueta con un texto específico.

        Args:
            texto (str): El texto que se mostrará en la etiqueta.
        """
        label = tk.Label(self.root, text=texto, font=(
            "Arial", 12), fg="white", bg="#2E2E2E")
        label.pack(pady=10)

    def _crear_entry(self):
        """
        Crea el campo de entrada de texto para la expresión aritmética.

        Returns:
            Entry: El widget de entrada de texto.
        """
        entry = tk.Entry(self.root, width=50, font=(
            "Arial", 12), bg="#333", fg="white")
        entry.pack(pady=10)
        return entry

    def _crear_boton(self, texto, color_fondo):
        """
        Crea un botón con el texto y color de fondo especificado.

        Args:
            texto (str): El texto que se mostrará en el botón.
            color_fondo (str): El color de fondo del botón.

        Returns:
            Button: El widget de botón creado.
        """
        button = tk.Button(self.root, text=texto, bg=color_fondo,
                           fg="white", font=("Arial", 12, "bold"))
        button.pack(pady=10)
        return button

    def _crear_resultado(self, texto):
        """
        Crea un área de texto para mostrar resultados de los recorridos del árbol.

        Args:
            texto (str): El texto que describe el tipo de recorrido (inorden, preorden, etc.).

        Returns:
            Text: El widget de área de texto para mostrar el resultado.
        """
        self._crear_label(texto)
        result_text = tk.Text(self.root, height=2, width=50, font=(
            "Arial", 12), bg="#333", fg="white", state=tk.DISABLED)
        result_text.pack(pady=5)
        return result_text

    def configurar_comandos(self, generar_arbol_callback, graficar_arbol_callback):
        """
        Asigna las funciones callback a los botones de la interfaz.

        Args:
            generar_arbol_callback (func): Función que se llama al generar el árbol.
            graficar_arbol_callback (func): Función que se llama al graficar el árbol.
        """
        self.generate_button.config(command=generar_arbol_callback)
        self.graph_button.config(command=graficar_arbol_callback)

    def obtener_expresion(self):
        """
        Obtiene la expresión ingresada por el usuario.

        Returns:
            str: La expresión ingresada en el campo de texto.
        """
        return self.entry.get()

    def mostrar_resultados(self, inorden, preorden, postorden, evaluacion):
        """
        Actualiza los campos de resultados con los recorridos del árbol y 
        el resultado de la evaluación.

        Args:
            inorden (str): Recorrido inorden del árbol.
            preorden (str): Recorrido preorden del árbol.
            postorden (str): Recorrido postorden del árbol.
            evaluacion (str): Resultado de la evaluación del árbol.
        """
        self._actualizar_campo(self.result_text_inorden, inorden)
        self._actualizar_campo(self.result_text_preorden, preorden)
        self._actualizar_campo(self.result_text_postorden, postorden)
        self._actualizar_campo(self.result_text_evaluacion, evaluacion)

    def _actualizar_campo(self, campo_texto, texto):
        """
        Actualiza un campo de texto con el contenido proporcionado.

        Args:
            campo_texto (Text): El widget de área de texto a actualizar.
            texto (str): El texto que se mostrará en el área de texto.
        """
        campo_texto.config(state=tk.NORMAL)
        campo_texto.delete(1.0, tk.END)
        campo_texto.insert(tk.END, texto)
        campo_texto.config(state=tk.DISABLED)

    def mostrar_error(self, titulo, mensaje):
        """
        Muestra un cuadro de diálogo con un mensaje de error.

        Args:
            titulo (str): Título de la ventana de error.
            mensaje (str): Mensaje de error a mostrar.
        """
        messagebox.showerror(titulo, mensaje)
