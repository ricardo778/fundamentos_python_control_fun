# Lista de transacciones con diferentes estados y montos
transacciones = [
    {"id": 1, "monto": 1200, "estado": "completada"},
    {"id": 2, "monto": -50, "estado": "error"},
    {"id": 3, "monto": 800, "estado": "pendiente"},
    {"id": 4, "monto": 1500, "estado": "completada"},
    {"id": 5, "monto": 0, "estado": "cancelada"}
]

total_procesado = 0  # Inicializamos el total procesado en 0

# Recorremos cada transacción en la lista
for t in transacciones:
    # Ignoramos transacciones que no están completadas
    if t["estado"] != "completada":
        print(f"Transacción {t['id']}: {t['estado']} - ignorada")
        continue  # Pasamos a la siguiente transacción

    # Verificamos que el monto sea positivo
    if t["monto"] <= 0:
        print(f"Transacción {t['id']}: monto inválido ({t['monto']})")
        continue  # Pasamos a la siguiente transacción

    # Sumamos el monto válido al total procesado
    total_procesado += t["monto"]
    print(f"Transacción {t['id']}: {t['monto']}€ procesada")

# Mostramos el total de transacciones procesadas
print(f"Total procesado: {total_procesado}€")
