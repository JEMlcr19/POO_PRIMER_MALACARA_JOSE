class Estudiante:
    def __init__(self, nombre, carrera, matricula):
        self.nombre = nombre
        self.carrera = carrera
        self.matricula = matricula
    
    def estudiar(self):
        print("Estudiando Ando")
    def faltar(self):
        print("Se salto la clase")

alumno1 = Estudiante("Jose", "LANEV", 68821)
alumno2 = Estudiante("Jorge", "LAN", 68848)

print(alumno1.nombre, alumno1.carrera)
print(alumno2.nombre, alumno2.matricula), alumno2.faltar()

