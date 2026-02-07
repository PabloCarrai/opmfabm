import tkinter as tk
from tkinter import ttk

# from .auxabm import validarEntero as ve


class VentanaABMUsuario:
    def __init__(self):
        #   Arranca la ventana secundaria
        self.ventana = tk.Toplevel()
        #   Tiene un titulo para la descripcion
        self.ventana.title("ABM-Usuario")
        #   Estoy pegado con labelframe. Me encantan como quedan
        self.labelFrameABMUsuarioVentanaSecundaria = tk.LabelFrame(
            self.ventana, text="ABM Usuario"
        )
        self.labelFrameABMUsuarioVentanaSecundaria.grid(
            column=0, row=0, padx=10, pady=10
        )
        #   Etiqueta nombre
        self.etiquetaNombrelabelFrameABMUsuarioVentanaSecundaria = tk.Label(
            self.labelFrameABMUsuarioVentanaSecundaria, text="Nombre:  "
        )
        self.etiquetaNombrelabelFrameABMUsuarioVentanaSecundaria.grid(
            column=0, row=0, padx=10, pady=10
        )
        #   Arrancamos con el stringvar
        self.stringvarNombrelabelFrameABMUsuarioVentanaSecundaria = tk.StringVar()
        #   El entry para nombre
        self.entradaNombrelabelFrameABMUsuarioVentanaSecundaria = tk.Entry(
            self.labelFrameABMUsuarioVentanaSecundaria,
            textvariable=self.stringvarNombrelabelFrameABMUsuarioVentanaSecundaria,
        )
        #   Ahora ubicamos el entry al lado del label nombre
        self.entradaNombrelabelFrameABMUsuarioVentanaSecundaria.grid(
            column=1, row=0, padx=10, pady=10
        )
        #   id no usado
        #   Etiqueta apellido
        self.etiquetaApellidolabelFrameABMUsuarioVentanaSecundaria = tk.Label(
            self.labelFrameABMUsuarioVentanaSecundaria, text="Apellido:  "
        )
        self.etiquetaApellidolabelFrameABMUsuarioVentanaSecundaria.grid(
            column=0, row=1, padx=10, pady=10
        )
        #   El stringvar de Apellido
        self.stringvarApellidolabelFrameABMUsuarioVentanaSecundaria = tk.StringVar()
        self.entradaApellidolabelFrameABMUsuarioVentanaSecundaria = tk.Entry(
            self.labelFrameABMUsuarioVentanaSecundaria,
            textvariable=self.stringvarApellidolabelFrameABMUsuarioVentanaSecundaria,
        )
        self.entradaApellidolabelFrameABMUsuarioVentanaSecundaria.grid(
            column=1, row=1, padx=10, pady=10
        )
        # dni
        self.etiquetaDNIlabelFrameABMUsuarioVentanaSecundaria = tk.Label(
            self.labelFrameABMUsuarioVentanaSecundaria, text="DNI:  "
        )
        self.etiquetaDNIlabelFrameABMUsuarioVentanaSecundaria.grid(
            column=0, row=2, padx=10, pady=10
        )
        self.stringvarDNIlabelFrameABMUsuarioVentanaSecundaria = tk.StringVar()
        self.entradaDNIlabelFrameABMUsuarioVentanaSecundaria = tk.Entry(
            self.labelFrameABMUsuarioVentanaSecundaria,
            textvariable=self.stringvarDNIlabelFrameABMUsuarioVentanaSecundaria,
        )
        self.entradaDNIlabelFrameABMUsuarioVentanaSecundaria.grid(
            column=1, row=2, padx=10, pady=10
        )
        # email
        self.etiquetaEmaillabelFrameABMUsuarioVentanaSecundaria = tk.Label(
            self.labelFrameABMUsuarioVentanaSecundaria, text="Email:   "
        )
        self.etiquetaEmaillabelFrameABMUsuarioVentanaSecundaria.grid(
            column=0, row=3, padx=10, pady=10
        )
        self.stringvarEmaillabelFrameABMUsuarioVentanaSecundaria = tk.StringVar()
        self.entradaEmaillabelFrameABMUsuarioVentanaSecundaria = tk.Entry(
            self.labelFrameABMUsuarioVentanaSecundaria,
            textvariable=self.stringvarEmaillabelFrameABMUsuarioVentanaSecundaria,
        )
        self.entradaEmaillabelFrameABMUsuarioVentanaSecundaria.grid(
            column=1, row=3, padx=10, pady=10
        )

        # telefono
        self.etiquetaTelefonolabelFrameABMUsuarioVentanaSecundaria.grid(
            column=0, row=4, padx=10, pady=10
        )
        self.stringvarTelefonolabelFrameABMUsuarioVentanaSecundaria = tk.StringVar()
        self.entradaTelefonolabelFrameABMUsuarioVentanaSecundaria = tk.Entry(
            self.labelFrameABMUsuarioVentanaSecundaria,
            textvariable=self.stringvarTelefonolabelFrameABMUsuarioVentanaSecundaria,
        )
        self.entradaTelefonolabelFrameABMUsuarioVentanaSecundaria.grid(
            column=1, row=4, padx=10, pady=10
        )

        #   Boton Aceptar
        self.botonAceptarlabelFrameABMUsuarioVentanaSecundaria = tk.Button(
            self.labelFrameABMUsuarioVentanaSecundaria,
            text="Aceptar",
            command=self.ValidrBotonAceptar,
        )
        self.botonAceptarlabelFrameABMUsuarioVentanaSecundaria.grid(
            column=0, row=5, padx=10, pady=10
        )

        #   Boton Cancelar
        self.botonCancelarlabelFrameABMUsuarioVentanaSecundaria = tk.Button(
            self.labelFrameABMUsuarioVentanaSecundaria,
            text="Cancelar",
            command=self.ValidrBotonAceptar,
        )
        self.botonCancelarlabelFrameABMUsuarioVentanaSecundaria.grid(
            column=1, row=5, padx=10, pady=10
        )

    def ValidrBotonAceptar(self):
        pass
