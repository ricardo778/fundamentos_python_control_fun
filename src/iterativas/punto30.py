# Lista de números impares
numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
limite = 50  # Límite máximo de la suma
suma = 0     # Inicializo la suma en 0

# Recorro cada número en la lista
for num in numeros:
    # Ignoramos múltiplos de 3
    if num % 3 == 0:
        print(f"Omitiendo {num} (múltiplo de 3)")  # Mensaje indicando que se omite
        continue  # Paso al siguiente número sin sumar

    # Sumamos el número
    suma += num
    print(f"Añadiendo {num}: suma = {suma}")  # Mostramos la suma parcial

    # Si la suma supera el límite, terminamos el bucle
    if suma > limite:
        print(f"Límite de {limite} superado")  # Mensaje indicando que se superó el límite
        break  # Salimos del bucle
