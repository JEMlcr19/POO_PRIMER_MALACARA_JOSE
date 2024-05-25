#Programa que categorice las edades de una lista en mayores o menores de edad
#(mínimo 8 edades) e imprima una lista por cada caso.
#Nota: se crearían otras listas vacías para las edades de adultos y menores que se 
#llenarían con los datos correspondientes (usando la instrucción para agregar) en la 
#condición.

edades = [11,15,12,18,20,22,24,13]

edad_mayor = []
edad_menor = []

for edad in edades:
    if edad >= 18:
        edad_mayor.append(edad)
    else:
        edad_menor.append(edad)

print("Edad de mayor a menor", edad_mayor)
print("Edad de menor a mayor", edad_menor)