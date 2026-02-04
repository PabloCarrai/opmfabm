import sqlite3
import os


def leerArchivos(archivo):
    """
    Lee una ruta a un archivo

    :param archivo: Ruta a un archivo(sql)
    Returns:
    Devuelve el contenido de un archivo
    """
    with open(archivo, "r", encoding="utf-8") as ArchivosSql:
        consulta = ArchivosSql.read()
        return consulta


def crearDB(sentencia):
    """
    Crea una db en sqlite con el nombre datos.db

    :param sentencia: Lee una sentencia en sqlite para crear tablas
    """

    db_name = "datos.db"
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute(sentencia)
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")


archivos = [
    "sql-sentencias/1.sql",
    "sql-sentencias/2.sql",
    "sql-sentencias/3.sql",
    "sql-sentencias/4.sql",
]

#   Leo los path de cada archivos .sql, estos tienen sentencias sql para crear tablas
try:
    for archivo in archivos:
        #   leerArchivo lee lo que hay en los sql y se los pasa a crearDB
        crearDB(leerArchivos(archivo))
        print("Creacion de la db realizada")
        print("Generacion de tablas necesarias.")
except Exception as e:
    print(f"Error al querer generar las tablas de la db{e}")
