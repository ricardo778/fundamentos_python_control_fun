# Definición de la función crear_usuario
# Recibe nombre, apellido, edad, email y un parámetro opcional 'activo' que por defecto es True.
# Devuelve un diccionario con los datos del usuario creados a partir de los parámetros.
def crear_usuario(nombre, apellido, edad, email, activo=True):
    return {
        "nombre_completo": f"{nombre} {apellido}",
        "edad": edad,
        "email": email,
        "activo": activo
    }

# Se pasa cada argumento por nombre, lo que hace más fácil la lectura del código.
usuario = crear_usuario(
    nombre="Juan",
    apellido="Pérez",
    edad=28,
    email="juan@ejemplo.com",
    activo=False
)
