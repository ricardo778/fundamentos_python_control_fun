# Definimos una lista de condiciones booleanas
condiciones = [True, True, False, True]

# Verificamos si todas las condiciones son verdaderas usando all()
if all(condiciones):
    print("Todas las condiciones son verdaderas.")
else:
    # Si al menos una condición es falsa
    print("Al menos una condición es falsa.")