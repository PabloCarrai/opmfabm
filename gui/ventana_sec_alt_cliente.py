import tkinter as tk
from tkinter import ttk


class Ventana_sec_alt_cliente(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Alta-Cliente:")
        self.geometry("300x350")
        self.labelFrame = tk.LabelFrame(self, text="Alta-Cliente")
        self.labelFrame.grid(column=0, row=0, padx=10, pady=10)
        self.etiquetaNombrelabelFrame = tk.Label(self.labelFrame, text="Nombre:   ")
        self.etiquetaNombrelabelFrame.grid(
            column=0, row=0, padx=10, pady=10, sticky="w"
        )
