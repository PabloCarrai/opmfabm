import re
from aux import verifica_correo_existe


def validar_entradas_vacias(datos):
    return all(dato.strip() for dato in datos)


def validar_formato_correo(correo):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, correo):
        return True
    return False



#   1) todos los campos con datos       validar_entradas_vacias(datos)
#   2) el formato del correo valido     validar_formato_correo
#   3) el correo no exista en la db

# validar_formato_correo(self.stringVarCorreolabelFrame.get()):
# if verifica_correo_existe:
# datos = ["3", "3", "1"]
# print(validar_formato_correo("pcarrai@gmail.com"))
# print(validar_entradas_vacias(datos))
# print(validar_entradas_vacias(datos))
# print(validar_formato_correo("pablocarrai@gmail.com"))

print(verifica_correo_existe("@gmail.com"))
# verifica_correo_existe("")
