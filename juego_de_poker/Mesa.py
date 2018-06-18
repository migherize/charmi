class Mesa:

    def __init__(self):
        self.mesa = []
        self.quemada = []
        self.apuesta = 0

    def mostrar_mano(self):
        for c in self.mesa:
            print("     carta : ",c)

    def mostrar_quemada(self):
        for c in self.quemada:
            print("     cartas: ",c)

    def ciegas(self,min,max):
        self.apuesta= (self.apuesta + min + max)

    def apuesta(self,bote_pre):
        self.apuesta = self.apuesta + self.bote_pre

    def recibir_mano(self, c):
        self.mesa.append(c)

    def pasar_mano(self):
        mesa = self.mesa
        return mesa

    def quemar(self, c):
        self.quemada.append(c)

    def regresar(self):
        return self.mesa.pop()

    def qregresar(self):
        return self.quemada.pop()