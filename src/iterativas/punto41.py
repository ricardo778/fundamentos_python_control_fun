# Función para encontrar la raíz cuadrada aproximada de un número
def encontrar_raiz(numero, max_iteraciones=10):
    aproximacion = numero / 2  # Valor inicial para la aproximación
    iteracion = 0  # Contador de iteraciones

    # Bucle mientras la aproximación no sea suficientemente precisa y no se exceda el máximo de iteraciones
    while abs(aproximacion**2 - numero) > 0.001 and iteracion < max_iteraciones:
        aproximacion = (aproximacion + numero / aproximacion) / 2  # Fórmula de Newton-Raphson
        iteracion += 1  # Incrementamos el contador
        print(f"Iteración {iteracion}: {aproximacion:.6f}")  # Mostramos la aproximación actual

    else:
        # Si el bucle terminó antes de alcanzar el límite de iteraciones
        if iteracion < max_iteraciones:
            print(f"Convergencia alcanzada en {iteracion} iteraciones")
            return aproximacion  # Retornamos la aproximación final

    # Si se alcanzó el máximo de iteraciones sin converger
    print("No se alcanzó convergencia en el número máximo de iteraciones")
    return aproximacion  # Retornamos la última aproximación

# Probamos la función con diferentes valores
encontrar_raiz(25)       # Debería converger rápidamente
encontrar_raiz(612, 5)   # Probablemente no converja en 5 iteraciones
