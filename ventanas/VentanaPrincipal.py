import tkinter as tk
from tkinter import ttk
from ventanas.VentanaABMAltaUsuario import VentanaABMAltaUsuario
#   En desarrollo
from ventanas.VentanaABMListadoUsuario import VentanaABMListadoUsuario


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
            text="Alta",
            command=self.abrirVentanaABMAltaUsuario,
        )
        self.botonAltaUsuariolabelFrameABMUsuario.grid(
            column=0, row=0, padx=10, pady=10
        )

        #   Boton Listado Usuario
        self.botonListadoUsuariolabelFrameABMUsuario = tk.Button(
            self.labelFrameABMUsuario,
            text="Listado",
            command=self.abrirVentanaABMListadoUsuario,
        )
        self.botonListadoUsuariolabelFrameABMUsuario.grid(
            column=1, row=0, padx=10, pady=10
        )

    def abrirVentanaABMAltaUsuario(self):
        ventanaSecundaria = VentanaABMAltaUsuario()

    def abrirVentanaABMListadoUsuario(self):
        ventanaSecundaria = VentanaABMListadoUsuario()
        print("Putoooo")
