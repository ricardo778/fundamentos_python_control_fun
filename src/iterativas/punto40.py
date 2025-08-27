# Función para analizar una lista de valores y compararlos con un umbral
def analizar_datos(valores, umbral):
    tiene_advertencias = False  # Bandera para saber si hay valores que exceden el umbral

    # Recorremos cada valor en la lista
    for valor in valores:
        if valor > umbral:  # Si el valor excede el umbral
            tiene_advertencias = True  # Activamos la bandera
            print(f"Advertencia: valor {valor} excede el umbral {umbral}")  # Mostramos advertencia
        else:
            pass  # No hacemos nada con valores dentro del rango
    else:
        # Si no se encontraron valores que excedan el umbral
        if not tiene_advertencias:
            print("Análisis completo: todos los valores están dentro del rango normal")
            return "OK"  # Retornamos OK si todos están dentro del umbral

    return "ADVERTENCIA"  # Retornamos ADVERTENCIA si al menos un valor excede el umbral

# Probamos la función con conjuntos de datos diferentes
analizar_datos([10, 15, 20, 25], 30)  # Todos dentro del umbral
analizar_datos([10, 35, 20, 25], 30)  # Uno excede el umbral
