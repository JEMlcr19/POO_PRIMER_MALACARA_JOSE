#Objetivo: Practicar el uso de diccionarios y estructuras de control

#Crear un diccionario vacio para almacenar información de los estuduiantes
estudiante = {}
calificaciones = {}
eleccion = ""

#Crear un menu que permita al usario agregar estudiantes con sus calificaciones de un estudiante especifico
#Escribiendo "C" salimos del menu.
while eleccion.upper() != "C": 
    print("Que es lo que deseas hacer hoy: ")
    print("A) Agregar Estudiante y Calificaciones")
    print("B) Visualizar calificaciones")
    print("C) Salir")
    eleccion = str(input()) #Obtiene la opcion seleccionada
    eleccion.upper()


    #Opcion A es para ingresar el nombre del estudiante
    if eleccion.upper() == "A":
        print("Ingrese el nombre completo del estudiante \n empezando por apellidos")
        nombre = str(input("Ingrese el nombre del estudiante completo: "))
        #Agregar la materia a evaluar, con "fin" salimos de este ciclo
        while True:
            print("Ingrese el nombre de la materia, Para salir escribir 'fin'")
            materia = str(input())
            if materia.lower() == "fin":
                break
            calificacion = float(input("Ingrese la calificacion"))

            #Guarda el nombre y calificacion del estudiante en el diccionario
            calificaciones[materia] = calificacion
            estudiante[nombre] = calificaciones

            #Imprime los datos ingresados
            print(estudiante)

    #Opcion B para buscar el nombre del usuario comenzando por apellido
    elif eleccion.upper() == "B":
        nombre = input("Ingrese el nombre del estudiante que quiere consultar: ")

    #Imprime los datos del alumno buscado
        if nombre in estudiante:
            print(f"{nombre}: {calificaciones}")

   