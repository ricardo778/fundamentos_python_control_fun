# Definimos el saldo inicial de la cuenta
saldo = 300

# Definimos el valor que el usuario desea retirar
retiro = 500

# Verificamos si el saldo es suficiente para realizar el retiro
if saldo >= retiro:
    # Si el saldo alcanza, se descuenta el valor del retiro
    saldo -= retiro
    # Confirmamos que el retiro fue exitoso
    print("Retiro exitoso.")
    # Mostramos el nuevo saldo después del retiro
    print(f"Nuevo saldo: {saldo}")
else:
    # Si el saldo no es suficiente, mostramos un mensaje de error
    print("Fondos insuficientes.")
    # Mostramos el saldo actual disponible
    print(f"Saldo actual: {saldo}")