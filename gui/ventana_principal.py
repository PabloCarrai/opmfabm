import tkinter as tk
from tkinter import ttk

from .ventana_sec_alt_cliente import Ventana_sec_alt_cliente


class Ventana_Principal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bienvenido a OPMFABM")
        self.geometry("300x350")
        self.labelFramePrincipal = tk.LabelFrame(self, text="ABM-Clientes:")
        self.labelFramePrincipal.grid(column=0, row=0, padx=10, pady=10)
        self.botonVentanaABMUsuario = tk.Button(
            self.labelFramePrincipal,
            text="Alta-Clientes   ",
            command=self.abrir_ventana_sec_alt_cliente,
        )
        self.botonVentanaABMUsuario.grid(column=0, row=0, padx=10, pady=10)
        self.botonCerrarVentanaPrincipal = tk.Button(
            self, text="Salir", command=self.salirAplicacionPrincipal
        )
        self.botonCerrarVentanaPrincipal.grid(
            column=0, row=1, padx=10, pady=10, sticky="S"
        )

    def abrir_ventana_sec_alt_cliente(self):
        ventana_secundaria = Ventana_sec_alt_cliente()

    def salirAplicacionPrincipal(self):
        self.destroy()
