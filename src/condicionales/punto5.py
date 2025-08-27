# Pedimos al usuario que escriba una contraseña
contrasena = input("Introduce la contraseña: ")

# Verificamos si la contraseña ingresada es igual a la correcta
if contrasena == "secreta123":
    # Si coincide, se concede el acceso
    print("Acceso concedido.")
else:
    # Si no coincide, se niega el acceso
    print("Contraseña incorrecta. Acceso denegado.")
