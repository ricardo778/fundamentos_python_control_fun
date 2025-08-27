# Esta función crea una lista con solo los números positivos de otra lista.
# Esto es un buen hábito para evitar errores inesperados.
def filtrar_positivos(numeros):
    # Primero, revisamos si lo que nos dieron es una lista.
    if not isinstance(numeros, list):
        # Si no es una lista, devolvemos una lista vacía para no romper el programa.
        return []

    # Si es una lista, hacemos una nueva lista solo con los números mayores que cero.
    return [num for num in numeros if num > 0]
