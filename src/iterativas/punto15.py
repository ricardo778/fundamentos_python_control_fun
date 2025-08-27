saldo = 1000   # Inicializo el saldo en 1000 euros
while saldo > 0:   # Mientras el saldo sea mayor que 0
    print(f"Saldo actual: {saldo}€")   # Muestro el saldo disponible
    gasto = float(input("Introduce la cantidad a gastar (0 para salir): "))   # Pido al usuario cuánto gastar
    
    if gasto == 0:   # Si el usuario escribe 0
        break   # Termino el bucle inmediatamente

    if gasto > saldo:   # Si intenta gastar más de lo que tiene
        print("No tienes suficiente saldo.")   # Aviso de error
        continue   # Vuelvo al inicio del bucle sin descontar nada

    saldo -= gasto   # Resto el gasto al saldo

print(f"Saldo final: {saldo}€")   # Muestro cuánto dinero quedó al final