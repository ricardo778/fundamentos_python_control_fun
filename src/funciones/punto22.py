# Esta función recibe un número y dice qué calificación es.
def obtener_calificacion(puntuacion):
    # Primero revisamos si el número está entre 0 y 100.
    if puntuacion < 0 or puntuacion > 100:
        # Si no lo está, devolvemos un mensaje de error.
        return "Puntuación inválida"

    # Si el número es 90 o más, la calificación es "Sobresaliente".
    if puntuacion >= 90:
        return "Sobresaliente"
    # Si es 70 o más (pero menos de 90), es "Notable".
    if puntuacion >= 70:
        return "Notable"
    # Si es 60 o más (pero menos de 70), es "Bien".
    if puntuacion >= 60:
        return "Bien"
    # Si es 50 o más (pero menos de 60), es "Suficiente".
    if puntuacion >= 50:
        return "Suficiente"

    # Y si no es ninguna de las anteriores, es "Insuficiente".
    return "Insuficiente"
