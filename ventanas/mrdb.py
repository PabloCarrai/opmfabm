import sqlite3
from pathlib import Path

#   Necesito meter la ruta del archivo .db, como esta en otro directorio armo esto
ruta_actual = Path(__file__).resolve()
db_path = ruta_actual.parent.parent / "datos.db"
db = f"{db_path}"


class MrDB:
    """
    Gestiona la conexion a la db datos.db
    Esta es la clase Padre
    """

    def __init__(self):
        self.nombreDB = db
        self.conexion = None

    def conectar(self):
        """
        Realiza la conexion a sqlite el archivo datos.db

        :param self.conexion: Es la conexion a la db datos.db

        """
        try:
            self.conexion = sqlite3.connect(self.nombreDB)
            return self.conexion.cursor()
            print(f"Conectado a {self.nombreDB}")
        except sqlite3.Error as e:
            print(f"Error al conectar {e}")

    def cerrar(self):
        """
        Esto se fija si la conexion esta abierta y la cierra
        """
        if self.conexion:
            self.conexion.close()
            print("Conexion cerrada")
