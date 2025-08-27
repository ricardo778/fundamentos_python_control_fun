# Función para calcular la raíz cuadrada de un número usando el método de aproximaciones
def calcular_raiz_cuadrada(numero, precision=0.0001):
    aproximacion = numero / 2  # Inicializo la aproximación con la mitad del número
    # Mientras la diferencia entre el cuadrado de la aproximación y el número sea mayor que la precisión
    while abs(aproximacion**2 - numero) > precision:
        # Actualizo la aproximación usando la fórmula de Newton-Raphson
        aproximacion = (aproximacion + numero / aproximacion) / 2
    return aproximacion  # Devuelvo la aproximación final

# Muestro la raíz cuadrada de 25 con 6 decimales
print(f"Raíz cuadrada de 25: {calcular_raiz_cuadrada(25):.6f}")  # 5.000000

# Muestro la raíz cuadrada de 7 con 6 decimales
print(f"Raíz cuadrada de 7: {calcular_raiz_cuadrada(7):.6f}")    # 2.645751
