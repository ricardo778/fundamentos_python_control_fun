# Variable que indica si estamos en modo debug o no
modo_debug = False

# Recorremos 100 iteraciones
for i in range(100):
    # Si no estamos en modo debug, no hacemos nada durante el procesamiento
    if not modo_debug:
        pass
    else:  # Si estamos en modo debug, mostramos la iteración actual
        print(f"Procesando iteración {i}")

    # Aquí iría el código de procesamiento real
