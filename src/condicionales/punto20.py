# Definimos la edad y si tiene permiso de los padres
edad = 17
permiso_parental = True

# Revisamos si cumple las condiciones para obtener la licencia
if (edad >= 18) or (edad >= 16 and permiso_parental):
    print("Puedes obtener la licencia de conducir.")
else:
    print("No cumples los requisitos para la licencia.")
