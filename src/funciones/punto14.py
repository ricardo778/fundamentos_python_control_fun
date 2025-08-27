# Definición de la función estadisticas que recibe una lista de números
def estadisticas(numeros):
    # Calcula la suma total de los números
    total = sum(numeros)
    # Calcula el promedio dividiendo la suma entre la cantidad de elementos
    promedio = total / len(numeros)
    # Encuentra el valor mínimo de la lista
    minimo = min(numeros)
    # Encuentra el valor máximo de la lista
    maximo = max(numeros)
    # Retorna una tupla con todos los resultados (suma, promedio, mínimo, máximo)
    return total, promedio, minimo, maximo

# Lista de números que se usará como entrada para la función
datos = [4, 8, 15, 16, 23, 42]

# Se llama la función y se guardan los resultados en variables separadas
suma, media, menor, mayor = estadisticas(datos)

# Imprime la suma total de los elementos de la lista
print(f"Suma: {suma}")        # Imprime: Suma: 108
# Imprime el promedio de los elementos de la lista
print(f"Promedio: {media}")   # Imprime: Promedio: 18.0
# Imprime el número menor de la lista
print(f"Mínimo: {menor}")     # Imprime: Mínimo: 4
# Imprime el número mayor de la lista
print(f"Máximo: {mayor}")     # Imprime: Máximo: 42
