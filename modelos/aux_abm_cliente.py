import re

from modelos.aux import verifica_correo_existe


def validar_entradas_vacias(datos):
    return all(dato.strip() for dato in datos)


def validar_formato_correo(correo):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, correo):
        return True
    return False


def chequeo_todo_abm_cliente(datos):
    if (
        validar_entradas_vacias(datos)
        and validar_formato_correo(datos[2])
        and verifica_correo_existe(datos[2])
    ):
        return True
    else:
        return False


#   1) todos los campos con datos       validar_entradas_vacias(datos)
#   2) el formato del correo valido     validar_formato_correo
#   3) el correo no exista en la db

# validar_formato_correo(self.stringVarCorreolabelFrame.get()):
# if verifica_correo_existe:
# datos = ["3", "3", "pablocarradi@gmail.com", "1"]
# print(chequeo_todo_abm_cliente(datos))
# print(validar_formato_correo("pcarrai@gmail.com"))
# print(validar_entradas_vacias(datos))
# print(validar_entradas_vacias(datos))
# print(validar_formato_correo("pablocarrai@gmail.com"))

# print(verifica_correo_existe("@gmail.com"))
# verifica_correo_existe("")
