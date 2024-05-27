edades = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

infancia = []
adolescentes = []
jovenes = []
adultos = []

for edad in edades:
    if edad <= 11:
        infancia.append(edad) 
    elif edad <= 17:
        adolescentes.append(edad)
    elif edad <= 26:
        jovenes.append(edad)
    else:
        adultos.append(edad)
print("Infantes", infancia)
print("Adolescentes", adolescentes)
print("Jóvenes", jovenes)
print("Adultos",adultos)