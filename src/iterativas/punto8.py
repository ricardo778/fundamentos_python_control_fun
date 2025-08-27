# Crear una matriz de multiplicación 3x3
for i in range(1, 4):  # Bucle externo: recorre los números de la fila (del 1 al 3)
    for j in range(1, 4):  # Bucle interno: recorre los números de la columna (del 1 al 3)
        # Mostrar el producto en formato "i × j = resultado"
        # end="\t" mantiene los resultados en la misma línea separados por tabulación
        print(f"{i} × {j} = {i*j}", end="\t")
    print()  # Salto de línea después de cada fila para dar forma a la tabla
