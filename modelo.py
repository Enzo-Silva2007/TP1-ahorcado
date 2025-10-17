import json
import validacion as validacion

DATOS = "datos"

#Fuciones de jugador
def obtener_datos() :
    datos = {}
    with open(DATOS + ".json", "r") as archivo :
        datos = json.load(archivo)
    return datos

def nuevo_jugador(nombre) :
    jugador = {}

    if not nombre :
        return None
    datos = obtener_datos()

    jugador = {"nombre" : nombre, "gano": 0}

    if obtener_jugador(jugador["nombre"]) :
        return False

    datos["jugador"].append(jugador)

    with open(DATOS + ".json", "w") as archivo :
        archivo.write(json.dumps(datos, indent=4))
    return True

def obtener_jugador(nombre) :
    datos = obtener_datos()
    jugador_obtenido = {}

    for i, jugador in enumerate(datos["jugador"]):
        if nombre == jugador["nombre"] :
            jugador_obtenido = jugador

    if not jugador_obtenido :
        return {}

    return jugador_obtenido


def obtener_mayor_ganador() :
    datos = obtener_datos()
    mayor_ganador = {}

    for i, jugador in enumerate(datos["jugador"]) :
        if i == 0 :
            mayor_ganador = jugador
        if i != 0 :
            if jugador["gano"] > mayor_ganador["gano"] :
                mayor_ganador = jugador

    return mayor_ganador

def agregar_gano(jugador) :
    datos = obtener_datos()
    jugador_actual = obtener_jugador(jugador)

    for j in datos["jugador"] :
        if j["nombre"] == jugador :
            j["gano"] += 1
            datos["jugador_conectado"]["gano"] += 1
            continue


    with open(DATOS + ".json", "w") as archivo :
        archivo.write(json.dumps(datos, indent=4))

agregar_gano("enzo")
def establecer_jugador_conectado(nombre) :
    datos = obtener_datos()
    jugador_conectado = {}

    if obtener_jugador(nombre) :
        jugador_conectado = obtener_jugador(nombre)

    datos["jugador_conectado"] = jugador_conectado

    with open(DATOS + ".json", "w") as archivo :
        json.dump(datos, archivo, indent=4)

def obtener_jugador_conectado() :
    datos = obtener_datos()
    return datos["jugador_conectado"] if datos["jugador_conectado"] else None

#Funciones de juego

def establecer_opciones(dificultad) :
    datos = obtener_datos()

    if dificultad :
        datos["opciones"]["dificultad"] = dificultad

    with open(DATOS + ".json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

def obtener_opciones() :
    datos = obtener_datos()

    return datos["opciones"]

def obtener_palabras(dificultad) :
    if not dificultad:
        return []

    datos = obtener_datos()
    palabras = datos["dificultad"].get(dificultad)
    return palabras

def agregar_palabra(dificultad, nueva_palabra) :
    if not dificultad or not nueva_palabra:
        return None

    if not validacion.tamanio_palabra(dificultad, nueva_palabra) :
        return False

    datos = obtener_datos()

    if nueva_palabra in datos["dificultad"][dificultad] :
        return False

    datos["dificultad"].get(dificultad).append(nueva_palabra)

    with open(DATOS + ".json", "w") as archivo:
        archivo.write(json.dumps(datos, indent=4))
    return True

