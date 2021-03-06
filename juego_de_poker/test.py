import unittest
from Jugador import Jugador
from Charmi import Charmi
from Jugar import Juego
from Mazo import Mazo,Carta
from Mano import hand
from Probabilidades import pro
from desempate import parametros
from montecarlo import probabilidades

class NotificacionesTest(unittest.TestCase):

    def test_montecarlos(self):

    	print("Test de monte carlos")

    	mazo = Mazo()

    	usuario = []

    	usuario.append(mazo.repartirc(12))
    	usuario.append(mazo.repartirc(25))

    	for a in usuario:
    		print(a)

    	m_carlos=probabilidades(mazo,usuario)
    	prob_carlos = m_carlos.montecarlo()

    def test_jugador(self):

    	print("Test de crear un jugador")

    	nombre = 'Jugador'
    	usuario = Jugador(nombre,1000)
    	print("usuario 1: ", usuario.name, "   bote:", usuario.bote,"\n")

    def test_Charmi(self):

    	print("Test de crear a charmi")
    	usuario = Charmi("Charmi",1000)
    	print("charmi: ", usuario.name, "   bote:", usuario.bote,"\n")

    def test_juego(self):

    	print("Test de simulacion de inicializacion del juego")

    	nombre = 'Jugador'
    	usuario = Jugador(nombre, 1000)
    	charmi = Charmi("Charmi", 1000)
    	juego = Juego(charmi,usuario)
    	print("usuario : ", juego.usuario.name, "   bote:", juego.usuario.bote)
    	print("Charmi: ", juego.charmi.name, "   bote:", juego.charmi.bote,"\n")

    def test_mazo(self):

    	print("Test del mazo de cartas del juego")

    	mazo = []
    	lista_Palos = ["nada", "Corazones", "Picas", "Diamantes", "Tréboles"]
    	lista_naipes = ["nada", "As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jota", "Reina", "Rey"]

    	for palo in range(1,5):
    		for valor in range(1, 14):
    			mazo.append(Carta(palo, valor))

    	print("Mazo:")
    	for cartas in mazo:
    		print(cartas)

    #Evalua la mano del jugador y la mesa

    print("Posibles Manos de poker \n")

    def test_hand_Full(self):
        mazo = Mazo()

        usuario = []

        usuario.append(mazo.repartirc(1))
        usuario.append(mazo.repartirc(13))

        mesa = []

        mesa.append(mazo.repartirc(25))
        mesa.append(mazo.repartirc(34))
        mesa.append(mazo.repartirc(28))
        mesa.append(mazo.repartirc(42))
        mesa.append(mazo.repartirc(4))

        evaluar = hand(usuario,mesa)
        evaluar.unir()
        res = evaluar.manos()

        print("Mano de Full")

        for c in usuario:
            print(c)

        for c in mesa:
            print(c)

        p = pro(res)
        proba = p.prob()

        if res == 6:
            print("Usuario tiene Mano de FullHouse,  probabilidad de ganar",proba,"%\n")

        else:
            print("No tiene FullHouse")

    def test_hand_poker(self):
        mazo = Mazo()

        usuario = []

        usuario.append(mazo.repartirc(0))
        usuario.append(mazo.repartirc(12))

        mesa = []

        mesa.append(mazo.repartirc(24))
        mesa.append(mazo.repartirc(36))
        mesa.append(mazo.repartirc(28))
        mesa.append(mazo.repartirc(42))
        mesa.append(mazo.repartirc(5))

        evaluar = hand(usuario,mesa)
        evaluar.unir()
        res = evaluar.manos()

        print("Mano de poker")

        for c in usuario:
            print(c)

        for c in mesa:
            print(c)

        p = pro(res)
        proba = p.prob()

        if res == 8:
            print("Usuario tiene Mano de poker,  probabilidad de ganar",proba,"%\n")

        else:
            print("No tiene poker")

    def test_hand_color(self):
        mazo = Mazo()

        usuario = []

        usuario.append(mazo.repartirc(0))
        usuario.append(mazo.repartirc(4))

        mesa = []

        mesa.append(mazo.repartirc(8))
        mesa.append(mazo.repartirc(39))
        mesa.append(mazo.repartirc(2))
        mesa.append(mazo.repartirc(5))
        mesa.append(mazo.repartirc(24))

        evaluar = hand(usuario,mesa)
        evaluar.unir()
        res = evaluar.manos()

        print("Mano de color")

        for c in usuario:
            print(c)

        for c in mesa:
            print(c)

        p = pro(res)
        proba = p.prob()

        if res == 5:
            print("Usuario tiene Mano de color,  probabilidad de ganar",proba,"%\n")

        else:
            print("No tiene color")


    def test_hand_escalera(self):
        mazo = Mazo()

        usuario = []

        usuario.append(mazo.repartirc(1))
        usuario.append(mazo.repartirc(3))

        mesa = []

        mesa.append(mazo.repartirc(26))
        mesa.append(mazo.repartirc(25))
        mesa.append(mazo.repartirc(14))
        mesa.append(mazo.repartirc(39))
        mesa.append(mazo.repartirc(29))

        evaluar = hand(usuario,mesa)
        evaluar.unir()
        evaluar.mostrar()
        res = evaluar.manos()

        propensa = evaluar.propensa_escalera()
        print("pro",propensa)

        print("Mano de escalera")

        p = pro(res)
        proba = p.prob()

        if res == 4:
            print("Usuario tiene Mano de escalera,  probabilidad de ganar",proba,"%\n")

        else:
            print("No tiene escalera",proba)

        desempates = parametros(usuario,mesa)
        desempates.unir()
        print("carga")

        n,cm,cartasA,s_cartasA = desempates.ganar(res)

        print("n",n)
        print("cm",cm)

        print("jugada")
        for a in cartasA:
            print (a)
        print("resto")
        for b in s_cartasA:
            print(b)
    
    def test_hand_trio(self):
        mazo = Mazo()

        usuario = []

        usuario.append(mazo.repartirc(0))
        usuario.append(mazo.repartirc(12))

        mesa = []

        mesa.append(mazo.repartirc(24))
        mesa.append(mazo.repartirc(34))
        mesa.append(mazo.repartirc(28))
        mesa.append(mazo.repartirc(42))
        mesa.append(mazo.repartirc(5))

        evaluar = hand(usuario,mesa)
        evaluar.unir()
        res = evaluar.manos()

        p = pro(res)
        proba = p.prob()

        if res == 3:
            print("Usuario tiene Mano de trio,  probabilidad de ganar",proba,"%\n")

        else:
            print("No tiene trio")

    def test_hand_doble_par(self):
        mazo = Mazo()

        usuario = []

        usuario.append(mazo.repartirc(1))
        usuario.append(mazo.repartirc(13))

        mesa = []

        mesa.append(mazo.repartirc(26))
        mesa.append(mazo.repartirc(34))
        mesa.append(mazo.repartirc(28))
        mesa.append(mazo.repartirc(42))
        mesa.append(mazo.repartirc(4))

        evaluar = hand(usuario,mesa)
        evaluar.unir()
        res = evaluar.manos()

        p = pro(res)
        proba = p.prob()

        print("mano de doble par")
        for c in usuario:
            print(c)

        for c in mesa:
            print(c)


        if res == 2:
            print("Usuario tiene Mano de doble par,  probabilidad de ganar",proba,"%\n")

        else:
            print("No tiene doble par")

    def test_hand_par(self):
        mazo = Mazo()

        usuario = []

        usuario.append(mazo.repartirc(0))
        usuario.append(mazo.repartirc(12))

        mesa = []

        mesa.append(mazo.repartirc(25))
        mesa.append(mazo.repartirc(34))
        mesa.append(mazo.repartirc(28))
        mesa.append(mazo.repartirc(42))
        mesa.append(mazo.repartirc(6))

        evaluar = hand(usuario,mesa)
        evaluar.unir()
        res = evaluar.manos()

        p = pro(res)
        proba = p.prob()

        if res == 1:
            print("Usuario tiene Mano de par,  probabilidad de ganar",proba,"%\n")

        else:
            print("No tiene par")

if __name__ == '__main__':
    unittest.main()