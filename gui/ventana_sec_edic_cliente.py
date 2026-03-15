import os, sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms

#   Esto me deja importar modelos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modelos.aux_abm_cliente import validar_entrada_vacia_id


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
        # Boton Buscar
        self.botonBuscarlabelFrame = tk.Button(
            self.labelFrame, text="Buscar", command=self.buscarclienteid
        )
        self.botonBuscarlabelFrame.grid(column=1, row=1, padx=10, pady=10)

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
        self.etiquetaApellidolabelFrameDetalleCliente = tk.Label(
            self.labelFrameDetalleCliente, text="Apellido:"
        )
        self.etiquetaApellidolabelFrameDetalleCliente.grid(
            column=0, row=1, padx=10, pady=10
        )
        #   Stringvar Apellido
        self.stringvarApellidolabelFrameDetalleCliente = tk.StringVar()
        #   Entrada Apellido
        self.entradaApellidolabelFrameDetalleCliente = tk.Entry(
            self.labelFrameDetalleCliente,
            textvariable=self.stringvarApellidolabelFrameDetalleCliente,
        )
        self.entradaApellidolabelFrameDetalleCliente.grid(
            column=1, row=1, padx=10, pady=10
        )
        #   Etiqueta Telefono
        self.etiquetaTelefonolabelFrameDetalleCliente = tk.Label(
            self.labelFrameDetalleCliente, text="Telefono:"
        )
        self.etiquetaTelefonolabelFrameDetalleCliente.grid(
            column=0, row=2, padx=10, pady=10
        )
        #   Stringvar telefono
        self.stringvarTelefonolabelFrameDetalleCliente = tk.StringVar()
        #   Entrada Telefono
        self.entradaTelefonolabelFrameDetalleCliente = tk.Entry(
            self.labelFrameDetalleCliente,
            textvariable=self.stringvarTelefonolabelFrameDetalleCliente,
        )
        self.entradaTelefonolabelFrameDetalleCliente.grid(
            column=1, row=2, padx=10, pady=10
        )
        #   Etiqueta Email
        self.etiquetaEmaillabelFrameDetalleCliente = tk.Label(
            self.labelFrameDetalleCliente, text="Correo:"
        )
        self.etiquetaEmaillabelFrameDetalleCliente.grid(
            column=0, row=3, padx=10, pady=10
        )
        #   Stringvar Email
        self.stringvarEmaillabelFrameDetalleCliente = tk.StringVar()
        #   Entrada Email
        self.entradaEmaillabelFrameDetalleCliente = tk.Entry(
            self.labelFrameDetalleCliente,
            textvariable=self.stringvarEmaillabelFrameDetalleCliente,
        )
        self.entradaEmaillabelFrameDetalleCliente.grid(
            column=1, row=3, padx=10, pady=10
        )
        self.botonEditarlabelFrameDetalleCliente = tk.Button(
            self.labelFrameDetalleCliente, text="Editar"
        )
        self.botonEditarlabelFrameDetalleCliente.grid(column=0, row=4, padx=10, pady=10)

        self.botonSalirlabelFrameDetalleCliente = tk.Button(
            self.labelFrameDetalleCliente,
            text="Salir",
            command=self.salirEdicionCliente,
        )
        self.botonSalirlabelFrameDetalleCliente.grid(column=1, row=4, padx=10, pady=10)

    def buscarclienteid(self):
        print(validar_entrada_vacia_id(self.stringvarIdlabelFrame))
        if validar_entrada_vacia_id(self.stringvarIdlabelFrame):
            ms.showinfo("Capitan America del quisqui ", "Vamos loco")
        else:
            ms.showerror(
                "Error ", "El id esta vacio papa, que queres que busque, la nada??"
            )

    def salirEdicionCliente(self):
        self.destroy()
