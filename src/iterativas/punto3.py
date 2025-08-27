# Lista con varios nombres
nombres = ["Ana", "Carlos", "Elena"]    # Creo una lista llamada 'nombres' que guarda 3 cadenas

# Uso de un ciclo for con range y len
for i in range(len(nombres)):           
    # Recorro la lista usando índices desde 0 hasta len(nombres)-1
    print(f"Posición {i}: {nombres[i]}")
    # Imprimo la posición actual y el nombre que está en esa posición
