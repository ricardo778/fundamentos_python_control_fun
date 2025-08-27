def dividir_seguro(a, b):
    # Aquí miramos si el número para dividir (b) es cero.
    if b == 0:
        # Si es cero, le decimos a la persona que no se puede dividir por cero.
        print("Error: División por cero")
        # Y no devolvemos nada, porque no hay resultado.
        return None

    # Si no es cero, hacemos la división y guardamos el resultado.
    resultado = a / b
    # Y devolvemos ese resultado.
    return resultado

# Aquí probamos la función con 10 y 2.
print(dividir_seguro(10, 2))

# Y aquí probamos con 10 y 0 para ver el mensaje de error.
print(dividir_seguro(10, 0))
