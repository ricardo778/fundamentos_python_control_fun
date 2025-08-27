# Recorro los números del 1 al 10 usando un bucle for
for numero in range(1, 11):
    if numero % 2 == 0:  # Si el número es par
        continue  # Saltamos a la siguiente iteración sin ejecutar el print

    # Si el número no es par (es impar), lo mostramos
    print(f"Número impar: {numero}")
