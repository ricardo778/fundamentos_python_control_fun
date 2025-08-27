# Lista de números, algunos de ellos son cero
numeros = [1, 2, 0, 4, 0, 6, 7]

# Recorro cada número en la lista
for num in numeros:
    if num == 0:  # Si el número es cero
        print("Omitiendo división por cero")  # Mensaje de advertencia
        continue  # Saltamos a la siguiente iteración para evitar división por cero

    # Realizo la división 10 / num
    resultado = 10 / num
    # Imprimo el resultado de la división
    print(f"10 / {num} = {resultado}")
