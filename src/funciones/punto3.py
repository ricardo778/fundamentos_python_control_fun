# Asignar una función a una variable
convertir = celsius_a_fahrenheit   # Guardamos la función celsius_a_fahrenheit en la variable "convertir"

# Usar la variable como si fuera la función original
temperatura_f = convertir(25)  # Llamamos a "convertir" con el valor 25°C, equivale a usar celsius_a_fahrenheit(25)

# Mostrar el resultado en pantalla
print(f"25°C equivalen a {temperatura_f}°F")  # Imprime: 25°C equivalen a 77.0°F
