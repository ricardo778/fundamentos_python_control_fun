# punto25.py

# Definimos los valores de las variables
a = 5
b = 10
c = 15

# Comparamos a con b
if a > b:
    # Si a es mayor que b, comparamos a con c
    if a > c:
        print('a es el mayor.')
    else:
        # Si c es mayor que a, comparamos c con b
        if c > b:
            print('c es el mayor.')
        else:
            print('b es el mayor.')
else:
    # Si b es mayor o igual que a, comparamos b con c
    if b > c:
        print('b es el mayor.')
    else:
        print('c es el mayor.')
