import tkinter as tk
from tkinter import ttk


class VentanaABMListadoUsuario:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Listado de Clientes")
        self.labelFrameventabaAMBListadoUsuario = tk.LabelFrame(
            self.ventana, text="Listado de Clientes: "
        )
        self.labelFrameventabaAMBListadoUsuario.grid(column=0, row=0, padx=10, pady=10)

        columnas = ("id", "nombre", "apellido", "email", "dni", "telefono")
        self.treeviewListadoABMUsuario = ttk.Treeview(
            self.labelFrameventabaAMBListadoUsuario, columns=columnas, show="headings"
        )
        self.treeviewListadoABMUsuario.heading("id", text="Id")
        self.treeviewListadoABMUsuario.heading("nombre", text="Nombre")
        self.treeviewListadoABMUsuario.heading("apellido", text="Apellido")
        self.treeviewListadoABMUsuario.heading("dni", text="Dni")
        self.treeviewListadoABMUsuario.heading("email", text="Email")
        self.treeviewListadoABMUsuario.heading("telefono", text="Telefono")
        self.treeviewListadoABMUsuario.grid(column=0, row=0, padx=10, pady=10)
