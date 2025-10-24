PANTALLA_MENU = [

"""
╔════════════════════════════════════════════════════╗
║                                                    ║
║              BIENVENIDO AL AHORCADO                ║
║                                                    ║
║                  ╔════════════════╗                ║
║                  ║  EMPEZAR JUEGO ║                ║
║                  ╚════════════════╝                ║
║                                                    ║
║                        OPCIONES                    ║
║                                                    ║
║                                                    ║
║                         SALIR                      ║
║                                                    ║
╚════════════════════════════════════════════════════╝
""",

"""
╔════════════════════════════════════════════════════╗
║                                                    ║
║              BIENVENIDO AL AHORCADO                ║
║                                                    ║
║                    EMPEZAR JUEGO                   ║
║                                                    ║
║                  ╔════════════════╗                ║
║                  ║    OPCIONES    ║                ║
║                  ╚════════════════╝                ║
║                                                    ║
║                                                    ║
║                         SALIR                      ║
║                                                    ║
╚════════════════════════════════════════════════════╝
""",
"""
╔════════════════════════════════════════════════════╗
║                                                    ║
║              BIENVENIDO AL AHORCADO                ║
║                                                    ║
║                    EMPEZAR JUEGO                   ║
║                                                    ║
║                                                    ║
║                       OPCIONES                     ║
║                                                    ║
║                                                    ║
║                  ╔════════════════╗                ║
║                  ║      SALIR     ║                ║
║                  ╚════════════════╝                ║
╚════════════════════════════════════════════════════╝
"""
]

PANTALLA_OPCIONES = [

"""
╔════════════════════════════════╗
║                                ║
║          OPCIONES DEL          ║
║             JUEGO              ║
║                                ║
║          DIFICULTAD:           ║
║                                ║
║        ████████████████        ║
║        █   FÁCIL       █       ║
║        ████████████████        ║
║            MEDIO               ║
║            DIFÍCIL             ║
║                                ║
╚════════════════════════════════╝
""",


"""
╔════════════════════════════════╗
║                                ║
║          OPCIONES DEL          ║
║             JUEGO              ║
║                                ║
║          DIFICULTAD:           ║
║                                ║
║            FÁCIL               ║
║        ████████████████        ║
║        █   MEDIO       █       ║
║        ████████████████        ║
║            DIFÍCIL             ║
║                                ║
╚════════════════════════════════╝
""",


"""
╔════════════════════════════════╗
║                                ║
║          OPCIONES DEL          ║
║             JUEGO              ║
║                                ║
║          DIFICULTAD:           ║
║                                ║
║            FÁCIL               ║
║            MEDIO               ║
║        ████████████████        ║
║        █  DIFÍCIL      █       ║
║        ████████████████        ║
║                                ║
╚════════════════════════════════╝
"""
]



PANTALLA_JUEGO = [
    """
╔══════════════════════════════════════════════╗
║                                              ║
║               JUEGO DEL AHORCADO             ║
║                                              ║
╠══════════════════════════════════════════════╣
   Jugador : {nombre}

   Palabra: {palabra}

   Letras usadas: {letras_usadas}

   Si quiere adivinar letra, presione "p". Si
   quiere intentar con la palabra entera,
   presione "ESPACIO".
   Si no quiere continuar jugando, presione
   "ESC".

   {mensaje}

╠══════════════════════════════════════════════╣
                    {dibujo}
╚══════════════════════════════════════════════╝

    """
]

ESCENARIO = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]

PANTALLA_PERDISTE = [
"""
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║                        ████████████████                        ║
║                        █  ¡PERDISTE!  █                        ║
║                        ████████████████                        ║
║                                                                ║
                     La palabra era: {palabra}
║                                                                ║
║          ──────────────────────────────────────────            ║
║                                                                ║
║                 Presiona ESC para volver al menú               ║
║                 O ENTER para jugar otra partida                ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
"""
]


PANTALLA_JUGADOR = [
"""
╔════════════════════════════════════════════════════╗
║                                                    ║
║                   ¡BIENVENIDO!                     ║
║                                                    ║
║                        Antes                       ║
║             Ingresa tu nombre abajo.               ║
║         Si no existe, se creará uno nuevo.         ║
║                                                    ║
║════════════════════════════════════════════════════║

               Presione ENTER para ver
                     su nombre.

     Presione R para registrar un nuevo jugador.
     Seguidamente presione S si quiere continuar o
            N para cancelar la operación
   Presione I si quiere usar un jugador existente.

{mensaje}

══════════════════════════════════════════════════════
"""
]

PANTALLA_VICTORIA = [
"""
╔════════════════════════════════════════════════════╗
║                                                    ║
║                 ¡FELICIDADES!                      ║
║                 ¡GANASTE!                          ║
║                                                    ║
║             Has adivinado la palabra.              ║
║                                                    ║
                  Palabra: {palabra}
║                                                    ║
║          Presiona ESC para volver al menú          ║
║          o ENTER para jugar otra partida.          ║
║                                                    ║
╚════════════════════════════════════════════════════╝
"""
]


