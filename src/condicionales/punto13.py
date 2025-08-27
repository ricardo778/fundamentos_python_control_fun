# punto13.py

# Definimos un punto como una tupla (x, y)
punto = (0, 0)

# Se evalúa la posición del punto usando la sentencia match
match punto:
    case (0, 0):  # Si x=0 e y=0
        print("El punto está en el origen.")
    case (0, y):  # Si x=0 y y cualquier valor
        print(f"El punto está en el eje Y en y={y}.")
    case (x, 0):  # Si y=0 y x cualquier valor
        print(f"El punto está en el eje X en x={x}.")
    case (x, y):  # Cualquier otra coordenada
        print(f"El punto está en coordenadas x={x}, y={y}.")