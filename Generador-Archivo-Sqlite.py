import sqlite3
import os



def leerArchivos(archivo):
    with open(archivo,"r",encoding="utf-8") as ArchivosSql:
        consulta=ArchivosSql.read()
        return consulta



def crearDB(tabla):
    db_name = "datos.db"
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute(tabla)
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")


# try:
#     crearDB()
#     print("Deberia de estar creada la db con una tabla")
# except Exception as e:
#     print(f"Error {e}")

archivos=["sql-sentencias/1.sql","sql-sentencias/2.sql","sql-sentencias/3.sql","sql-sentencias/4.sql"]
for archivo in archivos:
    print(archivo)


