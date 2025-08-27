# Defino una función llamada es_primo que recibe un número
def es_primo(num):
    # Si el número es menor que 2, no es primo
    if num < 2:
        return False
    # Recorro desde 2 hasta la raíz cuadrada del número para verificar divisores
    for i in range(2, int(num**0.5) + 1):
        # Si el número es divisible entre i, no es primo
        if num % i == 0:
            return False
    # Si no encontró divisores, entonces sí es primo
    return True

# Creo una lista vacía para guardar los números primos
primos = []
# Recorro los números del 2 al 19
for num in range(2, 20):
    # Verifico si el número es primo llamando a la función
    if es_primo(num):
        # Si es primo, lo agrego a la lista
        primos.append(num)

# Muestro en pantalla los números primos encontrados
print(f"Números primos entre 2 y 19: {primos}")  # [2, 3, 5, 7, 11, 13, 17, 19]
