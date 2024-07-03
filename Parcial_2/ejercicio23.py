#clase carro
class Carro:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def rodando(self):
        print("Sali a dar el rol",self.modelo,"run, run")

    def prender(self):
        print("Prendiendo",self.modelo,"arrancando")
    
    def apagarme(self):
        print(self.modelo,"Me voy a ir a dormir")

#objetos clase carro
carro1 = Carro("Honda", "Accord", 2024)
carro2 = Carro("Porsche", "911", 2024)

#Usar metodos
carro1.rodando()
carro2.prender()
