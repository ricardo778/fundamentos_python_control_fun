# Esta función crea una lista de números pares.
# Va desde el 2 hasta el número máximo que le digas, de dos en dos.
def crear_lista_pares(maximo):
    return [num for num in range(2, maximo + 1, 2)]

# Esta función crea un diccionario.
# Usa cada número de una lista como clave y su cuadrado como valor.
def crear_diccionario_cuadrados(numeros):
    return {num: num ** 2 for num in numeros}

# Aquí creamos una lista de números pares hasta el 10.
pares = crear_lista_pares(10)
# Y la imprimimos para ver el resultado: [2, 4, 6, 8, 10].
print(pares)

# Ahora creamos un diccionario de cuadrados con una lista de números.
cuadrados = crear_diccionario_cuadrados([1, 2, 3, 4])
# Y lo imprimimos para ver el resultado: {1: 1, 2: 4, 3: 9, 4: 16}.
print(cuadrados)
