def Nombre_Premier():
    for n in range(2, 100):
        if all(n % i != 0 for i in range(2, n)):
            print(n)

Nombre_Premier()