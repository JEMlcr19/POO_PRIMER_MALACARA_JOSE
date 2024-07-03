#clase carro
class Carro:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.neumatico = None
    
    def rodando(self):
        print("Sali a dar el rol",self.modelo,"run, run")

    def prender(self):
        print("Prendiendo",self.modelo,"arrancando")
    
    def apagarme(self):
        print(self.modelo,"Me voy a ir a dormir")

#Agregacion
#AGREGACIÓN
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
            print(carro.nombre)
    
    def dar_la_vuelta(self):
        print(self.nombre, "está dando el rol: ")
        for perro in self.carros:
            perro.rodando()

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
        for carro in self.carros_arreglados:
            print(carro.modelo)

#Composición 
class Neumaticos:
    def __init__(self, tipo, condicion):
        self.tipo = tipo
        self.condicion = condicion

    def describir(self):
        print("Este neúmatico es de tipo",
              self.tipo, "y es para condicion",self.condicion)

#objetos clase carro
carro1 = Carro("Honda", "Accord", 2024)
carro2 = Carro("Porsche", "911", 2024)

#Dueño objeto
dueño1 = Dueño("Eduardo")

#Objeto Mecanico
mecanico1 = Mecanico("Memo")

#Objeto Neúmatico
neumatico1 = Neumaticos("Slick","Pista")
neumatico2 = Neumaticos("All season","Uso diario")

#Usar metodos carro
carro1.rodando()
carro2.prender()
carro1.apagarme()

#Usar metodos mecanico
mecanico1.arreglar_carro(carro1)

#Usar metodos neumatico
neumatico1.describir()