import random
import Jugador
import Mazo
import Mesa
import Mano
import Charmi

class flop:
    
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

    def fullon(self):
        hand = self.hand
        self.hand = self.sort(hand)
        self.hand.reverse()

        trio = 1
        par = 1

        for i in range(0,len(self.hand)-1):
            if self.hand[i].valor == self.hand[i+1].valor:
                trio += 1
                if trio == 3:
                    for j in range(i+2,len(self.hand)-1):
                        if self.hand[j].valor == self.hand[j + 1].valor:
                            par += 1
                            if par == 2:
                                return True
                    return False
        return False

    def fullin(self):
        hands = self.hand
        self.hand = self.sort(hands)
        self.hand.reverse()
        trio = 1
        par = 1

        for i in range(0,len(self.hand)-1):
            if self.hand[i].valor == self.hand[i+1].valor:
                par += 1
                if par == 2:
                    for j in range(i+2,len(self.hand)-1):
                        if self.hand[j].valor == self.hand[j + 1].valor:
                            trio += 1
                            if trio == 3:
                                return True
                    return False
        return False

    def trio(self):

        for i in range(0,len(self.hand)):
            trio = 1
            for j in range(i+1,len(self.hand)):
                if self.hand[i].valor == self.hand[j].valor:
                    trio += 1
                    if trio == 3:
                        return True
        return False

    def doble_pareja(self):
        hands=self.hand
        self.hand = self.sort(hands)

        self.hand.reverse()
        pareja = 0

        for i in range(0, len(self.hand)-1):
            j=i+1
            if self.hand[i].valor == self.hand[j].valor:
                pareja += 1
                if pareja == 2:
                    return True

        return False