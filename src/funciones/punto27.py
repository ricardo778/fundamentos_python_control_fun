def filtrar_pares(lista):
    # Esta función recibe una lista de números.
    # Revisa cada número y si es par (si su residuo al dividir por 2 es 0), lo mete en una nueva lista.
    return [num for num in lista if num % 2 == 0]

# Aquí creamos una lista para probar la función.
numeros_ejemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Llamamos a la función con la lista de ejemplo.
pares = filtrar_pares(numeros_ejemplo)

# Imprimimos la nueva lista que solo tiene los números pares.
print(pares)  # Imprime: [2, 4, 6, 8, 10]
