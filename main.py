import controlador as controlador
import constantes as C

def main():
    estado_pantalla = C.ESTADO_MENU
    salida = True

    while salida:
        if estado_pantalla == C.ESTADO_MENU:
            estado_pantalla = controlador.mostrar_menu()
        elif estado_pantalla == C.ESTADO_JUGADOR:
            estado_pantalla = controlador.gestionar_jugador()
        elif estado_pantalla == C.ESTADO_OPCIONES:
            estado_pantalla = controlador.mostrar_opciones()
        elif estado_pantalla == C.ESTADO_JUEGO:
            estado_pantalla = controlador.mostrar_juego()
        elif estado_pantalla == C.ESTADO_SALIR:
            salida = False
        else:
            estado_pantalla = C.ESTADO_MENU

if __name__ == "__main__":
    main()