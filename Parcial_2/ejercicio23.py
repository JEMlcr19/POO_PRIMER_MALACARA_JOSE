#Definir la clase
class Estudiante:  #Nombre de la clase
    def __init__(self, nombre, carrera, matricula):
        self.nombre = nombre #Atributo
        self.carrera = carrera #Atributo
        self.matricula = matricula #Atributo
    
    def estudiar(self): #Metodo 1
        print("Estudiando Ando")
    def faltar(self): #Metodo 2
        print("Se salto la clase")
    def examn(self): #Metodo 3
        print("El alumno esta presentando examen")

class Horario:
    def __init__(self, materia, hora):
        self.materia = materia
        self.hora = hora

#Definir Objetos
alumno1 = Estudiante("Jose", "LANEV", 68821)
alumno2 = Estudiante("Jorge", "LAN", 68848)

#Mostrar los atributos del objeto
print(alumno1.nombre, alumno1.carrera), alumno1.examn()
print(alumno2.nombre, alumno2.matricula), alumno2.faltar() #El metodo de la clase para mi objeto


class Deporte:
    def _init_(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion
    def entrenando(self):
        print("Entrenando mi deporte")

    def escuchar(self):
        print("Escuchando musica ideal para el entreno")

class Entrenamiento:
    def _init_(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.entrenamientos = []

    def ir_a_entrenar(self, deporte):
        self.ir_a_entrenar(deporte)
        print(f"{self.nombre} entreno {Entrenamiento.nombre}")

    def entrenamiento_realizad(self):
        print(f"{self.nombre} ha realizado estos entrenos en la semana:")
        for entrenamiento in self.entrenamientos:
            print(entrenamiento.nombre)


