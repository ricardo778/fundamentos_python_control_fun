def calcular_descuento(precio, porcentaje=10):
    # Define una función que calcula el precio con descuento
    # Recibe el precio original y un porcentaje de descuento (por defecto es 10%)
    
    descuento = precio * (porcentaje / 100)  
    # Calcula el valor del descuento aplicando el porcentaje al precio
    
    precio_final = precio - descuento  
    # Resta el descuento al precio original para obtener el precio final
    
    return precio_final  
    # Devuelve el precio final con el descuento aplicado


precio_con_descuento = calcular_descuento(100)  
# Llama a la función con un precio de 100 y usa el descuento por defecto (10%)

print(f"Precio con descuento: {precio_con_descuento}")  
# Muestra en pantalla el resultado: "Precio con descuento: 90.0"

# print(descuento)  
# Si se descomenta, da error porque 'descuento' solo existe dentro de la función
