import random
import Jugador
import Mazo
import Mesa
import Mano
import Charmi
from desempate import parametros

class hand:
    
    def __init__(self,mano,mesa):
        self.hand = []
        self.mano = mano
        self.mesa = mesa
        self.c = 0
        self.e = 0

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

    # Menor a mayor
    def sort(self, hand_sort):

        for i in range(0, len(hand_sort)-1):
            for j in range(i + 1, len(hand_sort)):
                if hand_sort[i].valor > hand_sort[j].valor:
                    k = hand_sort[i]
                    hand_sort[i] = hand_sort[j]
                    hand_sort[j] = k
        return hand_sort

    def escalera_real(self):

        if self.escalera() and self.color():
            #Arreglar que es el As este en la escalera
            return True

        return False

    def escalera_color(self):

        if self.escalera() and self.color():
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

    def color(self):

        for co in range(0, (len(self.hand)//2)):
            color = 1
            for c in range(co+1, len(self.hand)):
                if self.hand[co].palo == self.hand[c].palo:
                    color += 1
            if color == 5:
                return True
            else:
                if self.c<color:
                    self.c=color

        return False

    def escalera(self):

        hands = self.hand
        self.hand = self.sort(hands)
        Resp = False

        for v in range(0, 3):
            m_escalera = 1
            for c in range(v, len(self.hand)-1):
                if (self.hand[c].valor + 1) == self.hand[c + 1].valor:
                    m_escalera += 1

                    if m_escalera == 5:
                        Resp=True
                        return Resp
                else:
                    if self.e<m_escalera:
                        self.e=m_escalera
                    c=4
                    m_escalera=1
        return Resp

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

    def pareja(self):

        for i in range(0,len(self.hand)):
            for j in range(i+1,len(self.hand)):
                if self.hand[i].valor == self.hand[j].valor:
                   return True
        return False

    def carta_alta(self):
        hands = self.hand
        self.hand = self.sort(hands)
        self.hand.reverse()
        carta_alta =self.hand[0]
        return carta_alta

    def manos(self):

        if self.As():
            self.T_As()
            if self.escalera_real():
                self.I_As()
                return 10
            self.I_As()

        elif self.escalera_color():
            return 9

        self.T_As()

        if self.poker():
            self.I_As()
            return 8

        elif self.fullon():
            self.I_As()
            return 7

        elif self.fullin():
            self.I_As()
            return 6

        elif self.color():
            self.I_As()
            return 5

        elif self.escalera():
            self.I_As()
            return 4

        if self.As():
            self.I_As()
            if self.escalera():
                return 4

        self.T_As()

        if self.trio():
            self.I_As()
            return 3

        elif self.doble_pareja():
            self.I_As()
            return 2

        elif self.pareja():
            self.I_As()
            return 1

        else:
            self.I_As()
            return 0

    def preflop(self,m):

        self.T_As()

        mano= self.mano
        self.mano=self.sort(mano)
        self.mano.reverse()

        if m == 0:
            if self.mano[0].palo == self.mano[1].palo:
                self.I_As()
                return True
            elif (self.mano[0].valor + 4) < self.mano[1].valor and self.mano[0].valor < 8:
                self.I_As()
                return False
            self.I_As()
            return True
        elif m==1:
            return True

    def flop(self,m):

        self.T_As()
        mano= self.mano
        self.mano=self.sort(mano)
        self.mano.reverse()

        if m == 0:
            #Arreglar propensa escalera
            print("propenso escalera",self.e)
            print("propenso color",self.c)

            if self.e > 2:
                return True
            elif self.c > 2:
                return True
            elif self.mano[0].valor>8:
                return True
            return False
        elif m==1:
            desempates = parametros(self.mano,self.mesa)
            desempates.unir()

            n,cm,cartasA,s_cartasA=desempates.ganar(m)
            if cartasA[0].valor < 5 and self.mano[0].valor < 7:
                return False
            else:
                return True 
        elif m>1:
            return True
"""
    def turn(self,m):

        if m == 0:
            return 0
        elif m==1:
            return 1
        elif m>1:
            return 2

    def river(self,m):

        if m == 0:
            return 0
        elif m==1:
            return 1
        elif m>1:
            return 2
"""