import os
import sys

#   Esto me deja importar gestor_archivo_sqlite.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from gestor_archivo_sqlite.gestor_db import gestorDB as gdb


class Gestor_Hijo(gdb):
    def insertar_Registro(self):
        pass
