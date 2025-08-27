# Se define la edad de la persona
edad = 20

# Se evalúa la categoría de edad usando match con guardas (if)
match edad:
    case edad if edad < 18:  # Menores de 18 años
        print("Eres menor de edad.")
    case edad if edad >= 18 and edad < 65:  # Entre 18 y 64 años
        print("Eres adulto.")
    case edad if edad >= 65:  # 65 años o más
        print("Eres adulto mayor.")