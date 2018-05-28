import random

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

    #Menor a mayor
    def sort(self,hand_sort):

        for i in range(0,len(hand_sort)):
            for j in range(i+1,len(hand_sort)):
                if hand_sort[i].valor > hand_sort[j].valor:
                    k = hand_sort[i]
                    hand_sort[i]= hand_sort[j]
                    hand_sort[j] = k
        return hand_sort

    #Mayor a menor
    def msort(self, hand_sort):
        As = False
        A = 0
        for a in range (0,len(hand_sort)):
            if hand_sort[a].valor == 1:
                A = a
                As = True
        print("AS",As)
        if As:
            hand_sort[A].valor = 14

        for i in range(0, len(hand_sort)-1):
            for j in range(i + 1, len(hand_sort)):
                if hand_sort[i].valor < hand_sort[j].valor:
                    k = hand_sort[i]
                    hand_sort[i] = hand_sort[j]
                    hand_sort[j] = k
        return hand_sort

    def color(self):
        hand = self.hand

        for co in range(0, (len(hand)//2)):
            color = 0
            carta = random.randrange(len(hand) - 1)
            for c in range(0, len(hand)):

                if hand[c].palo == hand[carta].palo:
                    color += 1

            if color == 5:
                return True

            else:
                hand.pop(carta)

        return False

    def escalera(self):
        hand = self.hand
        Resp = False
        escalera = self.sort(hand)

        for v in range(0, 3):
            m_escalera = 1
            for c in range(0, 5):
                if ((escalera[c].valor) + 1) == escalera[c + 1].valor:
                    m_escalera += 1
                    if m_escalera == 5:
                        Resp=True
                        return Resp

        if escalera[0].valor == 1 and Resp == False:
            escalera[0].valor = 14
            cambio = escalera.pop(0)
            escalera.append(cambio)

            for p in escalera:
                print("orden", p.valor)

            for v in range(0, 3):
                m_escalera = 1
                for c in range(v, 6):
                    if ((escalera[c].valor) + 1) == escalera[c + 1].valor:
                        m_escalera += 1
                        print(m_escalera)
                        if m_escalera == 5:
                            Resp = True
                            return Resp


        return Resp

    def escalera_color(self):

        if self.escalera() and self.color():
            return True

        return False

    def escalera_real(self):
        hand = self.hand
        As = False

        for a in range (0,len(hand)):
            if hand[a].valor == 1:
                As = True

        if self.escalera() and self.color() and As:
            return True

        return False

    def pareja(self):
        hand = self.hand

        for i in range(0,len(hand)):
            for j in range(i+1,len(hand)):
                if hand[i].valor == hand[j].valor:
                   return True
        return False

    def doble_pareja(self):
        hands = self.hand
        hand = self.msort(hands)
        pareja = 0

        for i in range(0, len(hand)):
            j=i+1
            if hand[i].valor == hand[j].valor:
                pareja += 1
                if pareja == 2:
                    return True

        return False

    def trio(self):
        hand = self.hand
        trio = 1

        for i in range(0,len(hand)):
            for j in range(i+1,len(hand)):
                if hand[i].valor == hand[j].valor:
                    trio += 1
                    if trio == 3:
                        return True
        return False

    def poker(self):
        hand = self.hand
        poker = 1

        for i in range(0, len(hand)):
            for j in range(i + 1, len(hand)):
                if hand[i].valor == hand[j].valor:
                    poker += 1
                    if poker == 4:
                        return True
        return False

    def Fullin(self):
        hands = self.hand
        hand = self.msort(hands)
        trio = 1
        par = 1

        for p in hand:
            print(p)

        for i in range(0,len(hand)):
            if hand[i].valor == hand[i+1].valor:
                trio += 1
                if trio == 3:
                    print("entro")
                    for j in range(i+2,len(hand)-1):
                        if hand[j].valor == hand[j + 1].valor:
                            par += 1
                            if par == 2:
                                return True
                    return False
        return False

    def Fullon(self):
        hands = self.hand
        hand = self.msort(hands)
        trio = 1
        par = 1

        for p in hand:
            print(p)

        for i in range(0,len(hand)):
            if hand[i].valor == hand[i+1].valor:
                par += 1
                if par == 2:
                    print("entro")
                    for j in range(i+2,len(hand)-1):
                        if hand[j].valor == hand[j + 1].valor:
                            trio += 1
                            if trio == 3:
                                return True
                    return False
        return False