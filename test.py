from consoledraw import Console
import keyboard
import time
import dibujo as dibujo

consola = Console()
salida = True

def hola() :
    print(f"Hola")

def no_saludar() :
    print("Ingresaste un nombre muy corto")

#Ejemplos de uso con hotkey y eventos


def salir() :
    global salida
    salida = False

def bucle() :

#Los eventos add_hoykey son asincronicos, es decir, funcionan sin necesidad de un bucle
#Si se fijan, la llamada de bucle() y el inicio del ciclo while se puede ejecutar y a la vez utilizar el teclado para cortar la ejecucion
    keyboard.add_hotkey('q', lambda : salir())
    keyboard.add_hotkey('s', lambda: print('Se preciono la s'))

    while salida:
        print("Saludo: s. Despedida : d. Salir : q")
        time.sleep(1)

def bucle_dos() :
    salida = True
    while salida:
        evento = keyboard.read_event()
        print("Saludo: s. Despedida : d. Salir : q")
        if evento.event_type == keyboard.KEY_DOWN and evento.name == "q" :
            salida = False
        elif evento.event_type == keyboard.KEY_DOWN and evento.name == "s" :
            hola()

#Este es un ejemplo de como podriamos usar consola y keyboard al mismo tiempo

def funcion_consola():
    posicion = 0  # 0 = Empezar juego, 1 = Opciones

    while True:
        with consola:
            consola.clear()
            consola.print(dibujo.menu_spray[posicion])

        if posicion == 2:
            keyboard.clear_all_hotkeys()
            funcion_carga()

        if keyboard.is_pressed('w'):
            posicion = 0
            time.sleep(0.2)
        elif keyboard.is_pressed('s'):
            posicion = 1
            time.sleep(0.2)
        elif keyboard.is_pressed("space") :
            posicion = 2
def funcion_carga():
    consola.clear()
    pos = 0
    while True :
        with consola :
            consola.print(dibujo.welcome_screen[0])

        if keyboard.is_pressed("e") :
            keyboard.clear_all_hotkeys()
            funcion_ahorcado()


def funcion_ahorcado() :
    consola.clear()

    keyboard.add_hotkey("esc", lambda : salir())
    while salida :
        with consola :
            consola.print(dibujo.game[0])




bucle_dos()