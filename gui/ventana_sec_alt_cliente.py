import tkinter as tk
from tkinter import ttk
import sys, os

#   Esto me deja importar modelos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modelos.aux_abm_cliente import verificar_campo_vacio


class Ventana_sec_alt_cliente(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Alta-Cliente:")
        self.geometry("300x350")
        self.labelFrame = tk.LabelFrame(self, text="Alta-Cliente")
        self.labelFrame.grid(column=0, row=0, padx=10, pady=10)
        #   Campo Nombre
        self.etiquetaNombrelabelFrame = tk.Label(self.labelFrame, text="Nombre:   ")
        self.etiquetaNombrelabelFrame.grid(
            column=0, row=0, padx=10, pady=10, sticky="w"
        )
        self.stringVarNombrelabelFrame = tk.StringVar()
        self.entradaNombrelabelFrame = tk.Entry(
            self.labelFrame, textvariable=self.stringVarNombrelabelFrame
        )
        self.entradaNombrelabelFrame.grid(column=1, row=0, padx=10, pady=10, sticky="e")

        #   Campo Apellido
        self.etiquetaApellidolabelFrame = tk.Label(self.labelFrame, text="Apellido:   ")
        self.etiquetaApellidolabelFrame.grid(
            column=0, row=1, padx=10, pady=10, sticky="w"
        )
        self.stringVarApellidolabelFrame = tk.StringVar()
        self.entradaApellidolabelFrame = tk.Entry(
            self.labelFrame, textvariable=self.stringVarApellidolabelFrame
        )
        self.entradaApellidolabelFrame.grid(
            column=1, row=1, padx=10, pady=10, sticky="e"
        )

        #   Campo Telefono
        self.etiquetaTelefonolabelFrame = tk.Label(self.labelFrame, text="Telefono:   ")
        self.etiquetaTelefonolabelFrame.grid(
            column=0, row=2, padx=10, pady=10, sticky="w"
        )
        self.stringVarTelefonolabelFrame = tk.StringVar()
        self.entradaTelefonolabelFrame = tk.Entry(
            self.labelFrame, textvariable=self.stringVarTelefonolabelFrame
        )
        self.entradaTelefonolabelFrame.grid(
            column=1, row=2, padx=10, pady=10, sticky="e"
        )

        #   Campo Correo
        self.etiquetaCorreolabelFrame = tk.Label(self.labelFrame, text="Correo:   ")
        self.etiquetaCorreolabelFrame.grid(
            column=0, row=3, padx=10, pady=10, sticky="w"
        )
        self.stringVarCorreolabelFrame = tk.StringVar()
        self.entradaCorreolabelFrame = tk.Entry(
            self.labelFrame, textvariable=self.stringVarCorreolabelFrame
        )
        self.entradaCorreolabelFrame.grid(column=1, row=3, padx=10, pady=10, sticky="e")

        self.botonIngresarlabelFrame = tk.Button(
            self.labelFrame, text="Ingresar", command=self.validar_datos_alta_cliente
        )
        self.botonIngresarlabelFrame.grid(column=0, row=4, padx=10, pady=10, sticky="e")
        # self.botonIngresarlabelFrame.config(state="disabled")
        self.botonCancelarlabelFrame = tk.Button(
            self.labelFrame, text="Cancelar", command=self.cancelar_alta_usuario
        )
        self.botonCancelarlabelFrame.grid(column=1, row=4, padx=10, pady=10, sticky="e")

    def validar_datos_alta_cliente(self):
        try:
            campos = [
                self.stringVarNombrelabelFrame.get(),
                self.stringVarApellidolabelFrame.get(),
                self.stringVarCorreolabelFrame.get(),
                self.stringVarTelefonolabelFrame.get(),
            ]
            print(campos)
        except Exception as e:
            print("Error al ingresar cliente")

    def cancelar_alta_usuario(self):
        self.destroy()
