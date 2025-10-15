#Librerias necesarias para el funcionamiento correcto del proyecto: consoledraw y keyboard
import controlador as controlador
from time import sleep

def main() :
    estado_pantalla = "menu"
    salida = True

    while salida :
        if estado_pantalla == "menu" :
            estado_pantalla = controlador.pantalla_menu()
        elif estado_pantalla == "jugador" :
            estado_pantalla = controlador.pantalla_jugador()
        elif estado_pantalla == "opciones" :
            estado_pantalla = controlador.pantalla_opcion()
            sleep(1)
        elif estado_pantalla == "juego" :
            estado_pantalla = controlador.pantalla_juego()

main()

