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

        if keyboard.is_pressed("w") :
            posicion = 0
        elif keyboard.is_pressed("s") :
            posicion = 1
        elif keyboard.is_pressed("enter") :
            if posicion == 0 :
                estado = "jugador"
                salida = False
            elif posicion == 1 :
                estado = "opciones"
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

    estado = ""
    posicion = 0
    posicion_palabra = 0
    salida = True
    palabra_secreta = formatear_palabra(palabras, posicion_palabra)


    while salida :
        with CONSOLA :
            CONSOLA.print(dibujo.PANTALLA_JUEGO[0].format(nombre=jugador_actual["nombre"], palabra=palabra_secreta, letras_usadas="", dibujo=dibujo.ESCENARIO[posicion]))
            CONSOLA.print(palabras[posicion_palabra])


#Funciones de control

def formatear_palabra(palabras, posicion_palabra) :
    palabra_secreta = ""
    for i in range(len(palabras[posicion_palabra])) :
        palabra_secreta += "_"
    return palabra_secreta