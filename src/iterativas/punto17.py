# Función para calcular el factorial de un número
def calcular_factorial(n):
    resultado = 1  # Inicializo la variable resultado en 1
    # Mientras n sea mayor que 0, multiplico resultado por n y reduzco n
    while n > 0:
        resultado *= n  # Multiplico el resultado acumulado por el número actual
        n -= 1  # Disminuyo n en 1 en cada vuelta
    return resultado  # Devuelvo el valor final del factorial

# Número del cual se quiere calcular el factorial
numero = 5

# Muestro el resultado llamando a la función calcular_factorial
print(f"El factorial de {numero} es {calcular_factorial(numero)}")  # 120
