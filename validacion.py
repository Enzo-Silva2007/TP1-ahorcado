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

def letra_valida(letra) :

    if len(letra) > 1 or re.findall("[ñÑ]", letra)  :
        return False
    try :
        str(letra)
        return True
    except ValueError:
        return False

def palabra_valida(palabra_secreta, palabra) :
    if len(palabra_secreta) != len(palabra) or re.findall("[ñÑ]", palabra):
        return False
    try :
        str(palabra)
        return True
    except ValueError :
        return False