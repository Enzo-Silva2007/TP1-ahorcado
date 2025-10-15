import re

#Funciones del modelo

def tamanio_palabra(dificultad, nueva_palabra) :
    longitud = len(nueva_palabra)

    if dificultad == "facil":
        if longitud > 6:
            return False
    elif dificultad == "medio":
        if longitud < 6 or longitud > 8:
            return False
    elif dificultad == "dificil":
        if longitud < 8 or longitud > 13:
            return False

    return True

#Funciones del controlador

def nombre_valido(nombre) :
    longitud = len(nombre)

    if longitud < 4 or longitud > 13:
        return False
    elif re.findall("[ñÑ]", nombre) :
        return False

    return True


