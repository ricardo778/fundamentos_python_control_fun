def convertir_a_celsius(fahrenheit):
    # Esta función cambia la temperatura de grados Fahrenheit a Celsius.
    
    # La fórmula es: (temperatura en Fahrenheit - 32) * 5/9.
    # La función hace la cuenta y devuelve el resultado.
    return (fahrenheit - 32) * 5/9

# Creamos una variable para la temperatura en Fahrenheit
temperatura_fahrenheit = 68

# Usamos la función para convertirla a Celsius
temperatura_celsius = convertir_a_celsius(temperatura_fahrenheit)

# Imprimimos el resultado para que se vea en pantalla.
print(f"68 grados Fahrenheit son {temperatura_celsius} grados Celsius")
