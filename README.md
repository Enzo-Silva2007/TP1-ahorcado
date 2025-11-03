# Juego del Ahorcado en Python

Este proyecto fue desarrollado en Python como trabajo práctico para la facultad.  
El objetivo es implementar una versión de consola del clásico juego del ahorcado, utilizando una estructura modular y almacenamiento de datos mediante archivos JSON.

---

## Descripción del juego

El jugador debe adivinar una palabra secreta letra por letra antes de que se complete el dibujo del ahorcado.  
Cada error añade una parte del cuerpo al dibujo, y la partida termina cuando el jugador logra descubrir la palabra o alcanza el número máximo de errores permitidos.  

El juego cuenta con registro de jugadores, niveles de dificultad, validación de entradas y guardado automático del progreso en un archivo JSON.

---

## Funcionalidades

- Interfaz de consola interactiva.  
- Detección de eventos de teclado en tiempo real mediante la librería keyboard.  
- Selección de nivel de dificultad: fácil, medio o difícil.  
- Registro e inicio de sesión de jugadores.  
- Guardado persistente de victorias por jugador.  
- Dibujos ASCII para cada estado del ahorcado.  
- Validaciones de entradas para asegurar la correcta ejecución.

---

## Instrucciones de uso

1. **Ejecución del programa**  
   Abrir una terminal en el directorio del proyecto y ejecutar:
   ```
   python main.py
   ```

2. **Navegación por el menú principal**  
   Utilizar las teclas **W** y **S** para desplazarse por las opciones y **ENTER** para confirmar.  
   Las opciones disponibles son:
   - Empezar juego  
   - Cambiar dificultad  
   - Salir  

3. **Gestión de jugadores**  
   En la pantalla de jugador se puede:  
   - Presionar **R** para registrar un nuevo usuario (nombre de 4 a 13 letras, sin acentos).  
   - Presionar **I** para ingresar con un usuario ya existente.

4. **Juego**  
   Una vez iniciado el juego:
   - Presionar **P** para ingresar una letra.  
   - Presionar **ESPACIO** para intentar adivinar la palabra completa.  
   - Presionar **ESC** para volver al menú principal.  

   Cada acierto revela letras de la palabra; cada error avanza el dibujo del ahorcado.  
   Al completar la palabra, se muestra una pantalla de victoria. Si se agotan los intentos, se muestra la pantalla de derrota.

5. **Fin de la partida**  
   El número de victorias de cada jugador se guarda automáticamente en el archivo `datos.json`.  
   Desde la pantalla final se puede volver al menú presionando **ESC**.

---

## Requisitos

- Python 3.8 o superior instalado.  
- Librerías necesarias:
  - keyboard  
  - consoledraw  

Instalación de dependencias:
```
pip install keyboard consoledraw
```

---

## Estructura del proyecto

Ahorcado/

│  
├── main.py             (punto de inicio del programa)  
├── controlador.py      (controla las pantallas y la lógica del juego)  
├── modelo.py           (maneja la lectura y escritura de datos en JSON)  
├── validacion.py       (verifica nombres, letras y palabras)  
├── dibujo.py           (contiene los dibujos ASCII del juego)  
├── constantes.py       (define teclas y estados globales del programa)  
└── datos.json          (almacena los jugadores, palabras y configuraciones)

---

## Contribución

Proyecto desarrollado por:  
 
- Gian Franco Caputo  
- Enzo Silva  
- Candela Mañas
- Thiago Alegre  
- Germán Gómez  

---

## Licencia

Proyecto de uso educativo.