import random
import Jugador
import Mesa
import Charmi

class Carta:
    lista_Palos = ["nada","Corazones","Picas","Diamantes","Tréboles"]
    lista_naipes = ["nada","As","2","3","4","5","6","7","8","9","10","Jota","Reina","Rey","AS 14"]

    def __init__(self,palo=0,valor=0):
        self.palo=palo
        self.valor=valor

    def __str__(self):
        return (self.lista_naipes[self.valor] + " de " + self.lista_Palos[self.palo])

class Mazo:

# atributos de la clase

    def __init__(self):
        self.cartas = []
        for palo in range(1,5):
            for valor in range(1, 14):
                self.cartas.append(Carta(palo, valor))

    def mostrar_mazo(self):
        for carta in self.cartas:
         print(carta.valor,carta.palo)


    def mostrar_nombres(self):
        for carta in self.cartas:
            print(carta)

    def mezclar(self):
        random.shuffle(self.cartas)

    def repartir(self):
        return self.cartas.pop(0)

    def repartirc(self,c):
        return self.cartas.pop(c)
        #return self.cartas[c]

    def retornar(self,c):
        self.cartas.append(c)