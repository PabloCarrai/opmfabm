import tkinter as tk
from tkinter import ttk


class VentanaABMUsuario:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("ABM-Usuario")

        self.labelFrameABMUsuarioVentanaSecundaria = tk.LabelFrame(
            self.ventana, text="ABM Usuario"
        )
        self.labelFrameABMUsuarioVentanaSecundaria.grid(
            column=0, row=0, padx=10, pady=10
        )
        self.etiquetaPrueba = tk.Label(
            self.labelFrameABMUsuarioVentanaSecundaria, text="Puto el que lee"
        )
        self.etiquetaPrueba.grid(
            column=0, row=0, padx=10, pady=10
        )
