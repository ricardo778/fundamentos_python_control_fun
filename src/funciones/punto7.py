def saludar(nombre, mensaje="¡Bienvenido!"):  
    # La función 'saludar' tiene dos parámetros:
    # - 'nombre': obligatorio, representa el nombre de la persona a saludar.
    # - 'mensaje': opcional, si no se proporciona usa el valor por defecto "¡Bienvenido!".
    print(f"Hola {nombre}. {mensaje}")

# Ejemplo 1: solo se pasa el nombre, se usa el mensaje por defecto.
saludar("Carlos")  
# Imprime: Hola Carlos. ¡Bienvenido!

# Ejemplo 2: se pasa un nombre y un mensaje personalizado.
saludar("María", "¿Cómo estás hoy?")  
# Imprime: Hola María. ¿Cómo estás hoy?
