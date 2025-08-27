# Definimos la nota obtenida por el estudiante
nota = 87

# Evaluamos la nota con estructuras condicionales
if nota >= 90:
    # Si la nota es 90 o más, el estudiante tiene calificación sobresaliente
    print("Calificación: Sobresaliente")
elif nota >= 80:
    # Si la nota está entre 80 y 89, se califica como notable
    print("Calificación: Notable")
elif nota >= 70:
    # Si la nota está entre 70 y 79, el resultado es aprobado
    print("Calificación: Aprobado")
else:
    # Si la nota es menor a 70, se considera suspenso
    print("Calificación: Suspenso")