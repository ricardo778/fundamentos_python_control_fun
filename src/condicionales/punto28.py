# Definimos la edad de la persona
edad = 20

# Usamos expresiones condicionales anidadas para asignar la categoría
categoria = "Menor" if edad < 18 else ("Joven Adulto" if edad < 30 else "Adulto")

# Imprimimos la categoría
print(categoria)