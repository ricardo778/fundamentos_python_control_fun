# Variable para indicar si se encontró el valor que cumple la condición
encontrado = False

# Bucle externo recorriendo valores de i del 0 al 4
for i in range(5):
    # Bucle interno recorriendo valores de j del 0 al 4
    for j in range(5):
        if i * j > 10:  # Si el producto i * j es mayor que 10
            print(f"Valor encontrado: {i} * {j} = {i*j}")  # Muestro el resultado
            encontrado = True  # Marcamos que se encontró
            break  # Salimos del bucle interno

    if encontrado:  # Si ya se encontró, salimos del bucle externo también
        break
