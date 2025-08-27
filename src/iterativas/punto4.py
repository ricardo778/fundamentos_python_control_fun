# Lista con varios nombres
nombres = ["Ana", "Carlos", "Elena"]             
# Creo una lista llamada 'nombres' que contiene 3 cadenas

# Uso del ciclo for con enumerate
for indice, nombre in enumerate(nombres):        
    # Recorro la lista con enumerate, que devuelve índice y valor
    print(f"Posición {indice}: {nombre}")        
    # Imprimo la posición y el nombre correspondiente