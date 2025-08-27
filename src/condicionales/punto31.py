# punto31.py

# Definimos el dividendo
dividendo = 10
# Definimos el divisor
divisor = 0

# Verificamos que el divisor no sea cero y que el resultado sea mayor que 1
if divisor != 0 and dividendo / divisor > 1:
    print("El resultado de la división es mayor que 1.")
else:
    # Si el divisor es cero, mostramos mensaje de error
    print("No es posible dividir entre cero.")