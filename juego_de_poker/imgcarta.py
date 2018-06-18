class imagen:

	def __init__(self,valor,palo):
	 	self.v = valor
	 	self.p = palo

	def mostrar_carta(self):
		print("cartav:",self.v)
		print("cartap:",self.p)

	def mostrar_imagen(self):
		#cartas de Corazon
		if self.v == 1 and self.p == 1:
			img1 = "border-image: url(:/mazo/AC.jpg);"
			return(img1)
		elif self.v == 2 and self.p == 1:
			img1 = "border-image: url(:/mazo/2C.jpg);"
			return(img1)
		elif self.v == 3 and self.p == 1:
			img1 = "border-image: url(:/mazo/3C.jpg);"
			return(img1)
		elif self.v == 4 and self.p == 1:
			img1 = "border-image: url(:/mazo/4C.jpg);"
			return(img1)
		elif self.v == 5 and self.p == 1:
			img1 = "border-image: url(:/mazo/5C.jpg);"
			return(img1)
		elif self.v == 6 and self.p == 1:
			img1 = "border-image: url(:/mazo/6C.jpg);"
			return(img1)
		elif self.v == 7 and self.p == 1:
			img1 = "border-image: url(:/mazo/7C.jpg);"
			return(img1)
		elif self.v == 8 and self.p == 1:
			img1 = "border-image: url(:/mazo/8C.jpg);"
			return(img1)
		elif self.v == 9 and self.p == 1:
			img1 = "border-image: url(:/mazo/9C.jpg);"
			return(img1)
		elif self.v == 10 and self.p == 1:
			img1 = "border-image: url(:/mazo/10C.jpg);"
			return(img1)
		elif self.v == 11 and self.p == 1:
			img1 = "border-image: url(:/mazo/JC.jpg);"
			return(img1)
		elif self.v == 12 and self.p == 1:
			img1 = "border-image: url(:/mazo/QC.jpg);"
			return(img1)
		elif self.v == 13 and self.p == 1:
			img1 = "border-image: url(:/mazo/KC.jpg);"
			return(img1)
    	#elif self.v == 13 and self.p == 1:
		#	img1 = "border-image: url(:/mazo/KC.jpg);"
		#	return(img1)

		#Cartas Pica
		elif self.v == 1 and self.p == 2:
			img1 = "border-image: url(:/mazo/ASP.jpg);"
			return(img1)
		elif self.v == 2 and self.p == 2:
			img1 = "border-image: url(:/mazo/2P.jpg);"
			return(img1)
		elif self.v == 3 and self.p == 2:
			img1 = "border-image: url(:/mazo/3P.jpg);"
			return(img1)
		elif self.v == 4 and self.p == 2:
			img1 = "border-image: url(:/mazo/4P.jpg);"
			return(img1)
		elif self.v == 5 and self.p == 2:
			img1 = "border-image: url(:/mazo/5P.jpg);"
			return(img1)
		elif self.v == 6 and self.p == 2:
			img1 = "border-image: url(:/mazo/6P.jpg);"
			return(img1)
		elif self.v == 7 and self.p == 2:
			img1 = "border-image: url(:/mazo/7P.jpg);"
			return(img1)
		elif self.v == 8 and self.p == 2:
			img1 = "border-image: url(:/mazo/8P.jpg);"
			return(img1)
		elif self.v == 9 and self.p == 2:
			img1 = "border-image: url(:/mazo/9P.jpg);"
			return(img1)
		elif self.v == 10 and self.p == 2:
			img1 = "border-image: url(:/mazo/10P.jpg);"
			return(img1)
		elif self.v == 11 and self.p == 2:
			img1 = "border-image: url(:/mazo/JP.jpg);"
			return(img1)
		elif self.v == 12 and self.p == 2:
			img1 = "border-image: url(:/mazo/QP.jpg);"
			return(img1)
		elif self.v == 13 and self.p == 2:
			img1 = "border-image: url(:/mazo/KP.jpg);"
			return(img1)

		#Cartas Diamante

		elif self.v == 1 and self.p == 3:
			img1 = "border-image: url(:/mazo/AD.jpg);"
			return(img1)
		elif self.v == 2 and self.p == 3:
			img1 = "border-image: url(:/mazo/2D.jpg);"
			return(img1)
		elif self.v == 3 and self.p == 3:
			img1 = "border-image: url(:/mazo/3D.jpg);"
			return(img1)
		elif self.v == 4 and self.p == 3:
			img1 = "border-image: url(:/mazo/4D.jpg);"
			return(img1)
		elif self.v == 5 and self.p == 3:
			img1 = "border-image: url(:/mazo/5D.jpg);"
			return(img1)
		elif self.v == 6 and self.p == 3:
			img1 = "border-image: url(:/mazo/6D.jpg);"
			return(img1)
		elif self.v == 7 and self.p == 3:
			img1 = "border-image: url(:/mazo/7D.jpg);"
			return(img1)
		elif self.v == 8 and self.p == 3:
			img1 = "border-image: url(:/mazo/8D.jpg);"
			return(img1)
		elif self.v == 9 and self.p == 3:
			img1 = "border-image: url(:/mazo/9D.jpg);"
			return(img1)
		elif self.v == 10 and self.p == 3:
			img1 = "border-image: url(:/mazo/10D.jpg);"
			return(img1)
		elif self.v == 11 and self.p == 3:
			img1 = "border-image: url(:/mazo/JD.jpg);"
			return(img1)
		elif self.v == 12 and self.p == 3:
			img1 = "border-image: url(:/mazo/QD.jpg);"
			return(img1)
		elif self.v == 13 and self.p == 3:
			img1 = "border-image: url(:/mazo/KD.jpg);"
			return(img1)

		#Carta Trebol

		elif self.v == 1 and self.p == 4:
			img1 = "border-image: url(:/mazo/AT.jpg);"
			return(img1)
		elif self.v == 2 and self.p == 4:
			img1 = "border-image: url(:/mazo/2T.jpg);"
			return(img1)
		elif self.v == 3 and self.p == 4:
			img1 = "border-image: url(:/mazo/3T.jpg);"
			return(img1)
		elif self.v == 4 and self.p == 4:
			img1 = "border-image: url(:/mazo/4T.jpg);"
			return(img1)
		elif self.v == 5 and self.p == 4:
			img1 = "border-image: url(:/mazo/5T.jpg);"
			return(img1)
		elif self.v == 6 and self.p == 4:
			img1 = "border-image: url(:/mazo/6T.jpg);"
			return(img1)
		elif self.v == 7 and self.p == 4:
			img1 = "border-image: url(:/mazo/7T.jpg);"
			return(img1)
		elif self.v == 8 and self.p == 4:
			img1 = "border-image: url(:/mazo/8T.jpg);"
			return(img1)
		elif self.v == 9 and self.p == 4:
			img1 = "border-image: url(:/mazo/9T.jpg);"
			return(img1)
		elif self.v == 10 and self.p == 4:
			img1 = "border-image: url(:/mazo/10T.jpg);"
			return(img1)
		elif self.v == 11 and self.p == 4:
			img1 = "border-image: url(:/mazo/JT.jpg);"
			return(img1)
		elif self.v == 12 and self.p == 4:
			img1 = "border-image: url(:/mazo/QT.jpg);"
			return(img1)
		elif self.v == 13 and self.p == 4:
			img1 = "border-image: url(:/mazo/KT.jpg);"
			return(img1)