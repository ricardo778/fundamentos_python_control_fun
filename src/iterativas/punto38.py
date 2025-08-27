# Función para validar una lista de edades
def validar_edades(lista_edades):
    # Recorremos cada edad en la lista
    for edad in lista_edades:
        # Verificamos si la edad es un número entero y no negativa
        if not isinstance(edad, int) or edad < 0:
            print(f"Edad inválida encontrada: {edad}")  # Mostramos la edad inválida
            break  # Salimos del bucle al encontrar un valor inválido
    else:
        # Si el bucle termina sin encontrar errores
        print("Todas las edades son válidas")
        return True  # Retornamos True si todas son válidas

    return False  # Retornamos False si se encontró una edad inválida

# Probamos la función con listas de edades
validar_edades([25, 17, 30, 42])  # Todas válidas
validar_edades([25, -3, 30, 42])  # Una inválida
