def validarNoEsteVacio(*textos):
    """
    Valida que textos tenga algun string o no este vacio

    :param textos: Los string a evaluar
    Returns:
    Devuelve True si se cumple que no tenga cadenas vacias
    """
    try:
        for texto in textos:
            if texto == "" or len(texto) == 0:
                raise ValueError("Al menos uno de los textos estan vacios ")
        return True
    except ValueError as e:
        print(f"Error {e}")
