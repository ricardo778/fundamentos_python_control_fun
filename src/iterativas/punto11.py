# Lista que guarda las temperaturas de cada día de la semana
temperaturas = [22, 19, 24, 25, 21, 23, 20]

# Lista con los nombres de los días de la semana
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Saco la temperatura más alta de la lista
max_temp = max(temperaturas)

# Busco en qué posición está esa temperatura en la lista
indice_max = temperaturas.index(max_temp)

# Muestro el día más caliente y su temperatura
print(f"El día más caluroso fue {dias[indice_max]} con {max_temp}°C")

# Calculo el promedio sumando todas las temperaturas y dividiéndolas por la cantidad de días
promedio = sum(temperaturas) / len(temperaturas)

# Muestro el promedio con un decimal
print(f"Temperatura promedio: {promedio:.1f}°C")

# Recorro cada día para ver si la temperatura de ese día está por encima del promedio
for i in range(len(dias)):
    if temperaturas[i] > promedio:
        # Si la temperatura de ese día es mayor al promedio, lo muestro en pantalla
        print(f"{dias[i]}: {temperaturas[i]}°C (por encima del promedio)")