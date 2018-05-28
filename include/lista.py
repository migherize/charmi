import Mano
import Mazo

mazo =Mazo.Mazo()
#mazo.mostrar_mazo()

"""
#Escalera
lista = []
lista.append(mazo.repartirc(0))
lista.append(mazo.repartirc(14))

list = []
list.append(mazo.repartirc(12))
list.append(mazo.repartirc(11))
list.append(mazo.repartirc(28))
list.append(mazo.repartirc(42))
list.append(mazo.repartirc(4))
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
"""

lista = []
lista.append(mazo.repartirc(30))
lista.append(mazo.repartirc(17))

list = []
list.append(mazo.repartirc(32))
list.append(mazo.repartirc(38))
list.append(mazo.repartirc(26))
list.append(mazo.repartirc(31))
list.append(mazo.repartirc(5))

print("C1",lista[0])
print("C2",lista[1])
print("M1",list[0])
print("M2",list[1])
print("M3",list[2])
print("M4",list[3])
print("M5",list[4])

#mazo.mostrar_mazo()

mano = Mano.hand(lista,list)
mano.unir()
manos = mano.color()
if manos:
    print("si")
else:
    print("no")
