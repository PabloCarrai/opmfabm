import sqlite3
from .mrdb import MrDB


class DB(MrDB):
    """
    Gestiona la conexion a la db datos.db
    Esta es la clase hijo de MrDB
    Solo va a tener los metodos propios de cada seccion.
    En este caso va a ser para la ventana ABM clientes
    """

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
        finally:
            self.cerrar()

    def listarClientesExistentes(self):
        pass
        consulta = "select id_cliente,nombre,apellido,dni,email from clientes"
        try:
            cursor = DB()
            cursor = cursor.conectar()
            cursor.execute(consulta)
            usuariosExistentes = cursor.fetchall()
            return usuariosExistentes
        except sqlite3.IntegrityError:
            print("Error al Listar los cliente")
        finally:
            self.cerrar()
