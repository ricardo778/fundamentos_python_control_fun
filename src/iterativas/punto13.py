# Empiezo con la variable entrada como un string vacío
entrada = ""

# El ciclo while se repite mientras lo que haya en "entrada" NO sea un número
# .isdigit() verifica si la cadena contiene solo dígitos (números positivos enteros)
while not entrada.isdigit():
    entrada = input("Introduce un número: ")  # Pido al usuario que escriba algo

# Cuando el ciclo termina significa que "entrada" sí es un número válido
print(f"Has introducido el número: {entrada}")