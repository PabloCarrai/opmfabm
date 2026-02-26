import os, sys, sqlite3

#   Esto me deja importar gestor_archivo_sqlite.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from gestor_archivo_sqlite.gestor_db import gestorDB as gdb


class Gestor_Hijo(gdb):
    """
    Gestiona las operaciones en una db sqlite3
    """

    def insertar_Registro(self, datos, sentencia):
        """
        Gestionar una insercion de un registro.
        Se requiere datos que es el conjunto de datos y
        sentencia que seria la consulta sql de insert para dichos datos
        """
        try:
            self.cursor.execute(sentencia, datos)
            self.conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al insertar registro: {e}")

    def eliminar_Registro(self, datos, sentencia):
        """
        Gestiona la eliminacion de un registro.
        Requiere datos que son los datos necesarios y una
        sentencia que es el sql para eliminar registros
        """
        try:
            self.cursor.execute(sentencia, datos)
            self.conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al eliminar registro: {e}")

    def actualizar_Registro(self, datos, sentencia):
        """
        Gestionar una Actualizacion de un registro.
        Se requiere datos que es el conjunto de datos y
        sentencia que seria la consulta sql de update para dichos datos
        """
        try:
            self.cursor.execute(sentencia, datos)
            self.conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al actualizar registro: {e}")

    def verificar_correo_existente(self, datos, sentencia):
        try:
            self.cursor.execute(sentencia, datos)
            if self.cursor.fetchone():
                return True
            else:
                return False
        except sqlite3.Error as e:
            print(f"Error al consultar correo existente: {e}")
