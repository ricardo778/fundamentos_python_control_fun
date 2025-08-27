# Bucle infinito que se repetirá hasta que el usuario escriba 'salir'
while True:
    # Solicito al usuario que escriba algo
    entrada = input("Escribe algo (o 'salir' para terminar): ")

    # Verifico si el usuario quiere terminar el programa
    if entrada.lower() == 'salir':  # Convierto a minúsculas para no depender de mayúsculas
        print("Programa terminado.")  # Mensaje de fin
        break  # Salgo del bucle

    # Si no es 'salir', muestro lo que escribió el usuario
    print(f"Has escrito: {entrada}")
