# Lista de números donde vamos a buscar un número primo
numeros = [4, 6, 8, 9, 10, 12]

# Recorremos cada número en la lista
for num in numeros:
    # Condición simple para detectar primos (mayormente impar y no divisible por 3)
    if num % 2 != 0 and num % 3 != 0:
        print(f"¡Encontrado un primo: {num}!")  # Mostramos el primo encontrado
        break  # Salimos del bucle al encontrar un primo
else:
    # Se ejecuta si el bucle termina sin encontrar un primo
    print("No se encontró ningún número primo en la lista")
