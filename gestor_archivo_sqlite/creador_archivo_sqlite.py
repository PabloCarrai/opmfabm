import os

carpeta_sql = "gestor_archivo_sqlite/sqls"

dir_script = os.path.dirname(__file__)  #   Carpeta actual
ruta_archivo = os.path.join(dir_script, "..", "gestor_archivo_sqlite", "archivo_db.db")


if os.path.exists(carpeta_sql):
    archivos = os.listdir(carpeta_sql)
    for archivo in archivos:
        if archivo.endswith(".sql"):
            ruta_completa = os.path.join(carpeta_sql, archivo)
            print(f"Leyendo {archivo}")
            with open(ruta_completa, "r", encoding="utf-8") as f:
                contenido = f.read()
else:
    print("La carpeta sqls no existe")