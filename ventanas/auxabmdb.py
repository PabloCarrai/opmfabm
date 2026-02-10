import sqlite3
from pathlib import Path

#   Necesito meter la ruta del archivo .db, como esta en otro directorio armo esto
ruta_actual = Path(__file__).resolve()
db_path = ruta_actual.parent.parent / "datos.db"
db = f"{db_path}"


class MrDB:
    """
    Gestiona la conexion a la db datos.db
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
            print(f"Conectado a {self.nombreDB}")
        except sqlite3.Error as e:
            print(f"Error al conectar {e}")

    def insertarCliente(self, datos):
        """
        Este metodo permite insertar datos en la tabla cliente de datos.db

        :param consulta: Es la consultar sql para insertar al cliente en la tabla cliente
        :param datos: Es una tupla con los datos a insertar que pide la tabla cliente
        """
        consulta = (
            "insert into clientes(nombre,apellido,dni,email,telefono) values(?,?,?,?,?)"
        )
        try:
            cursor = self.conexion.cursor()
            cursor.execute(consulta, datos)
            self.conexion.commit()
            print("Clientes guardados con exito")
        except sqlite3.IntegrityError:
            print("Error al guardar cliente")

    def cerrar(self):
        """
        Esto se fija si la conexion esta abierta y la cierra
        """
        if self.conexion:
            self.conexion.close()
            print("Conexion cerrada")


"""
prueba = MrDB()
prueba.conectar()
datos = ("Pepe", "Sanchez", "223234", "psanchez@gmail.com", "34322343")
prueba.insertarCliente(datos)
prueba.cerrar()
"""
