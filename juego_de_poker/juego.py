import sys 
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from sala_juego import Ui_sala 
from Mazo import Mazo, Carta
from imgcarta import imagen
from Jugador import Jugador
from Charmi import Charmi
from Mano import hand
from Mesa import Mesa 
from Probabilidades import pro

mazo_poker = Mazo()
mazo_poker.mezclar()
mesa = Mesa()
usuario = Jugador("user",1000)
charmi	= Charmi("charmi",1000)
minima = 50
maxima = 100
apuesta = 0
ronda = 0
altura = 0
quemada = 0

qtCreatorFile = "inicio.ui" # Nombre del archivo aquí. 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile) 

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow): 
	
	def __init__(self): 
		QtWidgets.QMainWindow.__init__(self) 
		Ui_MainWindow.__init__(self) 
		self.setupUi(self) 
		self.setWindowTitle("Poker Charmi")	#Cambia el nombre a la pagina principal
		self.showMaximized()
		self.btn_jugar.clicked.connect(self.abrir)
		self.btn_salir.clicked.connect(self.salir)

	#Funcion para que el boton me lleve a la otra ventana.
	def abrir (self):
		self.ventana = QtWidgets.QMainWindow()
		self.ui = Ui_sala()
		self.ui.setupUi(self.ventana)
		self.ventana.show()	#Para ver
		
		user = self.usuario.text()
		self.ui.bienvenido.setText(str("Hola " + user + " Bienvenido"))
		self.ui.user.setText(str(user))
		
		global minima,maxima, apuesta

		usuario.bote = usuario.bote - minima
		charmi.bote = charmi.bote - maxima

		apuesta = minima + maxima

		minima,maxima = maxima,minima

		self.ui.bote_user.setText(str(usuario.bote))
		self.ui.bote_charmi.setText(str(charmi.bote))
		self.ui.bote_mesa.setText(str(apuesta))

		usuario.recibir_mano(mazo_poker.repartir())
		charmi.recibir_mano(mazo_poker.repartir())
		usuario.recibir_mano(mazo_poker.repartir())
		charmi.recibir_mano(mazo_poker.repartir())

		U1 = imagen(usuario.mano[0].valor,usuario.mano[0].palo)
		C1 = imagen(charmi.mano[0].valor,charmi.mano[0].palo)
		U2 = imagen(usuario.mano[1].valor,usuario.mano[1].palo)
		C2 = imagen(charmi.mano[1].valor,charmi.mano[1].palo)

		self.ui.c1U.setStyleSheet(str(U1.mostrar_imagen()))
		self.ui.c1C.setStyleSheet(str(C1.mostrar_imagen()))
		self.ui.c2U.setStyleSheet(str(U2.mostrar_imagen()))
		self.ui.c2C.setStyleSheet(str(C2.mostrar_imagen()))

		self.ui.btn_pasar.clicked.connect(self.paso)
		self.ui.btn_subir.clicked.connect(self.subir)
		self.ui.btn_Allin.clicked.connect(self.allin)
		self.ui.btn_retirarse.clicked.connect(self.retirarse)
	
	def paso(self):
		
		global ronda

		print("paso",ronda)

		if ronda  == 0:
			self.flop()
		elif ronda == 1:
			self.turn()
		elif ronda == 2:
			self.river()
		elif ronda == 3:
			self.ganador()
		elif ronda == 4:
			self.reinicio()

	def subir(self):
		print("subio")

		global apuesta

		subida = self.ui.subida.value()
		apuesta = apuesta + subida
		self.ui.bote_mesa.setText(str(apuesta))
		
		#si acepta
		charmi.bote = charmi.bote - subida
		apuesta = apuesta + subida
		self.ui.bote_charmi.setText(str(charmi.bote))
		self.ui.bote_mesa.setText(str(apuesta))

		if ronda  == 0:
			self.flop()
		elif ronda == 1:
			self.turn()
		elif ronda == 2:
			self.river()
		elif ronda == 3:
			self.ganador()
		elif ronda == 4:
			self.reinicio()
	
	def retirarse(self):
		print("se retiro")

		global apuesta

		charmi.bote = charmi.bote + apuesta
		apuesta = 0

		self.ui.bote_charmi.setText(str(charmi.bote))
		self.ui.bote_mesa.setText(str(apuesta))

		if ronda  == 0:
			self.reinicio()
		elif ronda == 1:
			self.reinicio()
		elif ronda == 2:
			self.reinicio()
		elif ronda == 3:
			self.reinicio()
		elif ronda == 4:
			self.reinicio()


	def allin(self):
		print("allin")

		global apuesta

		apuesta = apuesta + usuario.bote
		self.ui.bote_mesa.setText(str(apuesta))

		all_in = usuario.bote		
		usuario.bote = 0
		self.ui.bote_user.setText(str(usuario.bote))

		#si acepta
		charmi.bote = charmi.bote - all_in
		apuesta = apuesta + charmi.bote
		self.ui.bote_charmi.setText(str(charmi.bote))
		self.ui.bote_mesa.setText(str(apuesta))

		if ronda  == 0:
			self.flop()
		elif ronda == 1:
			self.turn()
		elif ronda == 2:
			self.river()
		elif ronda == 3:
			self.ganador()
		elif ronda == 4:
			self.reinicio()

	def salir(self):
		sys.exit(app.exec_())

	def flop(self):

		global ronda,altura,quemada

		mesa.quemar(mazo_poker.repartir()) #quemada

		mesa.recibir_mano(mazo_poker.repartir())
		mesa.recibir_mano(mazo_poker.repartir())
		mesa.recibir_mano(mazo_poker.repartir())

		M1 = imagen(mesa.mesa[0].valor,mesa.mesa[0].palo)
		M2 = imagen(mesa.mesa[1].valor,mesa.mesa[1].palo)
		M3 = imagen(mesa.mesa[2].valor,mesa.mesa[2].palo)

		self.ui.c1M.setStyleSheet(str(M1.mostrar_imagen()))
		self.ui.c2M.setStyleSheet(str(M2.mostrar_imagen()))
		self.ui.c3M.setStyleSheet(str(M3.mostrar_imagen()))

		altura = 3
		quemada = 1

		ronda=ronda +1
		print("ronda ", ronda)

		mesa.mostrar_mano()

	def turn(self):

		global ronda,altura,quemada

		mesa.quemar(mazo_poker.repartir())#Quemada

		mesa.recibir_mano(mazo_poker.repartir())

		M4 = imagen(mesa.mesa[3].valor,mesa.mesa[3].palo)

		self.ui.c4M.setStyleSheet(str(M4.mostrar_imagen()))

		altura = altura + 1
		quemada = quemada + 1

		print("Hola turn")

		ronda=ronda +1
		print("ronda ", ronda)

		mesa.mostrar_mano()

	def river(self):

		global ronda,altura,quemada

		mesa.quemar(mazo_poker.repartir()) #Quemada 3

		mesa.recibir_mano(mazo_poker.repartir())

		M5 = imagen(mesa.mesa[4].valor,mesa.mesa[4].palo)

		self.ui.c5M.setStyleSheet(str(M5.mostrar_imagen()))

		altura = altura + 1
		quemada = quemada + 1

		print("hola river")
		ronda=ronda +1
		print("ronda ", ronda)

		mesa.mostrar_mano()

	def ganador(self):

		global ronda,apuesta
		
		ronda = ronda +1

		mano_charmi = hand(charmi.pasar_mano(),mesa.pasar_mano())
		mano_charmi.unir()
		
		resultado = mano_charmi.manos()

		pc = pro(resultado)
		print("Resultado jugador",resultado,"Probabilidad",pc.prob())

		mano_usuario = hand(usuario.pasar_mano(),mesa.pasar_mano())
		mano_usuario.unir()
		
		resultado2 = mano_usuario.manos()

		pu = pro(resultado2)
		print("Resultado jugador",resultado2,"Probabilidad",pu.prob())

		if resultado < resultado2:
			self.ui.resultado.setText(str("Gano Jugador"))
			usuario.bote = usuario.bote + apuesta
			self.ui.bote_user.setText(str(usuario.bote))
			apuesta = 0
			self.ui.bote_mesa.setText(str(apuesta))

		elif resultado > resultado2:
			self.ui.resultado.setText(str("Gano Charmi"))
			charmi.bote = charmi.bote + apuesta
			self.ui.bote_charmi.setText(str(charmi.bote))
			apuesta = 0
			self.ui.bote_mesa.setText(str(apuesta))
		else:
			self.ui.resultado.setText(str("empate"))
			charmi.bote = charmi.bote + (apuesta/2)
			self.ui.bote_charmi.setText(str(charmi.bote))
			usuario.bote = usuario.bote + (apuesta/2)
			self.ui.bote_user.setText(str(usuario.bote))
			apuesta = 0
			self.ui.bote_mesa.setText(str(apuesta))

	def reinicio(self):

		global ronda,altura,quemada

		for a in range(0,2):
			mazo_poker.retornar(charmi.regresar())
			mazo_poker.retornar(usuario.regresar())

		for b in range(0,altura):
			mazo_poker.retornar(mesa.regresar())
		
		for c in range(0,quemada):
			mazo_poker.retornar(mesa.qregresar())

		if usuario.bote == 0:
			self.ui.bienvenido.setText(str("Has perdido"))
		elif charmi.bote == 0:
			self.ui.bienvenido.setText(str("Me ganaste FELICIDADES"))

		mazo_poker.mezclar()
		ronda = 0
		self.abrir()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = MyApp() 
	window.show() 
	sys.exit(app.exec_())
