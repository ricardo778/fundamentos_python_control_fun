# Lista de usuarios con su nombre y rol
usuarios = [
    {"nombre": "Ana", "rol": "admin"},
    {"nombre": "Luis", "rol": "usuario"},
    {"nombre": "Marta", "rol": "moderador"}
]

# Se recorre cada usuario y se evalúa su rol usando match
for usuario in usuarios:
    match usuario:
        case {"rol": "admin"}:  # Si el rol es admin
            print(f"{usuario['nombre']} tiene permisos de administrador.")
        case {"rol": "moderador"}:  # Si el rol es moderador
            print(f"{usuario['nombre']} puede moderar contenidos.")
        case {"rol": "usuario"}:  # Si el rol es usuario regular
            print(f"{usuario['nombre']} es un usuario regular.")
        case _:  # Caso por defecto si el rol no coincide
            print(f"Rol de {usuario['nombre']} desconocido.")
