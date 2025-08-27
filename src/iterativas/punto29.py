# Lista de datos que contiene valores numéricos y no numéricos
datos = ["25", "error", "42", "texto", "17"]

suma = 0  # Inicializo la variable suma en 0

# Recorro cada valor en la lista
for valor in datos:
    if not valor.isdigit():  # Si el valor no es un número
        print(f"Valor no numérico ignorado: '{valor}'")  # Aviso que se ignora
        continue  # Paso al siguiente valor sin sumar

    # Sumo el valor convertido a entero a la variable suma
    suma += int(valor)

# Muestro la suma de los valores válidos
print(f"La suma de los valores válidos es: {suma}")
