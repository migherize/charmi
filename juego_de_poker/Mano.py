import random
import Jugador
import Mazo
import Mesa
import Mano
import Charmi

class hand:
    
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


    # Menor a mayor
    def sort(self, hand_sort):

        for i in range(0, len(hand_sort)-1):
            for j in range(i + 1, len(hand_sort)):
                if hand_sort[i].valor > hand_sort[j].valor:
                    k = hand_sort[i]
                    hand_sort[i] = hand_sort[j]
                    hand_sort[j] = k
        return hand_sort

    def color(self):

        for co in range(0, (len(self.hand)//2)):
            color = 1
            for c in range(co+1, len(self.hand)):
                if self.hand[co].palo == self.hand[c].palo:
                    color += 1
            if color == 5:
                return True

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
                    c=4

        """
        if escalera[0].valor == 1 and Resp == False:
            escalera[0].valor = 14
            cambio = escalera.pop(0)
            escalera.append(cambio)

            for v in range(0, 3):
                m_escalera = 1
                for c in range(v, 6):
                    if ((escalera[c].valor) + 1) == escalera[c + 1].valor:
                        m_escalera += 1
                        if m_escalera == 5:
                            Resp = True
                            return Resp
        """
        return Resp

    def escalera_color(self):

        if self.escalera() and self.color():
            return True

        return False

    def escalera_real(self):
        self.hand
        As = False

        if self.escalera() == False:

            for a in range (0,len(self.hand)):
                if self.hand[a].valor == 1:
                    As = True

            if self.escalera() and self.color() and As:
                return True

        return False

    def pareja(self):

        for i in range(0,len(self.hand)):
            for j in range(i+1,len(self.hand)):
                if self.hand[i].valor == self.hand[j].valor:
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

    def trio(self):

        for i in range(0,len(self.hand)):
            trio = 1
            for j in range(i+1,len(self.hand)):
                if self.hand[i].valor == self.hand[j].valor:
                    trio += 1
                    if trio == 3:
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

    def carta_alta(self):
        hands = self.hand
        self.hand = self.sort(hands)
        self.hand.reverse()
        carta_alta =self.hand[0]
        return carta_alta

    def manos(self):

        #for m in self.hand:
            #print("La mano que tienes es: ",m)

        if self.poker():
            return 8

        elif self.fullon():
            return 7

        elif self.fullin():
            return 6

        elif self.color():
            return 5

        elif self.escalera():
            return 4

        elif self.trio():
            return 3

        elif self.doble_pareja():
            return 2

        elif self.pareja():
            return 1

        else:
            return 0
          #  return self.carta_alta()

        """
        if self.color():
            if self.escalera():
                if self.As():
                    print("Tienes escalera Real de color")
                    return 10
                else:
                    print("Tienes Escalera de color")
                    return 9
            else:
                print("Tienes color")
                return 5
        
        else:
            if self.poker():
                print("Tienes Poker")
                return 8
            
            if self.fullon():
                print("Tienes Full House")
                return 7
            if self.fullin():
                print("Tienes Full House")
                return 6
            
            if self.trio():
                print("Tienes Trio")
                return 3
            if self.doble_pareja():
                print("Tienes 2 pares")
                return 2
            if self.pareja():
                print("Tienes un par")
                return 1
            else:
                print("carta alta", self.carta_alta())
                return 0

        """