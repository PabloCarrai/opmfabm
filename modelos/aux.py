import sys
import os

#   Esto me deja importar gestor_archivo_sqlite.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from archivo_db.gestor_hijo_db import Gestor_Hijo as gh


def insertar(datos):
    db = gh("gestor_archivo_sqlite/archivo_db.db")
    db.insertar_Registro(datos)
    db.cerrar()
    print(f" Registro {datos} insertado")


def eliminar(datos):
    db = gh("gestor_archivo_sqlite/archivo_db.db")
    db.eliminar_Registro(datos)
    db.cerrar()
    print(f" Registro {datos} Eliminado")


def actualizar(datos):
    db = gh("gestor_archivo_sqlite/archivo_db.db")
    db.actualizar_Registro(datos)
    db.cerrar()
    print(f" Registro {datos} Actualizado")
