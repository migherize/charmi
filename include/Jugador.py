import Mazo

class Jugador:

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
    
    def apuesta(self):
        opcion = int(input(print("""Acaba de obtener sus dos cartas
                       1)Desea ir: 
                       2)Desea subir: 
                       3)Desea all in 
                       4)Desea retirarse: 

               """)))
        if opcion == 1:
            print("pasar a flop")
            return True

        elif opcion == 2:
            #charmi iguala si le conviene
            print("subio")
            return True

        elif opcion == 3:
            #charmi no va si no le conviene
            #Se le paga al usuario
            print("fin de ronda")
            return False

        elif opcion == 4:
            # Pagar a charmi
            print("fin de ronda")
            return False
