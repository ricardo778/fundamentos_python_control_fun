# Definimos una función que calcula el precio con IVA.
# Si no le decimos el IVA, usa 0.21 por defecto (21%).
def calcular_precio_con_iva(precio_base, tasa_iva=0.21):
    # La función hace la cuenta: precio base por (1 más la tasa de IVA).
    # Por ejemplo, si el precio es 100, la cuenta es 100 * (1 + 0.21), que da 121.
    return precio_base * (1 + tasa_iva)

# Llamamos a la función solo con el precio base.
# Como no le damos el IVA, la función usa el 0.21 que tiene por defecto.
precio_final = calcular_precio_con_iva(100)
# Mostramos el resultado. El f"..." es para poner el valor de la variable en el texto.
print(f"Precio con IVA: {precio_final} €")  # Aquí se verá: Precio con IVA: 121.0 €
