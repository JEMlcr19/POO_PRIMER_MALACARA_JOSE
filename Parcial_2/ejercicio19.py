#Crea un programa con 2 conjuntos con 
#nombres de frutas, luego únelos en un 
#nuevo conjunto y agrega otra fruta.
#Imprime el resultado de la unión y del 
#conjunto final

frutas1 = {"manzana", "platano", "papaya", "fresa"}
frutas2 = {"durazno", "melon", "mango", "sandia"}
frutas2.add("naranja")
union = frutas1 | frutas2
print(union)