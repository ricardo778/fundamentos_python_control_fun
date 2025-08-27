def es_mayor_de_edad(edad):
    # Esta función revisa si una edad es 18 o más.
    # Devuelve True si es verdad, y False si no.
    return edad >= 18

def es_correo_valido(email):
    # Esta función revisa si el texto de un correo tiene un '@' y un '.'
    # Esto es una manera simple de verificar si es un correo válido.
    return "@" in email and "." in email

# Aquí ponemos una edad en una variable para probar.
usuario_edad = 16
# Usamos la función para saber si el usuario es mayor de edad.
if es_mayor_de_edad(usuario_edad):
    # Si la función devolvió True, se imprime esto.
    print("Acceso permitido")
else:
    # Si la función devolvió False, se imprime esto.
    print("Acceso denegado")  # En este caso, se imprime "Acceso denegado"
