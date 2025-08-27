# Definimos la edad de la persona
edad = 45

# Verificamos en qué rango de edad se encuentra
if edad < 18:
    # Si la edad es menor a 18, se considera menor de edad
    print("Eres menor de edad.")
elif 18 <= edad < 65:
    # Si la edad está entre 18 y 64, se considera adulto
    print("Eres adulto.")
else:
    # Si la edad es 65 o más, se considera mayor de 65 años
    print("Eres mayor de 65 años.")