import re
import tkinter as tk
from tkinter import ttk

from modelos.aux import verifica_correo_existe


def limpiar_entradas(datos):
    for dato in datos:
        dato.delete(0, tk.END)


def validar_entradas_vacias(datos):
    return all(dato.strip() for dato in datos)


def validar_entrada_vacia_id(dato):
    """
    Devuelve False si el stringvar no tiene elementos
    sino devuelve True
    """
    if not dato.get():
        return False
    else:
        return True


def validar_formato_correo(correo):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, correo):
        return True
    return False


def chequeo_todo_abm_cliente(datos):
    """
    Chequeo que cada funcion devuelve True

    validar_entradas_vacias(datos) Valida las entradas vacias
    validar_formato_correo(datos[2]) Valida el formato del correo
    verifica_correo_existe(datos[2]) Valida existencia en la db del correo

    """
    if (
        validar_entradas_vacias(datos)
        and validar_formato_correo(datos[3])
        and not verifica_correo_existe(datos[3])
    ):
        return True
    else:
        return False


#   1) todos los campos con datos       validar_entradas_vacias(datos)
#   2) el formato del correo valido     validar_formato_correo
#   3) el correo no exista en la db

# validar_formato_correo(self.stringVarCorreolabelFrame.get()):
# if verifica_correo_existe:
# datos = ["3", "3", "", "1"]
# print(chequeo_todo_abm_cliente(datos))
# print(validar_formato_correo("pcarrai@gmail.com"))
# print(validar_entradas_vacias(datos))
# print(validar_entradas_vacias(datos))
# print(validar_formato_correo("pcarrai@gmail.com"))
# print(chequeo_todo_abm_cliente(("1","2","pcarrai@gmail.com","7")))
# print(verifica_correo_existe("pablocarrai@gmail.com"))
# verifica_correo_existe("")
