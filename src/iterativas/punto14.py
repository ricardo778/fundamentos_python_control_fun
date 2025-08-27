import random  

# Genera un número aleatorio entre 1 y 10 como objetivo a adivinar
objetivo = random.randint(1, 10)
intentos = 0   # Contador de intentos realizados
adivinado = False  # Bandera para saber si el jugador acertó

# El jugador tiene máximo 3 intentos para adivinar el número
while not adivinado and intentos < 3:
    intentos += 1  # Se incrementa el intento
    # Se pide al jugador que ingrese un número
    numero = int(input(f"Intento {intentos}/3: Adivina un número del 1 al 10: "))

    # Si el número coincide con el objetivo, se gana el juego
    if numero == objetivo:
        print(f"¡Correcto! Has adivinado en {intentos} intentos.")
        adivinado = True
    else:
        # Se da una pista: si el objetivo es mayor o menor al número ingresado
        pista = "mayor" if numero < objetivo else "menor"
        print(f"Incorrecto. El número es {pista} que {numero}.")

# Si no se acierta en los 3 intentos, se muestra el número correcto
if not adivinado:
    print(f"Se acabaron los intentos. El número era {objetivo}.")
