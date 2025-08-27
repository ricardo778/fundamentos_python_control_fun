#Definir una función que acepte un número variable de argumentos y devuelva la suma de todos ellos.
def sumar(*numeros):
    total = 0
    # Iteramos sobre los números y los sumamos
    for numero in numeros:
        # Acumulamos la suma
        total += numero
    return total
# retornamos el total de la suma

# Podemos pasar cualquier cantidad de argumentos
print(sumar(1, 2))          # Imprime: 3
print(sumar(1, 2, 3, 4, 5)) # Imprime: 15
print(sumar())              # Imprime: 0
