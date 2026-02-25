def validar_entradas_vacias(datos):
    return all(dato.strip() for dato in datos)


datos = ["3", "3", "2"]
print(validar_entradas_vacias(datos))
