# Bucle infinito que se repetirá hasta que el usuario decida salir
while True:
    # Pido al usuario que indique si quiere continuar o no
    respuesta = input("¿Quieres continuar? (s/n): ").lower()  # Convierto la respuesta a minúsculas para normalizar

    # Si el usuario responde 'n', salgo del bucle
    if respuesta == "n":
        print("Programa finalizado.")
        break  # Termino el bucle

    # Si el usuario responde 's', muestro mensaje de continuar
    if respuesta == "s":
        print("Continuando...")

    # Si la respuesta no es ni 's' ni 'n', muestro mensaje de error
    else:
        print("Respuesta no válida. Introduce 's' o 'n'.")
