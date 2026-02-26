import re


def validar_entradas_vacias(datos):
    return all(dato.strip() for dato in datos)


def validar_formato_correo(correo):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, correo):
        return True
    return False


# datos = ["3", "3", "2"]
# print(validar_entradas_vacias(datos))
#print(validar_formato_correo("pablocarrai@gmail.com"))
