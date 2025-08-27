# punto24.py

# Definimos la edad de la persona
edad = 16
# Definimos si tiene permiso de los padres
permiso_padres = True

# Verificamos si la persona tiene 18 años o más
if edad >= 18:
    # Si tiene 18 o más, puede obtener la licencia
    print('Puedes obtener la licencia de conducir.')
else:
    # Si tiene menos de 18, verificamos si tiene al menos 16
    if edad >= 16:
        # Si tiene 16 o más, verificamos el permiso de los padres
        if permiso_padres:
            print('Puedes obtener la licencia con permiso de tus padres.')
        else:
            print('Necesitas el permiso de tus padres para obtener la licencia.')
    else:
        # Si tiene menos de 16
        print('Eres demasiado joven para conducir.')
