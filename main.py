from tkinter import Tk
from tkinter import ttk

from archivo_db.gestor_hijo_db import Gestor_Hijo as gh
from modelos.aux import insertar, eliminar, actualizar
from gui.ventana_principal import Ventana_Principal


# sentencias = [
#     "insert into clientes(nombre,apellido,telefono,email) values(?,?,?,?)",
#     "delete from clientes where id=?",
#     "update clientes set nombre=?,apellido=? ,telefono=? ,email=?  where id=?",
# ]


def mostrar_gui():
    ventanaPrincipal = Ventana_Principal()
    ventanaPrincipal.mainloop()


def main():
    mostrar_gui()
    # datos = ("Gigi", "DeAraoz", "1140896324", "gdaraoz@gmail.com", 3)
    # # insertar(datos, sentencias[0])
    # # eliminar(datos,sentencias[1])
    # actualizar(datos, sentencias[2])


if __name__ == "__main__":
    main()


"""
#   Update de Cliente
sentencia = "update clientes set nombre=?,apellido=? ,telefono=? ,email=?  where id=?"
#   Delete de Cliente
sentencia = "delete from clientes where id=?"
#   Insert de Cliente
sentencia = "insert into clientes(nombre,apellido,telefono,email) values(?,?,?,?)"
"""
