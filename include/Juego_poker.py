import Jugador
import Charmi
import Jugar

print("         !!!!BIENVENIDOS A JUGAR CON CHARMI!!!!      ")
print("Juguemos un torneo en el cual los dos tendremos un bote de 1000$")
inicio = input("¿Deseas Inscribirte? (si/no):")

while inicio != "si" and inicio != "no":
    inicio = input("Responde si o no porfavor. ¿Deseas Inscribirte? (si/no):")

if(inicio == "si"):
    print("Introduzca su Nombre: ")
    nombre = input()
    usuario = Jugador.Jugador(nombre, 1000)
    charmi = Charmi.Charmi("charmi",1000)
    print("Bienvenido ", usuario.name)

    while  ( usuario.bote != 0) and (charmi.bote != 0):
        partida = Jugar.Juego(charmi,usuario)

        #Ciegas minima y maxima
        partida.ciegas()

        #Primera Etapa Preeflop
        partida.preflop()
        retirar = partida.usuario.apuesta()
        
        if(retirar):

            #Segunda etapa
            partida.flop()
            retirar2 = partida.usuario.apuesta()

            if (retirar2):

                # Tercera etapa
                partida.turn()
                retirar3 = partida.usuario.apuesta()

                if (retirar3):

                    # Cuarta etapa
                    partida.river()
                    retirar4 = partida.usuario.apuesta()

                    if(retirar4):
                        # Final
                        partida.final()
                        partida.ronda()

                    else:
                        break


                else:
                    break


            else:
                break

        else:
            break
        
       # partida.ronda()
        

elif(inicio == "no"):
        print("Hasta Luego")

