import tkinter as tk
from tkinter import ttk

from .ventana_sec_alt_cliente import Ventana_sec_alt_cliente


class Ventana_Principal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bienvenido a OPMFABM")
        # self.geometry("300x350")
        self.labelFramePrincipalABMCliente = tk.LabelFrame(self, text="ABM-Cliente:")
        self.labelFramePrincipalABMCliente.grid(column=0, row=0, padx=10, pady=10)
        #   Boton Alta-Cliente
        self.botonVentanaABMUsuarioAltaUsuario = tk.Button(
            self.labelFramePrincipalABMCliente,
            text="Alta-Cliente   ",
            command=self.abrir_ventana_sec_alt_cliente,
        )
        self.botonVentanaABMUsuarioAltaUsuario.grid(column=0, row=0, padx=10, pady=10)
        #   Boton Edicion-Cliente
        self.botonVentanaABMUsuarioEdicionUsuario = tk.Button(
            self.labelFramePrincipalABMCliente, text="Edicion-Cliente"
        )
        self.botonVentanaABMUsuarioEdicionUsuario.grid(
            column=1, row=0, padx=10, pady=10
        )

        #   Boton Baja-Cliente
        self.botonVentanaABMUsuarioBajaUsuario = tk.Button(
            self.labelFramePrincipalABMCliente, text="Baja-Cliente"
        )
        self.botonVentanaABMUsuarioBajaUsuario.grid(column=1, row=1, padx=10, pady=10)

        #   Boton Listado-Cliente
        self.botonVentanaABMUsuarioListadoUsuario = tk.Button(
            self.labelFramePrincipalABMCliente, text="Listado-Cliente"
        )
        self.botonVentanaABMUsuarioListadoUsuario.grid(
            column=0, row=1, padx=10, pady=10
        )

        #   Boton Salir
        self.botonCerrarVentanaPrincipal = tk.Button(
            self, text="Salir", command=self.salirAplicacionPrincipal
        )
        self.botonCerrarVentanaPrincipal.grid(
            column=0, row=1, padx=10, pady=10, sticky="se"
        )

    def abrir_ventana_sec_alt_cliente(self):
        ventana_secundaria = Ventana_sec_alt_cliente()

    def salirAplicacionPrincipal(self):
        self.destroy()
