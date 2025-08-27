# Recorremos los números del 1 al 9
for numero in range(1, 10):
    if numero % 2 == 0:  # Si el número es par
        pass  # No hacemos nada con los números pares
    else:  # Si el número es impar
        print(f"Procesando número impar: {numero}")  # Mostramos el número impar
