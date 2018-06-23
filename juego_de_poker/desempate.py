import random
import Jugador
import Mazo
import Mesa
import Mano
import Charmi

class parametros:
    
    def __init__(self,mano,mesa):
        self.hand = []
        self.mano = mano
        self.mesa = mesa
        self.jugada = []
        self.num = 0

    def mostrar(self):

        print("listas: ")
        print("mano")
        for c in self.hand:
            print(c)

    def unir(self):
       self.hand = self.mano + self.mesa

    def sort(self, hand_sort):

        for i in range(0, len(hand_sort)-1):
            for j in range(i + 1, len(hand_sort)):
                if hand_sort[i].valor > hand_sort[j].valor:
                    k = hand_sort[i]
                    hand_sort[i] = hand_sort[j]
                    hand_sort[j] = k

        return hand_sort

    def sortc(self, hand_sort):

        for i in range(0, len(hand_sort)-1):
            for j in range(i + 1, len(hand_sort)):
                if hand_sort[i].palo > hand_sort[j].palo:
                    k = hand_sort[i]
                    hand_sort[i] = hand_sort[j]
                    hand_sort[j] = k

        return hand_sort

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

    def escalera_color(self):

        cartaAlta = []
        self.num = 5
        cm = 0
        t = 0

        hands = self.hand
        self.hand = self.sortc(hands)

        a,b,c=self.escalera()      

        cartaAlta=self.jugada
        cm=self.carta_mano(cm)
        return self.num,cm,cartaAlta   

    def escalera(self):

        cartaAlta = []
        col = []
        self.num = 5
        cm = 0
        t = 0

        self.T_As()

        hands = self.hand
        self.hand = self.sort(hands)

        for v in range(0, 3):
            m_escalera = 1
            for c in range(v, len(self.hand)):
                if (self.hand[c].valor + 1) == self.hand[c + 1].valor:
                    m_escalera += 1
                    if t == 0:
                        col.append(c)
                        col.append(c+1)
                        t=1
                    elif t<4:
                        if len(col)<=4:
                            col.append(c+1)
                        t+=1

                        if m_escalera == 5:
                            
                            for r in range(0,5):
                                self.jugada.append(self.hand[col[r]])  
                            cartaAlta=self.jugada
                            cm=self.carta_mano(cm)
                            return self.num,cm,cartaAlta        
                else:
                    c=4
                    t=0
                    m_escalera=1
                    col =[]

        self.T_As()


        cartaAlta = []
        col = []
        self.num = 5
        cm = 0
        t = 0

        for v in range(0, 3):
            m_escalera = 1
            for c in range(v, len(self.hand)):
                if (self.hand[c].valor + 1) == self.hand[c + 1].valor:
                    m_escalera += 1
                    if t == 0:
                        col.append(c)
                        col.append(c+1)
                        t=1
                    elif t<4:
                        if len(col)<=4:
                            col.append(c+1)
                        t+=1

                        if m_escalera == 5:
                            
                            for r in range(0,5):
                                self.jugada.append(self.hand[col[r]])  
                            cartaAlta=self.jugada
                            cm=self.carta_mano(cm)
                            return self.num,cm,cartaAlta        
                else:
                    c=4
                    t=0
                    m_escalera=1
                    col =[]

   


    def color(self):

        cartaAlta = []
        self.num = 5
        cm = 0
        t = 0
        m = 0
        self.T_As()

        for co in range(0, (len(self.hand)//2)):
            color = 1
            t=0
            col = []
            for c in range(co+1, len(self.hand)):
                if self.hand[co].palo == self.hand[c].palo:
                    if t == 0:
                        col.append(co)
                        col.append(c)
                        t=1
                    elif t==1:
                        col.append(c)

                    color += 1
            if color == 5:
                for r in range(0,5):
                    self.jugada.append(self.hand[col[r]])  

                cartaAlta=self.jugada

                cm=self.carta_mano(cm)
                return self.num,cm,cartaAlta

    def fullon(self):

        cartaAlta = []
        self.num = 5
        cm = 0
        t = 0
        self.T_As()

        hand = self.hand
        self.hand = self.sort(hand)
        self.hand.reverse()

        trio = 1
        par = 1

        for i in range(0,len(self.hand)-1):
            if self.hand[i].valor == self.hand[i+1].valor:
                trio += 1
                k=i+1
                cartaAlta.append(self.hand[i])
                self.jugada.append(self.hand[i])
                cartaAlta.append(self.hand[k])
                self.jugada.append(self.hand[k])
                cartaAlta.append(self.hand[k+1])
                self.jugada.append(self.hand[k+1])
                trio=3
                if trio == 3:
                    for j in range(i+2,len(self.hand)-1):
                        if self.hand[j].valor == self.hand[j + 1].valor:
                            par += 1
                            cartaAlta.append(self.hand[j])
                            self.jugada.append(self.hand[j])
                            cartaAlta.append(self.hand[j+1])
                            self.jugada.append(self.hand[j+1]) 
                            cm=self.carta_mano(cm)
                            return self.num,cm,cartaAlta

    
    def fullin(self):

        cartaAlta = []
        self.num = 5
        cm = 0
        t = 0
        self.T_As()

        hands = self.hand
        self.hand = self.sort(hands)
        self.hand.reverse()
        trio = 1
        par = 1

        for i in range(0,len(self.hand)-1):
            if self.hand[i].valor == self.hand[i+1].valor:
                par += 1
                cartaAlta.append(self.hand[i])
                self.jugada.append(self.hand[i])
                cartaAlta.append(self.hand[i+1])
                self.jugada.append(self.hand[i+1])

                if par == 2:
                    for j in range(i+2,len(self.hand)-1):
                        k=j+1
                        if self.hand[j].valor == self.hand[k].valor:
                            trio += 1
                            cartaAlta.append(self.hand[j])
                            self.jugada.append(self.hand[j])
                            cartaAlta.append(self.hand[k])
                            self.jugada.append(self.hand[k])
                            cartaAlta.append(self.hand[k+1])
                            self.jugada.append(self.hand[k+1])
                            cm=self.carta_mano(cm)
                            return self.num,cm,cartaAlta


    def poker(self):

        cartaAlta = []
        self.num = 4
        cm = 0
        t = 0

        for i in range(0, len(self.hand)):
            poker=1
            for j in range(i+1, len(self.hand)):
                if self.hand[i].valor == self.hand[j].valor:
                    poker += 1
                    if t==0:                    
                        cartaAlta.append(self.hand[i])
                        self.jugada.append(self.hand[i])
                        cartaAlta.append(self.hand[j])
                        self.jugada.append(self.hand[j])
                        t=1
                    elif t==1: 
                        cartaAlta.append(self.hand[j])
                        self.jugada.append(self.hand[j])
                        t=2
                    elif t==2: 
                        cartaAlta.append(self.hand[j])
                        self.jugada.append(self.hand[j])
                        t=3

        
        cm=self.carta_mano(cm)

        return self.num,cm,cartaAlta

    def trio(self):

        cartaAlta = []
        self.num=3
        cm = 0
        t=0

        for i in range(0,len(self.hand)):
            trio = 1
            for j in range(i+1,len(self.hand)):
                if self.hand[i].valor == self.hand[j].valor:
                    trio += 1
                    if t==0:                    
                        cartaAlta.append(self.hand[i])
                        self.jugada.append(self.hand[i])
                        cartaAlta.append(self.hand[j])
                        self.jugada.append(self.hand[j])
                        t=1
                    elif t==1: 
                        cartaAlta.append(self.hand[j])
                        self.jugada.append(self.hand[j])
                        t=2

        cm=self.carta_mano(cm)

        return self.num,cm,cartaAlta

    def doble_pareja(self):

        cartaAlta = []
        self.num=4
        cm = 0

        hands=self.hand
        self.hand = self.sort(hands)

        self.hand.reverse()
        pareja = 0

        for i in range(0, len(self.hand)-1):
            j=i+1
            if self.hand[i].valor == self.hand[j].valor:
                pareja += 1
                cartaAlta.append(self.hand[i])
                self.jugada.append(self.hand[i])
                cartaAlta.append(self.hand[j])
                self.jugada.append(self.hand[j])   

        cm=self.carta_mano(cm)

        return self.num,cm,cartaAlta

    def pareja(self):

        cartaAlta = []
        self.num=2
        cm = 0

        for i in range(0,len(self.hand)):
            for j in range(i+1,len(self.hand)):
                if self.hand[i].valor == self.hand[j].valor:
                   cartaAlta.append(self.hand[i])
                   self.jugada.append(self.hand[i])
                   cartaAlta.append(self.hand[j])
                   self.jugada.append(self.hand[j])

        cm=self.carta_mano(cm)

        return self.num,cm,cartaAlta

    def mcarta_alta(self):
        cartaAlta = []

        self.T_As()
        hands = self.hand
        self.hand = self.sort(hands)
        self.hand.reverse()

        cartaAlta=self.hand

        return cartaAlta

    def carta_alta(self,hand):
        cartaAlta = []
        remove1=[]
        remove2=[]
        m=0

        self.T_As()
        hands = self.hand
        self.hand = self.sort(hands)
        self.hand.reverse()

        for i in range(0,len(hand)):
            for j in range(0,len(self.hand)):
                if hand[i]==self.hand[j]:
                    remove1.append(j)

        remove2=list(set(remove1))

        remove2.sort()      

        for r in range(0,len(remove2)):
            self.hand.pop(remove2[r]+m)
            m=m-1

        cartaAlta=self.hand

        return cartaAlta

    def carta_mano(self,cm):
        for a in range(0,2):
            for b in range(0,len(self.jugada)):
                if self.jugada[b]==self.mano[a]:
                    cm=cm+1
        return cm


    def ganar(self,hand):

        if hand==1:
            a,b,c=self.pareja()
            d=self.carta_alta(c)
            return a,b,c,d
        elif hand == 2:
            a,b,c=self.doble_pareja()
            d=self.carta_alta(c)
            return a,b,c,d
        elif hand == 3:
            a,b,c=self.trio()
            d=self.carta_alta(c)
            return a,b,c,d
        elif hand == 4:
            a,b,c=self.escalera()
            d=self.carta_alta(c)
            return a,b,c,d

        elif hand == 8:
            a,b,c=self.poker()
            d=self.carta_alta(c)
            return a,b,c,d
        elif hand == 6:
            a,b,c=self.fullin()
            d=self.carta_alta(c)
            return a,b,c,d
        elif hand == 7:
            a,b,c=self.fullon()
            d=self.carta_alta(c)
            return a,b,c,d
        elif hand == 5:
            a,b,c=self.color()
            d=self.carta_alta(c)
            return a,b,c,d
        elif hand == 9:
            a,b,c=self.escalera_color()
            d=self.carta_alta(c)
            return a,b,c,d
        elif hand == 10:
            a,b,c=self.escalera_color()
            d=self.carta_alta(c)
            return a,b,c,d
        elif hand == 0:
            a=1
            b=0
            c=self.mcarta_alta()
            d=c
            return a,b,c,d


      