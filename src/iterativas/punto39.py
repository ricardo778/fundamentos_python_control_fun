# Función para buscar un usuario por nombre en una lista de usuarios
def buscar_usuario(usuarios, nombre):
    # Recorremos cada usuario en la lista
    for usuario in usuarios:
        # Comprobamos si el nombre coincide con el usuario actual
        if usuario["nombre"] == nombre:
            print(f"Usuario encontrado: {usuario}")  # Mostramos el usuario encontrado
            return usuario  # Retornamos el usuario encontrado
    else:
        # Se ejecuta si no se encuentra el usuario en la lista
        print(f"Usuario '{nombre}' no encontrado, creando nuevo perfil...")
        # Creamos un nuevo usuario con nivel inicial 1
        nuevo_usuario = {"nombre": nombre, "nivel": 1}
        # Agregamos el nuevo usuario a la lista
        usuarios.append(nuevo_usuario)
        return nuevo_usuario  # Retornamos el nuevo usuario

# Lista de usuarios existente
base_usuarios = [
    {"nombre": "Ana", "nivel": 5},
    {"nombre": "Carlos", "nivel": 3}
]

# Buscamos un usuario existente
buscar_usuario(base_usuarios, "Ana")
# Buscamos un usuario que no existe, se crea uno nuevo
buscar_usuario(base_usuarios, "Roberto")
