import Jugador
import Mazo
import Mesa
import Mano

mazo_poker = Mazo.Mazo()
mesa = Mesa.Mesa()
mazo_poker.mezclar()

class Juego:

    def __init__(self,charmi,usuario):
        self.charmi = charmi
        self.usuario = usuario

    def ciegas(self):
        print("Empezaremoos con las ciegas tipicas del juego")
        print("Yo sere la minima esta ocasion 50$")
        self.charmi.bote = (self.charmi.bote - 50)
        print("tu sere la maxima esta ocasion 100$")
        self.usuario.bote = (self.usuario.bote - 100)
        
    def preflop(self):
        self.usuario.recibir_mano(mazo_poker.repartir())
        self.charmi.recibir_mano(mazo_poker.repartir())
        self.usuario.recibir_mano(mazo_poker.repartir())
        self.charmi.recibir_mano(mazo_poker.repartir())
        print("")
        print("usuario 1: ",self.usuario.name,"   bote:",self.usuario.bote)
        self.usuario.mostrar_mano()
        print("")
        print("usuario 2: ",self.charmi.name,"   bote:",self.charmi.bote)
        self.charmi.mostrar_mano()

    #Segunda fase
    def flop(self):
        # Se quema una carta
        mesa.quemar(mazo_poker.repartir())
        mesa.recibir_mano(mazo_poker.repartir())
        mesa.recibir_mano(mazo_poker.repartir())
        mesa.recibir_mano(mazo_poker.repartir())
        
        print("Mesa")
        mesa.mostrar_mano()

    def turn(self):
        # Se quema una carta
        mesa.quemar(mazo_poker.repartir())
        mesa.recibir_mano(mazo_poker.repartir())

        print("Mesa")
        mesa.mostrar_mano()

    def river(self):
        # Se quema una carta
        mesa.quemar(mazo_poker.repartir())
        mesa.recibir_mano(mazo_poker.repartir())

        print("Mesa")
        mesa.mostrar_mano()

    def final(self):
        print("veremos quien gana")
        mano = Mano.hand(self.charmi.pasar_mano(),mesa.pasar_mano())
        mano.unir()
        #mano.mostrar()



    def ronda(self):

        mazo_poker.retornar(self.charmi.regresar())
        mazo_poker.retornar(self.usuario.regresar())

        mazo_poker.retornar(self.charmi.regresar())
        mazo_poker.retornar(self.usuario.regresar())

        mazo_poker.retornar(mesa.regresar())
        mazo_poker.retornar(mesa.regresar())
        mazo_poker.retornar(mesa.regresar())
        mazo_poker.retornar(mesa.regresar())
        mazo_poker.retornar(mesa.regresar())

        mazo_poker.retornar(mesa.qregresar())
        mazo_poker.retornar(mesa.qregresar())
        mazo_poker.retornar(mesa.qregresar())

        print("hola")
        #self.charmi.mostrar_mano()
        #self.usuario.mostrar_mano()
        #mesa.mostrar_mano()
        #mesa.mostrar_quemada()
        #mazo_poker.mostrar_nombres()
        mazo_poker.mezclar()
        