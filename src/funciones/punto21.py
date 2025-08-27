# Esta función calcula el promedio de una lista de números.
# Lo bueno de esta función es que solo se encarga de hacer la cuenta.
def calcular_promedio(numeros):
    # Sumamos todos los números y los dividimos por cuántos hay.
    return sum(numeros) / len(numeros)

# Aquí tenemos una lista de notas para probar.
notas = [7, 8, 6, 9]
# Llamamos a la función y guardamos el resultado en la variable 'promedio'.
promedio = calcular_promedio(notas)
# Ahora, fuera de la función, mostramos el resultado con un texto bonito.
print(f"El promedio es: {promedio}")  # Imprime: El promedio es: 7.5
