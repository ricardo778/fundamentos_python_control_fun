# Función para validar un formulario de datos
def validar_formulario(datos):
    campos_requeridos = ["nombre", "email", "edad"]  # Lista de campos que deben existir
    errores = []  # Lista para almacenar errores encontrados

    # Verificar que todos los campos requeridos existan y no estén vacíos
    for campo in campos_requeridos:
        if campo not in datos:  # Si falta un campo
            errores.append(f"Falta el campo requerido: {campo}")
            break  # Salimos del bucle
        elif not datos[campo]:  # Si el campo está vacío
            errores.append(f"El campo {campo} no puede estar vacío")
            break  # Salimos del bucle
    else:
        # Solo si todos los campos requeridos existen y no están vacíos
        # Validar el formato del email
        if "@" not in datos["email"]:
            errores.append("Email inválido")

        # Validar edad
        try:
            edad = int(datos["edad"])  # Convertimos a número
            if edad < 18 or edad > 120:  # Rango permitido
                errores.append("La edad debe estar entre 18 y 120")
        except ValueError:
            errores.append("La edad debe ser un número")  # No se pudo convertir

    # Validaciones opcionales: teléfono
    if "telefono" in datos:
        if not datos["telefono"].isdigit():  # Solo dígitos permitidos
            errores.append("El teléfono debe contener solo dígitos")
    else:
        pass  # Campo opcional, no hacemos nada

    # Devolver el resultado final según si hay errores o no
    if errores:
        return {"valido": False, "errores": errores}
    else:
        return {"valido": True}

# Probamos la función con formularios de ejemplo
formulario1 = {
    "nombre": "Ana García",
    "email": "ana@ejemplo.com",
    "edad": "28"
}

formulario2 = {
    "nombre": "Carlos López",
    "email": "carlosejemplo.com",  # Falta @
    "edad": "17"  # Menor de edad
}

# Mostramos resultados de la validación
print(validar_formulario(formulario1))
print(validar_formulario(formulario2))
