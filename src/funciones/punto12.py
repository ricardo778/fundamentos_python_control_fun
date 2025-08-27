# Definición de la función llamada calcular_cuadrado que recibe un parámetro llamado numero
def calcular_cuadrado(numero):
    # Calcula el cuadrado del número recibido y lo guarda en la variable resultado
    resultado = numero * numero
    # Devuelve el valor calculado y termina la función
    return resultado  

# Llamada a la función calcular_cuadrado pasando el valor 4 como argumento, y guarda el resultado en la variable area
area = calcular_cuadrado(4)

# Imprime en pantalla el valor guardado en area (que será 16)
print(area)  # Imprime: 16
