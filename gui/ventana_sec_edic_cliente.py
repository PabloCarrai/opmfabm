import tkinter as tk
from tkinter import ttk


class Ventana_sec_edic_cliente(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Edicion-Cliente")
        #   Label del id
        self.labelFrame = tk.LabelFrame(self, text="Edicion-Cliente")
        self.labelFrame.grid(column=0, row=0, padx=10, pady=10)
        #   Etiqueta id
        self.etiquetaIdlabelFrame = tk.Label(self.labelFrame, text="Id:")
        self.etiquetaIdlabelFrame.grid(column=0, row=0, padx=10, pady=10)
        #   stringvar id
        self.stringvarIdlabelFrame = tk.StringVar()
        #   Entry para id
        self.entradaIdlabelFrame = tk.Entry(
            self.labelFrame, textvariable=self.stringvarIdlabelFrame
        )
        self.entradaIdlabelFrame.grid(column=1, row=0, padx=10, pady=10)
        #   Label para el detalle del cliente
        self.labelFrameDetalleCliente = tk.LabelFrame(self, text="Detalle-Cliente")
        self.labelFrameDetalleCliente.grid(column=0, row=1, padx=10, pady=10)

        #   Etiqueta Nombre
        self.etiquetaNombrelabelFrameDetalleCliente = tk.Label(
            self.labelFrameDetalleCliente, text="Nombre: "
        )
        self.etiquetaNombrelabelFrameDetalleCliente.grid(
            column=0, row=0, padx=10, pady=10
        )
        #   Stringvar Nombre
        self.stringvarNombrelabelFrameDetalleCliente = tk.StringVar()
        #   Entry Nombre
        self.entradaNombrelabelFrameDetalleCliente = tk.Entry(
            self.labelFrameDetalleCliente,
            textvariable=self.stringvarNombrelabelFrameDetalleCliente,
        )
        self.entradaNombrelabelFrameDetalleCliente.grid(
            column=1, row=0, padx=10, pady=10
        )
        #   Etiqueta Apellido
        #   Etiqueta Telefono
        #   Etiqueta Email
