# Función para obtener un número dentro de un rango específico
def obtener_numero_en_rango(mensaje, minimo, maximo):
    while True:  # Bucle infinito hasta que el usuario ingrese un valor válido
        try:
            valor = int(input(mensaje))  # Intento convertir la entrada a entero
            if minimo <= valor <= maximo:  # Verifico si está dentro del rango
                return valor  # Devuelvo el valor si es válido
            print(f"Error: El número debe estar entre {minimo} y {maximo}.")  # Mensaje si no está en el rango
        except ValueError:  # Capturo el error si no es un número entero
            print("Error: Debes introducir un número entero.")  # Mensaje de error

# Solicito al usuario que ingrese su edad, validando que esté entre 0 y 120
edad = obtener_numero_en_rango("Introduce tu edad (0-120): ", 0, 120)

# Muestro la edad registrada
print(f"Edad registrada: {edad} años")
