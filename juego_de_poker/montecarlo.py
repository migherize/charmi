import random
import Jugador
import Mazo
import Mesa
import Mano
import Charmi

mesa = Mesa.Mesa()

class probabilidades():

    def __init__(self,m,mc):
        self.mazo = m
        self.mano_charmi =mc

    def kelly(self,bote_mesa,subida,prob,):

        cuota = bote_mesa / subida

        bankroll = (cuota*(prob/100)-1)*100 / cuota -1

        return bankroll



    # DESICIONES DE CHARMI

    def montecarlo(self):

        run = 1
        lose = 0
        win = 0
        draw = 0

        for it in range(0, run):

            lcharmi = self.mano_charmi
            mazo = self.mazo

            mazo.mostrar_nombres()

            lusuario = []

            lusuario.append(mazo.repartir())
            lusuario.append(mazo.repartir())

            mesa.quemar(mazo.repartir())
            mesa.recibir_mano(mazo.repartir())
            mesa.recibir_mano(mazo.repartir())
            mesa.recibir_mano(mazo.repartir())
            mesa.quemar(mazo.repartir())
            mesa.recibir_mano(mazo.repartir())
            mesa.quemar(mazo.repartir())
            mesa.recibir_mano(mazo.repartir())

            for c in lcharmi:
                print("cha",c)
            for c in lusuario:
                print("usu",c)

            mesa.mostrar_mano()
            lmesa = mesa.mesa

            # Mano de charmi
            mano1 = Mano.hand(lcharmi, lmesa)
            mano1.unir()

            res1 = mano1.manos()

            # Mano de usuario
            mano2 = Mano.hand(lusuario, lmesa)
            mano2.unir()
            res2 = mano1.manos()

            print("res1",res1)
            print("res1", res2)

            if res1 < res2:
                lose += 1

            elif res1 > res2:
                win += 1

            elif res1 == res2:
                draw += 1
            ######## fin del for

        prob = win / run

        if prob <= 0.4:
            print("retirar")
            ## fold

        elif prob > 0.4 and prob <= 0.55:
            print("pasar")
            ## check

        elif prob > 0.55 and prob < 0.7:
            print("apuesta suave")
            ## raise debil

        elif prob > 0.7:
            print("apuesta duro")
            ## raise duro

        return prob

"""      
    def fold(prob):
        if prob <= 0.4:
            return 0
        return -1

    #monto es el dinero de charmi y apuesta lo que el usuario pago

    def call(self, monto, apuesta):
            if apuesta > monto:
                print("All in")

    #def check():#pasar

    #def raise_b():#apuesta suave

    #def raise_a():##apuesta full
"""