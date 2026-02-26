import sys
import os

#   Esto me deja importar gestor_archivo_sqlite.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from archivo_db.gestor_hijo_db import Gestor_Hijo as gh

#   Se repetia mucho en cada funcion el nombre del archivo, asi se ve mejor
archivo_Db = "gestor_archivo_sqlite/archivo_db.db"


def insertar(datos, sentencia):
    """
    Se necesita datos y sentencia.
    Datos son una tupla con los datos necesarios en base a sentencia
    sentencia es una sql para una insercion.
    """
    db = gh(archivo_Db)
    db.insertar_Registro(datos, sentencia)
    db.cerrar()
    print(f" Registro {datos} insertado")


def eliminar(datos, sentencia):
    """
    Se necesita datos y sentencia.
    Datos son una tupla con los datos necesarios en base a sentencia
    sentencia es una sql para una eliminar datos.
    """
    db = gh(archivo_Db)
    db.eliminar_Registro(datos, sentencia)
    db.cerrar()
    print(f" Registro {datos} Eliminado")


def actualizar(datos, sentencia):
    """
    Se necesita datos y sentencia.
    Datos son una tupla con los datos necesarios en base a sentencia
    sentencia es una sql para una actualizacion.
    """
    db = gh(archivo_Db)
    db.actualizar_Registro(datos, sentencia)
    db.cerrar()
    print(f" Registro {datos} Actualizado")

def verifica_correo_existe(correo):
    sentencia = "select email from clientes where email=?"
    datos = (correo,)
    db = gh(archivo_Db)
    resultado = db.verificar_correo_existente(datos, sentencia)
    db.cerrar()
    return resultado
    


print(verifica_correo_existe("gdaraoez@gmail.com"))