import Mano
import Mazo
import Mano
import Probabilidades
import Charmi
import montecarlo

mazo = Mazo.Mazo()

manochar = []
manochar.append(mazo.repartirc(0))
manochar.append(mazo.repartirc(13))

montecarlos = montecarlo.probabilidades(mazo,manochar)
probabilidad = montecarlos.montecarlo()

print("probb: ",probabilidad)


import Jugador
import Mazo
import Mesa
import Mano
import Charmi
import montecarlo



"""
mazo1 = Mazo.Mazo()
mazo2 = Mazo.Mazo()
mazo3 = Mazo.Mazo()
mazo4 = Mazo.Mazo()


#Escalera
lista = []
lista.append(mazo.repartirc(0))
lista.append(mazo.repartirc(14))

list = []
list.append(mazo.repartirc(13))
list.append(mazo.repartirc(11))
list.append(mazo.repartirc(28))
list.append(mazo.repartirc(42))
list.append(mazo.repartirc(4))

#poker
lista1 = []
lista1.append(mazo.repartirc(0))
lista1.append(mazo.repartirc(13))

list1 = []
list1.append(mazo.repartirc(26))
list1.append(mazo.repartirc(39))
list1.append(mazo.repartirc(28))
list1.append(mazo.repartirc(42))
list1.append(mazo.repartirc(4))


#trio
lista3 = []
lista3.append(mazo.repartirc(0))
lista3.append(mazo.repartirc(13))

list3 = []
list3.append(mazo.repartirc(26))
list3.append(mazo.repartirc(34))
list3.append(mazo.repartirc(28))
list3.append(mazo.repartirc(42))
list3.append(mazo.repartirc(4))

#doblepar
lista4 = []
lista4.append(mazo.repartirc(0))
lista4.append(mazo.repartirc(13))

list4 = []
list4.append(mazo.repartirc(27))
list4.append(mazo.repartirc(40))
list4.append(mazo.repartirc(28))
list4.append(mazo.repartirc(43))
list4.append(mazo.repartirc(5))
"""

#mazo.mostrar_mazo()
#mazo.mostrar_nombres()

"""

"""
"""
lista = []
lista.append(mazo.repartirc(12))
lista.append(mazo.repartirc(11))

list = []
list.append(mazo.repartirc(23))
list.append(mazo.repartirc(22))
list.append(mazo.repartirc(0))
list.append(mazo.repartirc(45))
list.append(mazo.repartirc(46))
"""
"""
lista = []
lista.append(mazo.repartirc(12))
lista.append(mazo.repartirc(24))

list = []
list.append(mazo.repartirc(22))
list.append(mazo.repartirc(36))
list.append(mazo.repartirc(47))
list.append(mazo.repartirc(42))
list.append(mazo.repartirc(4))

lista = []
lista.append(mazo.repartirc(2))
lista.append(mazo.repartirc(9))

list = []
list.append(mazo.repartirc(25))
list.append(mazo.repartirc(23))
list.append(mazo.repartirc(38))
list.append(mazo.repartirc(12))
list.append(mazo.repartirc(10))


print("C1",lista[0])
print("C2",lista[1])
print("M1",list[0])
print("M2",list[1])
print("M3",list[2])
print("M4",list[3])
print("M5",list[4])

mano = Mano.hand(lista3,list3)
mano.unir()
res = mano.manos()
p = Probabilidades.pro(res)
proba = p.prob()

print("res:",res)
print("p",proba)

#resultado = mano.manos()

#print("res",resultado)

"""



