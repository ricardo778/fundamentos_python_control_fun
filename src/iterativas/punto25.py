# Función para determinar si un número es primo
def es_primo(n):
    if n < 2:  # Los números menores que 2 no son primos
        return False

    # Recorro los números desde 2 hasta la raíz cuadrada de n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # Si n es divisible entre i
            return False  # No es primo, salimos inmediatamente

    return True  # Si no se encontró ningún divisor, n es primo
