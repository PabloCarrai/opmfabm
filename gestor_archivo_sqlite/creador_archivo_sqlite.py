import os

dir_script = os.path.dirname(__file__)  #   Carpeta actual
ruta_archivo = os.path.join(
    dir_script, "..", "gestor_archivo_sqlite", "archivo_db.db"
)

with open(ruta_archivo,"w+") as f:
    datos = f.read()
    print(datos)
