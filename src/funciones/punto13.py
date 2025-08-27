# Definimos una función llamada saludar que recibe un parámetro 'nombre'
def saludar(nombre):
    # Imprime un saludo usando el nombre recibido como argumento
    print(f"Hola, {nombre}")
    # No hay 'return', por lo tanto la función devuelve None automáticamente


# Llamamos a la función 'saludar' pasando el nombre "Laura"
resultado = saludar("Laura")

# Mostramos en pantalla lo que devolvió la función
# Como la función no tiene 'return', imprimirá: None
print(f"La función devolvió: {resultado}")  # Imprime: La función devolvió: None
