import tkinter as tk
from tkinter import ttk
from .auxabmdb import DB as db


class VentanaABMListadoUsuario:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Listado de Clientes")
        # Esto ajusta las columnas por el contenedor del labelframe
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)
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
        #   Esto ajusta el ancho de las columnas
        self.treeviewListadoABMUsuario.column("id", width=100, anchor="w")
        self.treeviewListadoABMUsuario.column("nombre", width=100, anchor="w")
        self.treeviewListadoABMUsuario.column("apellido", width=100, anchor="w")
        self.treeviewListadoABMUsuario.column("email", width=100, anchor="w")
        self.treeviewListadoABMUsuario.column("telefono", width=100, anchor="w")
        self.treeviewListadoABMUsuario.grid(column=0, row=0, sticky="nsew")
        self.labelFrameventabaAMBListadoUsuarioBotones = tk.LabelFrame(
            self.ventana, text=""
        )
        self.labelFrameventabaAMBListadoUsuarioBotones.grid(
            column=0, row=1, padx=10, pady=10, sticky="w"
        )
        self.botonListarlabelFrameventabaAMBListadoUsuarioBotones = tk.Button(
            self.labelFrameventabaAMBListadoUsuarioBotones,
            text="Listar",
            command=self.listarUsuariosExistentes,
        )
        self.botonListarlabelFrameventabaAMBListadoUsuarioBotones.grid(
            column=0, row=0, padx=10, pady=10
        )

        self.botonCancelarlabelFrameventabaAMBListadoUsuarioBotones = tk.Button(
            self.labelFrameventabaAMBListadoUsuarioBotones,
            text="Cancelar",
            command=self.cancelarListadoUsuario,
        )
        self.botonCancelarlabelFrameventabaAMBListadoUsuarioBotones.grid(
            column=1, row=0, padx=10, pady=10
        )

    def listarUsuariosExistentes(self):
        conexion = db()
        resultado = conexion.listarClientesExistentes()
        for fila in resultado:
            self.treeviewListadoABMUsuario.insert("", "end", values=fila)

    def cancelarListadoUsuario(self):
        self.ventana.destroy()
