# Esta función revisa si una persona es mayor de edad.
# Le damos un número (la edad) y nos dice si es 18 o más.
def es_mayor_de_edad(edad):
    # Devuelve True si la edad es 18 o más, y False si es menos.
    return edad >= 18

# Ejemplo de uso
edad_persona = 20

# Guardamos el resultado de la función en una variable llamada 'es_adulto'.
es_adulto = es_mayor_de_edad(edad_persona)

# Imprimimos el resultado.
print(f"¿La persona es mayor de edad? {es_adulto}")
