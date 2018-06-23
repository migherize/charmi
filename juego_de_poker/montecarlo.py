import random
from Jugador import Jugador
import Mazo
import Mesa
import Mano
import Charmi
from desempate import parametros

mesa = Mesa.Mesa()
lusuario = Jugador("prueba",1000)

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

        run = 5000
        lose = 0
        win = 0
        draw = 0

        for it in range(0, run):

            self.mano_charmi
            mazo = self.mazo
            mazo.mezclar()
            suma=0
            suma2=0

            lusuario.recibir_mano(mazo.repartir())
            lusuario.recibir_mano(mazo.repartir())

            mesa.quemar(mazo.repartir())
            mesa.recibir_mano(mazo.repartir())
            mesa.recibir_mano(mazo.repartir())
            mesa.recibir_mano(mazo.repartir())
            mesa.quemar(mazo.repartir())
            mesa.recibir_mano(mazo.repartir())
            mesa.quemar(mazo.repartir())
            mesa.recibir_mano(mazo.repartir())
            
            lmesa=mesa.mesa

            # Mano de charmi
            mano1 = Mano.hand(self.mano_charmi, lmesa)
            mano1.unir()

            res1 = mano1.manos()

            # Mano de usuario
            mano2 = Mano.hand(lusuario.pasar_mano(), lmesa )
            mano2.unir()
            res2 = mano2.manos()

            if res1 < res2:
                lose += 1

            elif res1 > res2:
                win += 1

            elif res1 == res2:
                empate1 = parametros(self.mano_charmi, lmesa)
                empate1.unir()
                a,b,c,d = empate1.ganar(res1)
                empate2 = parametros(lusuario.pasar_mano(), lmesa)
                empate2.unir()
                a2,b2,c2,d2 = empate2.ganar(res2)
                
                if b == b2:
                    for a in range(0,2):
                        suma = suma + d[a].valor
                    for b in range(0,2):
                        suma2 = suma2 + d2[b].valor
                    if suma==suma2:
                        draw += 1
                    elif suma>suma2:
                        win +=1
                    elif suma2>suma:
                        lose+1

            for a in range(0,2):
                mazo.retornar(lusuario.regresar())

            for b in range(0,5):
                mazo.retornar(mesa.regresar())
        
            for c in range(0,3):
                mazo.retornar(mesa.qregresar())

            ######## fin del for

        prob = win / run

        if prob <= 0.15:
            print("retirar")
            ## fold

        elif prob > 0.15 and prob <= 0.38:
            print("pasar")
            ## check

        elif prob > 0.38 and prob < 0.4:
            print("apuesta suave")
            ## raise debil

        elif prob > 0.4:
            print("apuesta duro")
            ## raise duro

        return prob