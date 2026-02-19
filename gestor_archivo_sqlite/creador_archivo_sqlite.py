import os
from gestor_db import gestorDB as gdb

#   Aca tengo archivos con numeros.sql para correr la creacion de las tablas
carpeta_sql = "gestor_archivo_sqlite/sqls"
#   Esto es la carpeta actual
dir_script = os.path.dirname(__file__)  #   Carpeta actual
#   La ruta del archivo archivo_db.db(donde guarda sqlite3)
ruta_archivo = os.path.join(dir_script, "archivo_db.db")

#   Reviso si la carpeta sql existe
if os.path.exists(carpeta_sql):
    #   Listo los directorios
    archivos = os.listdir(carpeta_sql)
    for archivo in archivos:
        #   Reviso que los archivos terminen con .sql
        if archivo.endswith(".sql"):
            #   Armo la ruta
            ruta_completa = os.path.join(carpeta_sql, archivo)
            with open(ruta_completa, "r", encoding="utf-8") as f:
                #   Leo el contenido de cada archivo .sql
                contenido = f.read()
                #   Conecto a la db pasandole la ruta del archivo archivo_db.db
                base = gdb(ruta_archivo)
                #   paso las secuencias sql en los archivos a la funcion crear_tablas
                base.crear_tablas(contenido)
                #   Cierro la conexion
                base.cerrar()
else:
    print("La carpeta sqls no existe")
