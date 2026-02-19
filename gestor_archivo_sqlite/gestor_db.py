import sqlite3


class gestorDB:
    """
    gestorDB Gestiona la apertura el cierre y el volcado de
    las secuencias sql para la creacion de las tablas en el
    archivo sqlite
    """

    def __init__(self, db_name):
        """
        __init__    conecta inicialmente a db_name

        :param db_name: Es el nombre del archivo .sqlite/.db a usar
        :param self.conexion: Es la conexion al archivo .sqlite/.db
        :param self.curso: Es el cursor de la conexion
        """

        try:
            self.conexion = sqlite3.connect(db_name)
            self.cursor = self.conexion.cursor()
        except Exception as e:
            return f"Error Al conectar a la db: {e}"

    def crear_tablas(self, sql):
        """
        crear_tablas es quien se encarga de ejecutar las secuencias sql

        :param sql: Son sentencias sql para crear las tablas de toda la db
        """
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
        except Exception as e:
            return f"Error al crear las tablas: {e}"

    def cerrar(self):
        """
        cerrar Cierra la conexion
        """
        try:
            self.conexion.close()
        except Exception as e:
            return f"Error Al cerrar la conexion: {e}"
