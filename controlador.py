import dibujo as dibujo
from consoledraw import Console
import keyboard
import validacion as validacion
import modelo as modelo
import random

#Consola principal
CONSOLA = Console()

#Funciones menu
def pantalla_menu() :
    salida = True
    estado = ""
    posicion = 0

    while salida :
        with CONSOLA :
            CONSOLA.print(dibujo.PANTALLA_MENU[posicion])
        evento = keyboard.read_event()
        if evento.event_type == keyboard.KEY_DOWN :
            if evento.name == "w" :
                if posicion > 0 :
                    posicion -= 1
            elif evento.name == "s" :
                if posicion < 2 :
                    posicion += 1
            elif evento.name == "enter" :
                if posicion == 0 :
                    estado = "jugador"
                    salida = False
                elif posicion == 1 :
                    estado = "opciones"
                    salida = False
                elif posicion == 2 :
                    estado = "salir"
                    salida = False
    return estado

def pantalla_jugador() :
    salida = True
    estado = ""
    nombre = ""
    mensaje = ""

    while salida :
        with CONSOLA :
            CONSOLA.print(dibujo.PANTALLA_JUGADOR[0].format(mensaje=mensaje))

        if keyboard.is_pressed("r") :
            nombre = input("Ingrese el nuevo jugador: ")

            if not validacion.nombre_valido(nombre) :
                mensaje = "Tu nombre contiene una ñ o no tiene la longitud suficiente"
                nombre = ""
            elif modelo.obtener_jugador(nombre) :
                mensaje = "El nombre ya existe"
                nombre = ""
            else :
                salir = True
                while salir:
                    if keyboard.is_pressed("s"):
                        modelo.nuevo_jugador(nombre)
                        modelo.establecer_jugador_conectado(nombre)
                        estado = "juego"
                        salida = False
                        salir = False
                    elif keyboard.is_pressed("n"):
                        mensaje = "Operación cancelada."
                        nombre = ""
                        salir = False
        elif keyboard.is_pressed("i") :
            nombre = input("Ingrese el jugador existente: ")
            if modelo.obtener_jugador(nombre) :
                modelo.establecer_jugador_conectado(nombre)
                estado = "juego"
                salida = False
            else :
                mensaje = "No existe ese usuario, vuelva a intentarlo."

    return estado

def pantalla_opcion() :
    estado = "menu"
    salida = True
    posicion = 0

    while salida :
        with CONSOLA :
            CONSOLA.print(dibujo.PANTALLA_OPCIONES[posicion])
            CONSOLA.print(posicion)

        evento = keyboard.read_event()
        if evento.event_type == keyboard.KEY_DOWN:
            if evento.name == "w":
                if posicion > 0:
                    posicion -= 1
            elif evento.name == "s":
                if posicion < 2:
                    posicion += 1
            elif evento.name == "enter":
                salida = False
                if posicion == 0:
                    modelo.establecer_opciones("facil")
                    salida = False
                elif posicion == 1:
                    modelo.establecer_opciones("medio")
                    salida = False
                elif posicion == 2:
                    modelo.establecer_opciones("dificil")
                    salida = False
    return estado

def pantalla_juego() :
    jugador_actual = modelo.obtener_jugador_conectado()
    opciones = modelo.obtener_opciones()
    palabras = modelo.obtener_palabras(opciones["dificultad"])
    palabras = random.sample(palabras, len(palabras))
    letras_usadas = []
    evento = ""

    estado = ""
    posicion_dibujo = 0
    posicion_palabra = 0
    mensaje = ""
    salida = True
    palabra_secreta = palabras[posicion_palabra]
    palabra_formateada = list(formatear_palabra(palabra_secreta))


    while salida :
        with CONSOLA :
            CONSOLA.print(dibujo.PANTALLA_JUEGO[0].format(nombre=jugador_actual["nombre"], palabra="".join(palabra_formateada), letras_usadas=",".join(letras_usadas),mensaje=mensaje ,dibujo=dibujo.ESCENARIO[posicion_dibujo]))
            CONSOLA.print(palabras[posicion_palabra])

        if posicion_dibujo == 6 :
            estado = pantalla_perder(palabra_secreta)
            if estado == "menu" :
                salida = False
            mensaje = "Partida reiniciada. Una nueva palabra se ha generado.\nBuena suerte"
            posicion_palabra += 1
            posicion_dibujo = 0
            palabra_secreta = palabras[posicion_palabra]
            palabra_formateada = list(formatear_palabra(palabra_secreta))
            letras_usadas = []
        else :
            evento = keyboard.read_event()

        if evento.event_type == keyboard.KEY_DOWN :
            if evento.name == "p" :
                mensaje = ingresar_letra(letras_usadas, palabra_formateada, palabra_secreta)
                if mensaje == None :
                    posicion_dibujo += 1
                    mensaje = "Uh, mal ahí. Para la proxima pa."
            elif evento.name == "space" :
                mensaje = ingresar_palabra(palabra_secreta)
                if mensaje == "menu" :
                    estado = mensaje
                    salida = False
                elif mensaje == "seguir" :
                    mensaje = "Partida reiniciada. Una nueva palabra se ha generado.\nBuena suerte"
                    posicion_palabra += 1
                    posicion_dibujo = 0
                    palabra_secreta = palabras[posicion_palabra]
                    palabra_formateada = list(formatear_palabra(palabra_secreta))
                    letras_usadas = []
            elif evento.name == "esc" :
                estado = "menu"
                salida = False
    return estado


def pantalla_victoria(palabra_secreta) :
    jugador_actual = modelo.obtener_jugador_conectado()
    modelo.agregar_gano(jugador_actual["nombre"])
    estado = ""
    salida = True

    while salida :
        with CONSOLA :
            CONSOLA.print(dibujo.PANTALLA_VICTORIA[0].format(palabra=palabra_secreta))
        evento = keyboard.read_event()
        if evento.event_type == keyboard.KEY_DOWN :
            if evento.name == "esc" :
                estado = "menu"
                salida = False
            elif evento.name == "enter" :
                estado = "seguir"
                salida = False
    return estado

def pantalla_perder(palabra_secreta) :
    estado = ""
    salida = True

    while salida :
        with CONSOLA :
            CONSOLA.print(dibujo.PANTALLA_PERDISTE[0].format(palabra=palabra_secreta))
        evento = keyboard.read_event()
        if evento.event_type == keyboard.KEY_DOWN :
            if evento.name == "esc" :
                estado = "menu"
                salida = False
            elif evento.name == "enter" :
                estado = "seguir"
                salida = False
    return estado


#Funciones de control

def formatear_palabra(palabra_secreta) :
    palabra_formateada = ""
    for i in range(len(palabra_secreta)) :
        palabra_formateada += "_"
    return palabra_formateada

def ingresar_letra(letras_usadas, palabra_formateada, palabra_secreta) :
    letra = input("Igrese una sola letra: ").lower().strip()

    if not validacion.letra_valida(letra) :
        return "Has ingresado mas de una letra \no un caracter inválido."

    letra = str(letra)
    if letra in letras_usadas :
        return "Ya has usado esta letra"

    letras_usadas.append(letra)

    if letra in palabra_secreta :
        for i, l in enumerate(palabra_secreta) :
            if l == letra :
                palabra_formateada[i] = letra

        return "Muy bien, seguí asi crack, máquina, distinto."
    else :
        return None

def ingresar_palabra(palabra_secreta) :
    palabra = input("Ingrese la palabra completa, si fallas, perderá automáticamente: ").lower().strip()

    if not validacion.palabra_valida(palabra_secreta, palabra) :
        return "Ingresaste un caracter inválido \no la palabra no tiene la misma longitud."

    if palabra_secreta == palabra :
        mensaje = pantalla_victoria(palabra_secreta)
        return mensaje
    else :
        mensaje = pantalla_perder(palabra_secreta)
        return mensaje
