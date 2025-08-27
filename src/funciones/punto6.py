def calcular_precio_final(precio_base, impuesto):
    # Esta función recibe un precio base y un impuesto,
    # y retorna el precio final aplicando el impuesto.
    return precio_base + (precio_base * impuesto)

# Llamada a la función con argumentos:
# precio_base = 100
# impuesto = 0.21 (equivalente al 21%)
total = calcular_precio_final(100, 0.21)

# Muestra el resultado del cálculo
print(f"Precio final: {total}")  # Imprime: Precio final: 121.0
