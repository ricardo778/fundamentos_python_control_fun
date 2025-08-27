# Función para validar la contraseña según requisitos: 
# mínimo 8 caracteres, al menos una mayúscula, una minúscula y un número
def validar_contraseña(contraseña):
    if len(contraseña) < 8:  # Si la longitud es menor a 8
        return False

    # Inicializamos variables para verificar cada requisito
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False

    # Recorremos cada caracter de la contraseña
    for caracter in contraseña:
        if caracter.isupper():  # Si es mayúscula
            tiene_mayuscula = True
            continue  # Ya verificamos este requisito

        if caracter.islower():  # Si es minúscula
            tiene_minuscula = True
            continue

        if caracter.isdigit():  # Si es un número
            tiene_numero = True

    # Retornamos True si cumple todos los requisitos, False si no
    return tiene_mayuscula and tiene_minuscula and tiene_numero

# Lista de contraseñas de prueba
contraseñas = ["abc123", "Password", "Password1", "pass123", "PASS123"]

# Evaluamos cada contraseña usando la función
for pwd in contraseñas:
    if validar_contraseña(pwd):
        print(f"'{pwd}' es válida")
    else:
        print(f"'{pwd}' NO es válida")
