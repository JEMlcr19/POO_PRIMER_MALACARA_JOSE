#clase carro
class Carro:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.neumatico = None
        self.estacionamiento = None
    
    def rodando(self):
        print("Sali a dar el rol",self.modelo,"run, run")

    def prender(self):
        print("Prendiendo",self.modelo,"arrancando")
    
    def apagarme(self):
        print(self.modelo,"Me voy a ir a dormir")
        print("-------------------------")

#Agregacion
class Dueño:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carros = []
    
    def añadir_carro(self, carro):
        self.carros.append(carro)
        print(carro.modelo, "añadido al garage de carros de", self.nombre )

    def listar_carros(self):
        print(self.nombre, "tiene los siguientes carros: ")
        for carro in self.carros:
            print(carro.modelo)
    
    def dar_la_vuelta(self):
        print(self.nombre, "está dando el rol: ")
        for carro in self.carros:
            carro.rodando()
            print("-------------------------")   

#Asosiación
class Mecanico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carros_arreglados = []

    def arreglar_carro(self, carro): 
        if carro not in self.carros_arreglados:
            self.carros_arreglados.append(carro) 
            print(self.nombre, "está revisando a", carro.modelo)
        else:
            print(self.nombre, "ya reviso el", carro.modelo)    

    def listar_carros_arreglados(self): 
        print(self.nombre, "ha arreglado a los siguientes vehiculos:")
        if not self.carros_arreglados:
            print("No se esta trabajando en ningun carro en este momento, Mecanico disponible")
        for carro in self.carros_arreglados:
            print(carro.modelo)
        print("-------------------------")

#Composición 
class Neumaticos:
    def __init__(self, tipo, condicion):
        self.tipo = tipo
        self.condicion = condicion

    def describir(self):
        print("Este neúmatico es de tipo",
              self.tipo, "y es para condicion",self.condicion)
        
    def inflar(self, psi):
        print(f"Inflando el neumático de tipo {self.tipo} a {psi} psi.")
    
    def revisar_presion(self, psi):
        if psi < 30:
            print("La presión del neumático es baja. Se recomienda inflar.")
        elif psi > 35:
            print("La presión del neumático es alta. Se recomienda desinflar un poco.")
            print("-------------------------")
        else:
            print("La presión del neumático es adecuada.")
            print("-------------------------")
#Herencia
class CarroEspecial(Carro):
    def __init__(self, marca, modelo, año, tipo_utilidad):
        super().__init__(marca, modelo, año)
        self.tipo_utilidad = tipo_utilidad
        
    def funcion(self):
        print(self.modelo, "el carro esta siendo utiliado para:",self.tipo_utilidad)
    
    def describir(self):
        super().describir()
        print("Es carro para uso de",self.tipo_utilidad)
        print("-------------------------")

#Dependencia
class Estacionamiento:
    def __init__(self,tipo, ubicacion):
        self.tipo = tipo
        self.ubicacion = ubicacion
    
    def describir(self):
        print(self.tipo, "Es un estacionamiento que esta ubicado en", self.ubicacion)

    def abrir(self):
        print("El estacionamiento", self.tipo, "está ahora abierto.")
        print("-------------------------")
    def cerrar(self):
        print("El estacionamiento", self.tipo, "está ahora cerrado.")
        print("-------------------------")

# Asociación 2
class Seguro:
    def __init__(self, nombre, numero_poliza):
        self.nombre = nombre
        self.numero_poliza = numero_poliza
        self.carros_asegurados = []

    def asegurar_carro(self, carro):
        self.carros_asegurados.append(carro)
        print(carro.modelo, "ha sido asegurado con la póliza", self.numero_poliza)

    def listar_carros_asegurados(self):
        print("La póliza", self.numero_poliza, "asegura los siguientes carros:")
        for carro in self.carros_asegurados:
            print(carro.modelo)
            print("-------------------------")

# Agregación 2
class Concesionario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carros = []

    def añadir_carro(self, carro):
        self.carros.append(carro)
        print(carro.modelo, "añadido al concesionario", self.nombre)

    def listar_carros(self):
        print("Concesionario", self.nombre, "tiene los siguientes carros:")
        conteo_marcas ={}
        for carro in self.carros:
            if carro.marca in conteo_marcas:
                conteo_marcas[carro.marca] += 1
            else:
                conteo_marcas[carro.marca] = 1
        for marca, cantidad in conteo_marcas.items():
            print(f"{marca}: {cantidad} carro(s)")

    def vender_carro(self, carro):
        if carro in self.carros:
            self.carros.remove(carro)
            print(carro.modelo, "ha sido vendido")
        else:
            print(carro.modelo, "no está en el inventario")
            print("-------------------------")


#objetos clase carro
carro1 = Carro("Honda", "Accord", 2024)
carro2 = Carro("Porsche", "911", 2024)
carro3 = Carro("Honda", "Civic Type R", 2016)

#Dueño objeto
dueño1 = Dueño("Eduardo")

#Objeto Mecanico
mecanico1 = Mecanico("Memo")

#Objeto Neúmatico
neumatico1 = Neumaticos("Slick","Pista")
neumatico2 = Neumaticos("All season","Uso diario")

#Objeto carro especial
finde_carrera = CarroEspecial("Chevrolet","Corvette",2018,"Carreras")
finde_paseo = CarroEspecial("Jeep","Wrangler",98,"Rutear")

#Objeto Estacionamiento
parking1 = Estacionamiento("Privado","5 de febrero")

#Objeto seguro
seguro1 = Seguro("Qualitas", "724766-ZTP")
seguro2 = Seguro("AXA", "153689-JXH")

#Objeto Consesionario
concesionario1 = Concesionario("Honda")
concesionario2 = Concesionario("Porsche")
concesionario3 = Concesionario("Chevrolet")


#Usar metodos carro
carro1.rodando()
carro2.prender()
carro1.apagarme()

#Usar metodos mecanico
mecanico1.arreglar_carro(carro1)

#Usar metodos neumatico
neumatico1.describir()
neumatico1.inflar(32)
neumatico1.revisar_presion(32)

#Usar metodos carro especial
finde_carrera.funcion()

#Usar metodos Estacionamiento
parking1.describir()
parking1.abrir()
#parking1.cerrar()

#Usar metodos Seguro
seguro1.asegurar_carro(carro1)
seguro2.asegurar_carro(finde_carrera)
seguro1.listar_carros_asegurados()

# Usar métodos Concesionario
concesionario1.añadir_carro(carro1)
concesionario1.añadir_carro(carro3)
concesionario2.añadir_carro(carro2)
concesionario1.listar_carros()
concesionario1.vender_carro(carro1)

#Crear Menu de interfaz de usuario
def menu():
    while True:
        print("\nMenú de opciones")
        print("1. Ver detalles del carro")
        print("2. Dar la vuelta con el carro")
        print("3. Prender el carro")
        print("4. Apagar el carro")
        print("5. Añadir carro al dueño")
        print("6. Listar carros del dueño")
        print("7. Arreglar carro con el mecánico")
        print("8. Listar carros arreglados por el mecánico")
        print("9. Describir neumático")
        print("10. Inflar neumático")
        print("11. Revisar presión de neumático")
        print("12. Describir carro especial")
        print("13. Abrir estacionamiento")
        print("14. Cerrar estacionamiento")
        print("15. Asegurar carro")
        print("16. Listar carros asegurados")
        print("17. Añadir carro al concesionario")
        print("18. Listar carros del concesionario")
        print("19. Vender carro del concesionario")
        print("20. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            carro1.rodando()
        elif opcion == "2":
            carro1.prender()
        elif opcion == "3":
            carro1.prender()
        elif opcion == "4":
            carro1.apagarme()
        elif opcion == "5":
            dueño1.añadir_carro(carro1)
        elif opcion == "6":
            dueño1.listar_carros()
        elif opcion == "7":
            mecanico1.arreglar_carro(carro1)
        elif opcion == "8":
            mecanico1.listar_carros_arreglados()
        elif opcion == "9":
            neumatico1.describir()
        elif opcion == "10":
            psi = int(input("Ingrese la presión en psi: "))
            neumatico1.inflar(psi)
        elif opcion == "11":
            psi = int(input("Ingrese la presión en psi: "))
            neumatico1.revisar_presion(psi)
        elif opcion == "12":
            finde_carrera.funcion()
        elif opcion == "13":
            parking1.abrir()
        elif opcion == "14":
            parking1.cerrar()
        elif opcion == "15":
            seguro1.asegurar_carro(carro1)
        elif opcion == "16":
            seguro1.listar_carros_asegurados()
        elif opcion == "17":
            concesionario1.añadir_carro(carro1)
        elif opcion == "18":
            concesionario1.listar_carros()
        elif opcion == "19":
            concesionario1.vender_carro(carro1)
        elif opcion == "20":
            print("Saliendo del menú")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo")
menu()
#Dos lineas de comentarios
#Solo por que queria llegar a 300 lineas de codigo