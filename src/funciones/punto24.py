def calcular_promedio(numeros):
    # Esta es una función que calcula el promedio de una lista de números.
    # Recibe como argumento una lista llamada 'numeros'.

    # Para hacer el cálculo, primero suma todos los números de la lista
    # usando la función 'sum()'.
    # Luego, divide esa suma por la cantidad de números en la lista,
    # que se obtiene con la función 'len()'.
    
    # La función devuelve el resultado de esa operación.
    return sum(numeros) / len(numeros)

# Ejemplo de uso
notas = [7, 8, 6, 9]

# Guardamos el resultado de la función en una variable llamada 'promedio'.
promedio = calcular_promedio(notas)

# Imprimimos el resultado para que se vea en pantalla.
print(f"El promedio es: {promedio}")
