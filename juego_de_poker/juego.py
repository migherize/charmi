import sys 
from PyQt5 import uic, QtWidgets
from sala_juego import Ui_sala 

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

	#Funcion para que el boton me lleve a la otra ventana.
	def abrir (self):
		self.ventana = QtWidgets.QMainWindow()
		self.ui = Ui_sala()
		self.ui.setupUi(self.ventana)
		self.ventana.show()	#Para ver
		user = self.usuario.text()
		self.ui.bienvenido.setText(str("Hola " + user + " Bienvenido"))
		self.ui.user.setText(str(user))


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = MyApp() 
	window.show() 
	sys.exit(app.exec_())
