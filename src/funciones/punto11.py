# Definición de la función mostrar_informacion que recibe parámetros variables con nombre
def mostrar_informacion(**datos):
    # Recorremos el diccionario 'datos' que contiene clave: valor de los argumentos
    for clave, valor in datos.items():
        # Imprimimos cada clave y su respectivo valor
        print(f"{clave}: {valor}")

# Llamada a la función pasando argumentos por nombre
# En este caso, se envía el nombre del lenguaje, su creador y el año de creación
mostrar_informacion(nombre="Python", creador="Guido van Rossum", año=1991)

# La salida en pantalla será:
# nombre: Python
# creador: Guido van Rossum
# año: 1991
