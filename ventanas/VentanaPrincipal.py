import tkinter as tk
from tkinter import ttk
from ventanas.VentanaABMAltaUsuario import VentanaABMAltaUsuario


class Ventana_Principal:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicacion Principal")
        # self.root.geometry("400x400")
        #   Label del ABM Usuario
        self.labelFrameABMUsuario = tk.LabelFrame(self.root, text="ABM-Usuario")
        self.labelFrameABMUsuario.grid(column=0, row=0, padx=10, pady=10)
        #   Boton Alta Usuario
        self.botonAltaUsuariolabelFrameABMUsuario = tk.Button(
            self.labelFrameABMUsuario,
            text="Alta Usuario",
            command=self.abrirVentanaABMUsuario,
        )
        self.botonAltaUsuariolabelFrameABMUsuario.grid(
            column=0, row=0, padx=10, pady=10
        )

    def abrirVentanaABMUsuario(self):
        self.ventanaSecundaria = VentanaABMAltaUsuario()
