import re
import keyboard

# funciones del controlador

def nombre_valido(nombre):
    if not isinstance(nombre, str):
        return False
    n = nombre.strip().lower()
    if len(n) < 4 or len(n) > 13:
        return False
    # solo letras a-z sin acentos ni ñ
    return re.fullmatch(r"[a-z]+", n) is not None

def letra_valida(letra):
    if not isinstance(letra, str):
        return False
    l = letra.strip().lower()
    # tiene que ser una sola letra a-z
    return re.fullmatch(r"[a-z]", l) is not None

def palabra_valida(palabra_secreta, palabra):
    if not isinstance(palabra, str):
        return False
    p = palabra.strip().lower()
    if len(palabra_secreta) != len(p):
        return False
    # todas letras a-z, sin acentos; longitud correcta
    return re.fullmatch(r"[a-z]+", p) is not None
