import random
import Jugador
import Mazo
import Mesa
import Mano
import Charmi

class preflop:
    
    def __init__(self,mano,mesa):
        self.hand = []
        self.mano = mano
        self.mesa = mesa

    def mostrar(self):

        print("listas: ")
        print("mano")
        for c in self.hand:
            print(c)

    def unir(self):
       self.hand = self.mano + self.mesa

    def As(self):
        
        for A in range(0,len(self.hand)):
            if self.hand[A].valor == 1:
                return True

    def T_As(self):
        
        for A in range(0,len(self.hand)):
            if self.hand[A].valor == 1:
                self.hand[A].valor = 14

    def I_As(self):
        
        for A in range(0,len(self.hand)):
            if self.hand[A].valor == 14:
                self.hand[A].valor = 1

    def pareja(self):

        for i in range(0,len(self.hand)):
            for j in range(i+1,len(self.hand)):
                if self.hand[i].valor == self.hand[j].valor:
                   return True
        return False
        def poker(self):

        for i in range(0, len(self.hand)):
            poker=1
            for j in range(i+1, len(self.hand)):
                if self.hand[i].valor == self.hand[j].valor:
                    poker += 1
                    if poker == 4:
                        return True
        return False

    def manos(self):

        T_As()

        if self.pareja():
            

