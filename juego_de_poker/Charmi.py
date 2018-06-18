import Jugador
import Mazo
import Mesa
import Mano

class Charmi:

    def __init__(self,n,bote):
        self.name = n
        self.bote = bote
        self.mano = []

    def mostrar_mano(self):
        for c in self.mano:
            print("     cartas: ",c)

    def recibir_mano(self,c):
        self.mano.append(c)

    def regresar(self):
        return self.mano.pop()

    def pasar_mano(self):
        mano = self.mano
        return mano
