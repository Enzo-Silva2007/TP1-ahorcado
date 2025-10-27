import dibujo
from consoledraw import Console
import keyboard
import validacion
import modelo
import random
import constantes as C

CONSOLA = Console()


def mostrar_menu():
    salida = True
    estado = ""
    posicion = 0
    total = len(dibujo.PANTALLA_MENU)
    while salida:
        with CONSOLA:
            CONSOLA.print(dibujo.PANTALLA_MENU[posicion])
        evento = keyboard.read_event()
        if evento.event_type == keyboard.KEY_DOWN:
            if evento.name == C.K_ARRIBA and posicion > 0:
                posicion -= 1
            elif evento.name == C.K_ABAJO and posicion < total - 1:
                posicion += 1
            elif evento.name == C.K_ENTRAR:
                if posicion == 0:
                    estado = C.ESTADO_JUGADOR
                elif posicion == 1:
                    estado = C.ESTADO_OPCIONES
                elif posicion == 2:
                    estado = C.ESTADO_SALIR
                salida = False
    return estado


def gestionar_jugador():
    salida = True
    estado = ""
    mensaje = ""
    tecla_bloqueada = None
    while salida:
        with CONSOLA:
            CONSOLA.print(dibujo.PANTALLA_JUGADOR[0].format(mensaje=mensaje))
        evento = keyboard.read_event()
        if evento.event_type == keyboard.KEY_UP and tecla_bloqueada == evento.name:
            tecla_bloqueada = None
            continue
        if evento.event_type == keyboard.KEY_DOWN:
            if evento.name in (C.K_REGISTRAR, C.K_INGRESAR):
                if tecla_bloqueada == evento.name:
                    continue
                tecla_bloqueada = evento.name
            if evento.name == C.K_REGISTRAR:
                salida = False
                nombre = input("Ingrese el nuevo jugador: ").strip()
                if not validacion.nombre_valido(nombre):
                    mensaje = "Nombre inválido: debe tener 4 a 13 letras sin acentos."
                    salida = True
                elif modelo.obtener_jugador(nombre):
                    mensaje = "El nombre ya existe"
                    salida = True
                else:
                    print("Confirmar creación del jugador. Presiona 's' para confirmar o 'n' para cancelar.")
                    confirmar = True
                    while confirmar:
                        e = keyboard.read_event()
                        if e.event_type == keyboard.KEY_DOWN:
                            if e.name == C.K_SI:
                                modelo.nuevo_jugador(nombre)
                                modelo.establecer_jugador_conectado(nombre)
                                estado = C.ESTADO_JUEGO
                                salida = False
                                confirmar = False
                            elif e.name == C.K_NO:
                                mensaje = "Operación cancelada."
                                confirmar = False
                                salida = True

            elif evento.name == C.K_INGRESAR:
                salida = False
                nombre = input("Ingrese el jugador existente: ").strip()
                if modelo.obtener_jugador(nombre):
                    modelo.establecer_jugador_conectado(nombre)
                    estado = C.ESTADO_JUEGO
                    salida = False
                else:
                    mensaje = "No existe ese usuario, vuelva a intentarlo."
                    salida = True
    return estado


def mostrar_opciones():
    salida = True
    estado = C.ESTADO_MENU
    posicion = 0
    total = len(dibujo.PANTALLA_OPCIONES)
    while salida:
        with CONSOLA:
            CONSOLA.print(dibujo.PANTALLA_OPCIONES[posicion])
        evento = keyboard.read_event()
        if evento.event_type == keyboard.KEY_DOWN:
            if evento.name == C.K_ARRIBA and posicion > 0:
                posicion -= 1
            elif evento.name == C.K_ABAJO and posicion < total - 1:
                posicion += 1
            elif evento.name == C.K_ENTRAR:
                if posicion == 0:
                    modelo.establecer_opciones("facil")
                elif posicion == 1:
                    modelo.establecer_opciones("medio")
                elif posicion == 2:
                    modelo.establecer_opciones("dificil")
                salida = False
    return estado


def mostrar_juego():
    jugador_actual = modelo.obtener_jugador_conectado()
    opciones = modelo.obtener_opciones()
    palabras = modelo.obtener_palabras(opciones["dificultad"])
    palabras = random.sample(palabras, len(palabras))
    if not palabras:
        return C.ESTADO_MENU
    letras_usadas = []
    estado = ""
    posicion_dibujo = 0
    posicion_palabra = 0
    mensaje = ""
    salida = True
    palabra_secreta = palabras[posicion_palabra]
    palabra_formateada = list(formatear_palabra(palabra_secreta))
    tecla_bloqueada = None
    while salida:
        with CONSOLA:
            CONSOLA.print(dibujo.PANTALLA_JUEGO[0].format(
                nombre=jugador_actual["nombre"],
                palabra="".join(palabra_formateada),
                letras_usadas=",".join(letras_usadas),
                mensaje=mensaje,
                dibujo=dibujo.ESCENARIO[posicion_dibujo]
            ))
        if posicion_dibujo == 6:
            estado = mostrar_derrota(palabra_secreta)
            return estado
        evento = keyboard.read_event()
        if evento.event_type == keyboard.KEY_UP and tecla_bloqueada == evento.name:
            tecla_bloqueada = None
            continue
        if evento.event_type == keyboard.KEY_DOWN:
            if evento.name in (C.K_JUGAR, C.K_ESPACIO):
                if tecla_bloqueada == evento.name:
                    continue
                tecla_bloqueada = evento.name
            if evento.name == C.K_JUGAR:
                mensaje, acierto = ingresar_letra(letras_usadas, palabra_formateada, palabra_secreta)
                if not acierto:
                    posicion_dibujo += 1
                    if mensaje is None:
                        mensaje = "Uh, mal ahí. Para la proxima pa."
                if "_" not in palabra_formateada:
                    estado = mostrar_victoria(palabra_secreta)
                    return estado
            elif evento.name == C.K_ESPACIO:
                estado = ingresar_palabra(palabra_secreta)
                return estado
            elif evento.name == C.K_ESC:
                return C.ESTADO_MENU
    return estado


def mostrar_victoria(palabra_secreta):
    jugador_actual = modelo.obtener_jugador_conectado()
    modelo.agregar_gano(jugador_actual["nombre"])
    estado = ""
    salida = True
    while salida:
        with CONSOLA:
            CONSOLA.print(dibujo.PANTALLA_VICTORIA[0].format(palabra=palabra_secreta))
        evento = keyboard.read_event()
        if evento.event_type == keyboard.KEY_DOWN:
            if evento.name == C.K_ESC:
                estado = C.ESTADO_MENU
                salida = False
            elif evento.name == C.K_ENTRAR:
                estado = C.ESTADO_SEGUIR
                salida = False
    return estado


def mostrar_derrota(palabra_secreta):
    estado = ""
    salida = True
    while salida:
        with CONSOLA:
            CONSOLA.print(dibujo.PANTALLA_PERDISTE[0].format(palabra=palabra_secreta))
        evento = keyboard.read_event()
        if evento.event_type == keyboard.KEY_DOWN:
            if evento.name == C.K_ESC:
                estado = C.ESTADO_MENU
                salida = False
            elif evento.name == C.K_ENTRAR:
                estado = C.ESTADO_SEGUIR
                salida = False
    return estado


def formatear_palabra(palabra_secreta):
    return ["_"] * len(palabra_secreta)


def ingresar_letra(letras_usadas, palabra_formateada, palabra_secreta):
    letra = input("Ingrese una sola letra: ").lower().strip()
    if not validacion.letra_valida(letra):
        return "Ingresaste más de una letra o un carácter inválido.", False
    letra = str(letra)
    if letra in letras_usadas:
        return "Ya usaste esta letra", False
    letras_usadas.append(letra)
    if letra in palabra_secreta:
        for i, l in enumerate(palabra_secreta):
            if l == letra:
                palabra_formateada[i] = letra
        return "Muy bien, seguí así crack.", True
    else:
        return None, False


def ingresar_palabra(palabra_secreta):
    palabra = input("Ingresa la palabra completa; si fallas, perdés automáticamente: ").lower().strip()
    if not validacion.palabra_valida(palabra_secreta, palabra):
        return C.ESTADO_MENU
    if palabra_secreta == palabra:
        return mostrar_victoria(palabra_secreta)
    else:
        return mostrar_derrota(palabra_secreta)
