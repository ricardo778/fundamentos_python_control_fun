# Lista de temperaturas, algunas positivas y otras negativas
temperaturas = [22, -5, 28, 31, -15, 19, 26, -8]

# Mensaje inicial para indicar que se mostrarán solo las positivas
print("Temperaturas positivas:")

# Recorro cada temperatura en la lista
for temp in temperaturas:
    if temp <= 0:  # Si la temperatura es cero o negativa
        continue  # Saltamos a la siguiente iteración sin imprimir

    # Imprimo la temperatura positiva
    print(f"{temp}°C")
