#Pide al usuario que ingrese tres promedios y encuentra el mayor de ellos (elif)

prom1 = int(input("Dame un promedio: "))
prom2 = int(input("Dame un promedio: "))
prom3 = int(input("Dame un promedio: "))

if prom1 > prom2 and prom3:
    print(prom1, "Es el mayor de los promedios")
elif prom2 > prom1 and prom3:
    print(prom2, "Es el mayor de los promedios")
elif prom3 > prom1 and prom2:
    print(prom3, "Es el mayor de los promedios")