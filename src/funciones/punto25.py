# Esta función revisa si un texto parece un correo electrónico válido.
def validar_email(email):
    # Primero, miramos si lo que nos dieron es un texto. Si no, genera un error.
    if not isinstance(email, str):
        raise TypeError("El email debe ser una cadena de texto")
    
    # Aquí revisamos si tiene un "@" y si el último pedazo (después del "@") tiene un punto.
    # Por ejemplo, para "ejemplo@mail.com", revisa si "mail.com" tiene un punto.
    return "@" in email and "." in email.split("@")[-1]
