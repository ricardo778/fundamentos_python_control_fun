def dividir_seguro(a, b):
    # Esta función divide un número por otro, pero se asegura de que no dividas por cero.
    # Si el segundo número (b) es cero, la función no hace la división.
    if b == 0:
        # Si b es cero, devuelve 'None' para decir que no hay resultado.
        return None
    # Si b no es cero, la función hace la división y devuelve el resultado.
    return a / b
