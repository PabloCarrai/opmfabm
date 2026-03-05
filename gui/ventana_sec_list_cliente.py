import tkinter as tk
from tkinter import ttk


class Ventana_sec_list_cliente(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Listado-Cliente:")
        self.labelFrame = tk.LabelFrame(self, text="Listado-Cliente")
        self.labelFrame.grid(column=0, row=0, padx=10, pady=10)
        #   El mentado treeview va a partir de aca
        columnas = ("Nombre", "Apellido", "Telefono", "Email")
        self.treeviewListadoClientelabelFrame = ttk.Treeview(
            self.labelFrame, columns=columnas, show="headings"
        )
        for columna in columnas:
            self.treeviewListadoClientelabelFrame.heading(columna, text=columna)
            self.treeviewListadoClientelabelFrame.column(columna, width=100)
        self.treeviewListadoClientelabelFrame.grid(column=0, row=0, padx=10, pady=10)

        self.labelFrameBotones = tk.LabelFrame(self, text="")
        self.labelFrameBotones.grid(column=0, row=1, padx=10, pady=10, sticky="e")
        #   Boton listar
        self.botonListarClienteListadoClientelabelFrame = tk.Button(
            self.labelFrameBotones, text="Listar"
        )
        self.botonListarClienteListadoClientelabelFrame.grid(
            column=0, row=1, padx=10, pady=10
        )
        #   Boton salir
        self.botonSalirListadoClientelabelFrame = tk.Button(
            self.labelFrameBotones, text="Salir", command=self.salirListadoCliente
        )
        self.botonSalirListadoClientelabelFrame.grid(column=1, row=1, padx=10, pady=10)

    def salirListadoCliente(self):
        self.destroy()
