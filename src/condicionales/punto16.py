# Lista de números
numeros = [1, 2, 3, 4]

# Revisamos cómo está formada la lista usando match
match numeros:
    case []:  # Si la lista está vacía
        print("La lista está vacía.")
    case [uno]:  # Si tiene solo un elemento
        print(f"Un solo elemento: {uno}.")
    case [uno, dos]:  # Si tiene dos elementos
        print(f"Dos elementos: {uno} y {dos}.")
    case [uno, *resto]:  # Si tiene más de dos elementos
        print(f"Primer elemento: {uno}, resto de la lista: {resto}.")
