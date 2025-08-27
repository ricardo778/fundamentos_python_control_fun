# Defino la variable n con el valor 10, que representa hasta qué número quiero sumar.
n = 10  

# Inicializo la variable suma en 0, donde se acumulará el resultado.
suma = 0  

# Uso un bucle for que recorre desde 1 hasta n (incluido).
for i in range(1, n+1):  
    # En cada iteración, sumo el valor actual de i a la variable suma.
    suma += i  

# Imprimo el resultado de la suma con un mensaje descriptivo.
print(f"La suma de los primeros {n} números es: {suma}")  # 55  
