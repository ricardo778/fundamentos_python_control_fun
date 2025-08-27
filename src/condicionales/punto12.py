# Se pide al usuario que ingrese el nombre de una fruta
fruta = input("Introduzca una fruta: ")

# Se evalúa el valor de 'fruta' usando la sentencia match
match fruta:
    case "manzana":  # Si la fruta es "manzana"
        print("La fruta es una manzana.")
    case "naranja":  # Si la fruta es "naranja"
        print("La fruta es una naranja.")
    case "plátano":  # Si la fruta es "plátano"
        print("La fruta es un plátano.")
    case _:  # Caso por defecto (si no coincide con ninguno anterior)
        print("Fruta desconocida.")