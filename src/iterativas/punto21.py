# --- Usando while ---
suma = 0  # Inicializo la variable suma en 0
i = 1     # Inicializo el contador i en 1
while i <= 10:  # Mientras i sea menor o igual a 10
    suma += i   # Sumo el valor de i a la variable suma
    i += 1      # Incremento i en 1
print(f"Suma (while): {suma}")  # Muestro la suma calculada con while

# --- Equivalente con for ---
suma = 0  # Reinicio la variable suma en 0
for i in range(1, 11):  # Recorro los números del 1 al 10
    suma += i           # Sumo cada número a la variable suma
print(f"Suma (for): {suma}")  # Muestro la suma calculada con for
