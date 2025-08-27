def formato_nombre(nombre, apellido):
    # Esta función recibe un nombre y un apellido.
    # Devuelve el apellido en mayúsculas, una coma, un espacio, y el nombre con la primera letra en mayúscula.
    return f"{apellido.upper()}, {nombre.capitalize()}"

# Aquí usamos la función con los nombres "ana" y "garcía" para ver el resultado.
print(formato_nombre("ana", "garcía"))
