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


#mazo_poker = Mazo()
#mazo_poker.mostrar_mazo()
#mazo_poker.mostrar_nombres()
#mazo_poker.mezclar()

#usuario1 = Jugador("miguel","1000")
#usuario2 = Jugador("charles","1000")

#usuario1.recibir_carta(mazo_poker.Repartir())
#usuario2.recibir_carta(mazo_poker.Repartir())
#usuario1.recibir_carta(mazo_poker.Repartir())
#usuario2.recibir_carta(mazo_poker.Repartir())

#print("")
#print("usuario 1: ",usuario1.name,"   bote:",usuario1.bote)
#usuario1.mostrar_mano()
#print("")
#print("usuario 2: ",usuario2.name,"   bote:",usuario2.bote)
#usuario2.mostrar_mano()
