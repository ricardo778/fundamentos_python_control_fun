# Función para imprimir un triángulo de asteriscos
def imprimir_triangulo(altura):
    fila = 1  # Inicializo el contador de filas en 1
    while fila <= altura:  # Mientras la fila sea menor o igual a la altura deseada
        print("*" * fila)  # Imprimo tantos asteriscos como el número de la fila actual
        fila += 1  # Incremento el contador para la siguiente fila

# Llamo a la función para imprimir un triángulo de altura 5
imprimir_triangulo(5)
