# Definimos la edad de la persona
edad = 30
# Definimos el estado civil de la persona
estado_civil = 'soltero'

# Verificamos si la persona es mayor o igual a 18
if edad >= 18:
    # Si es mayor de edad, verificamos su estado civil
    if estado_civil == 'casado':
        # Si está casado
        print('Eres un adulto casado.')
    else:
        # Si no está casado
        print('Eres un adulto soltero.')
else:
    # Si es menor de 18
    print('Eres menor de edad.')
