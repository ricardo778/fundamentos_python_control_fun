# Creo una lista que guarda los cuadrados de los números del 1 al 5
cuadrados = [x**2 for x in range(1, 6)]

# Muestro en pantalla la lista de cuadrados
print(cuadrados)  # [1, 4, 9, 16, 25]

# Ahora creo una lista que solo guarda los números pares del 0 al 9
pares = [x for x in range(10) if x % 2 == 0]

# Muestro en pantalla la lista de pares
print(pares)  # [0, 2, 4, 6, 8]
