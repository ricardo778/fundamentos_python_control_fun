# Recorro los grupos del 1 al 3
for i in range(1, 4):
    print(f"Grupo {i}:")  # Muestro el número de grupo

    # Recorro los elementos del grupo del 1 al 5
    for j in range(1, 6):
        if j == 3:  # Si el elemento es 3
            print("  Saltando el elemento 3")  # Aviso que se omite
            continue  # Solo afecta al bucle interno

        # Muestro el elemento actual
        print(f"  Elemento {j}")

    # Indico que finalizó el grupo
    print("Fin del grupo\n")
