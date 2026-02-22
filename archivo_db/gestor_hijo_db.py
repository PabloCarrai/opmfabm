import os, sys, sqlite3

#   Esto me deja importar gestor_archivo_sqlite.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from gestor_archivo_sqlite.gestor_db import gestorDB as gdb


class Gestor_Hijo(gdb):
    def insertar_Registro(self, datos):
        try:
            sentencia = (
                "insert into clientes(nombre,apellido,telefono,email) values(?,?,?,?)"
            )
            self.cursor.execute(sentencia, datos)
            self.conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al insertar registro: {e}")

    def eliminar_Registro(self, datos):
        try:
            sentencia = "delete from clientes where id=?"
            self.cursor.execute(sentencia, datos)
            self.conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al eliminar registro: {e}")

    def actualizar_Registro(self, datos):
        try:
            sentencia = "update clientes set nombre=?,apellido=? ,telefono=? ,email=?  where id=?"
            self.cursor.execute(sentencia, datos)
            self.conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al actualizar registro: {e}")
