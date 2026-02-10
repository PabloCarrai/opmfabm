import tkinter as tk


def validarNoEsteVacio(*textos):
    """
    Valida que textos tenga algun string o no este vacio

    :param textos: Los string a evaluar
    Returns:
    Devuelve True si se cumple que no tenga cadenas vacias
    """
    try:
        for texto in textos:
            if texto == "" or len(texto) == 0:
                raise ValueError("Al menos uno de los textos estan vacios ")
        return True
    except ValueError as e:
        print(f"Error {e}")


def vaciarEntrys(entrada):
    """
    A cada entrada pasado como entrada, borramos su contenido
    :param entrada: Es una tupla con las entradas de cada parte de la ventaba ABM 
    """
    for e in entrada:
        e.delete(0, tk.END)
