import sys, os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms

#   Esto me deja importar modelos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modelos.aux import listar


class Ventana_sec_list_cliente(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Listado-Cliente:")
        self.labelFrame = tk.LabelFrame(self, text="Listado-Cliente")
        self.labelFrame.grid(column=0, row=0, padx=10, pady=10)
        #   El mentado treeview va a partir de aca
        columnas = ("Id", "Nombre", "Apellido", "Telefono", "Email")
        self.treeviewListadoClientelabelFrame = ttk.Treeview(
            self.labelFrame, columns=columnas, show="headings"
        )
        for columna in columnas:
            self.treeviewListadoClientelabelFrame.heading(columna, text=columna)
            self.treeviewListadoClientelabelFrame.column(columna, width=150)
        self.treeviewListadoClientelabelFrame.grid(column=0, row=0, padx=10, pady=10)

        self.labelFrameBotones = tk.LabelFrame(self, text="")
        self.labelFrameBotones.grid(column=0, row=1, padx=10, pady=10, sticky="e")
        #   Boton listar
        self.botonListarClienteListadoClientelabelFrame = tk.Button(
            self.labelFrameBotones, text="Listar", command=self.listarListadoClientes
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

    def listarListadoClientes(self):
        try:
            for item in self.treeviewListadoClientelabelFrame.get_children():
                self.treeviewListadoClientelabelFrame.delete(item)
            sentencia = "select id,nombre,apellido,telefono,email from clientes"
            resultado = listar(sentencia)
            if len(resultado) == 0:
                ms.showinfo("Error", "No hay datos en la DB")
            else:
                for contacto in resultado:
                    self.treeviewListadoClientelabelFrame.insert(
                        "", tk.END, values=contacto
                    )
        except Exception as e:
            ms.showerror("Error", f"Problemas con el listado de Clientes: {e}")
