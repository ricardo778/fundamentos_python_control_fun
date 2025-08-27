# Definimos una función llamada calcular_area_rectangulo que recibe dos parámetros: base y altura
def calcular_area_rectangulo(base, altura):
    # Calculamos el área multiplicando la base por la altura
    area = base * altura
    # Retornamos el valor del área calculada
    return area

# Llamamos a la función calcular_area_rectangulo enviando los valores 5 y 3 como argumentos
resultado = calcular_area_rectangulo(5, 3)

# Imprimimos en pantalla el resultado con un mensaje formateado
print(f"El área del rectángulo es: {resultado}")  # Esto mostrará: El área del rectángulo es: 15
