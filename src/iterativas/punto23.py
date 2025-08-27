# Función para buscar un elemento en una lista y devolver su posición
def buscar_elemento(lista, objetivo):
    # Recorro la lista con índice y elemento usando enumerate
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:  # Si el elemento coincide con el objetivo
            return indice  # Devuelvo la posición donde se encontró

    return -1  # Si llegamos aquí, el elemento no está en la lista

# Lista de números a buscar
numeros = [4, 7, 2, 9, 1, 5]

# Busco el número 9 en la lista y guardo la posición
posicion = buscar_elemento(numeros, 9)

# Muestro la posición del elemento encontrado
print(f"El elemento se encuentra en la posición: {posicion}")
