# Recorro los números del 1 al 10 usando un bucle for
for numero in range(1, 11):
    if numero == 5:  # Si el número actual es 5
        print("¡Encontrado el 5! Saliendo del bucle...")  # Mensaje indicando que se encontró el 5
        break  # Salgo inmediatamente del bucle
    print(f"Número actual: {numero}")  # Muestro el número actual si no es 5

# Mensaje al finalizar el bucle
print("Bucle terminado")
