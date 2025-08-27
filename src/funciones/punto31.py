def generar_contraseña(longitud=8):
    # Esta función crea una contraseña que es difícil de adivinar.
    # Si no le decimos cuántos caracteres queremos, usa 8 por defecto.
    
    # Aquí importamos las librerías necesarias para hacer el trabajo.
    import random
    import string
    
    # Juntamos letras (mayúsculas y minúsculas), números y signos.
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # De todos esos caracteres, elegimos uno al azar para cada espacio de la contraseña.
    # Luego los juntamos todos para formar la contraseña final.
    return ''.join(random.choice(caracteres) for _ in range(longitud))

# Ejemplo de uso
contraseña_nueva = generar_contraseña()

# Imprimimos la contraseña que se generó.
print(f"Tu nueva contraseña es: {contraseña_nueva}")
