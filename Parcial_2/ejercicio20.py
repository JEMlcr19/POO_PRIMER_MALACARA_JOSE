#Crea un programa que una 3 conjuntos, 
#luego recorrer ese conjunto y hacer uno 
#nuevo con únicamente los valores 
#pares, imprimir el resultado.

numero1 = {1,2,3,4,5,6}
numeros2 = {7,8,9,10,11,12}
numeros3 = {13,14,15,16,17,18}

union = numero1 | numeros2 | numeros3
print(union)

for pares in union:
    if pares % 2 == 0:
        print(pares)
