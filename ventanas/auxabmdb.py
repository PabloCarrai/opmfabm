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
            #   Creo un cursor
            cursor = self.conexion.cursor()
            #   Ejecuto la consulta pasando los datos que se usan en el abm
            cursor.execute(consulta, datos)
            #   Commiteo estos cambios en la db
            self.conexion.commit()
            print("Clientes guardados con exito")
        except sqlite3.IntegrityError:
            print("Error al guardar cliente")
        finally:
            #   Por ultimo cierro la conexion
            self.cerrar()

    def listarClientesExistentes(self):
        """
        Este metodo nos lista los clientes existentes en la db

        Returns:
        Devuelve lo que hay en la db consultando la sql consulta
        """
        consulta = "select id_cliente,nombre,apellido,dni,email,telefono from clientes"
        try:
            #   Creo el objeto instancia del tipo DB
            cursor = DB()
            #   Sobre dicho objeto llamo al metodo conectar(devuelve un cursor)
            cursor = cursor.conectar()
            #   Ejecuto la consulta
            cursor.execute(consulta)
            #   Devuelvo los registros a una variable
            usuariosExistentes = cursor.fetchall()
            #   Retorno esos datos
            return usuariosExistentes
        except sqlite3.IntegrityError:
            print("Error al Listar los cliente")
        finally:
            #   Por ultimo cierro la conexion a la db
            self.cerrar()
