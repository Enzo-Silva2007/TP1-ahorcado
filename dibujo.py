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
╔════════════════════════════════╗

            ¡PERDISTE!

        La palabra era: {palabra}

       Presiona ESPACIO para
          volver al menú...

╚════════════════════════════════╝
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

