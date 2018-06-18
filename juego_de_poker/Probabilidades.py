class pro:

    def __init__(self,m):
        self.mano = m

    def prob(self):
        if self.mano == 10:
            probabilidad = 100 - 4 / 2598960 *100
            probabilidad = round(probabilidad, 3)
            return probabilidad

        elif self.mano == 9:
            probabilidad = 100 - 36 / 2598960 *100
            probabilidad = round(probabilidad, 3)
            return probabilidad

        elif self.mano == 8:
            probabilidad = 100 - 624 / 2598960 *100
            probabilidad = round(probabilidad, 3)
            return probabilidad

        elif self.mano == 6 or self.mano == 7:
            probabilidad = 100 - 3774 / 2598960 *100
            probabilidad = round(probabilidad, 3)
            return probabilidad

        elif self.mano == 5:
            probabilidad = 100 - 5108 / 2598960 *100
            probabilidad = round(probabilidad,3)
            return probabilidad

        elif self.mano == 4:
            probabilidad = 100 - 10200 / 2598960 *100
            probabilidad = round(probabilidad, 3)
            return probabilidad

        elif self.mano == 3:
            probabilidad = 100 - 54912 / 2598960 *100
            probabilidad = round(probabilidad, 3)
            return probabilidad

        elif self.mano == 2:
            probabilidad = 100 - 123552 / 2598960 *100
            probabilidad = round(probabilidad, 3)
            return probabilidad

        elif self.mano == 1:
            probabilidad = 100 - 1098240 / 2598960 *100
            probabilidad = round(probabilidad, 3)
            return probabilidad

        elif self.mano == 0:
            probabilidad = 100 - 1302540 / 2598960 *100
            probabilidad = round(probabilidad, 3)
            return probabilidad

    def probabilidad(self):
        if self.mano == 10:
            probabilidad = 4 / 2598960 *100
            probabilidad = round(probabilidad, 3)
            return probabilidad

        elif self.mano == 9:
            probabilidad = 36 / 2598960 *100
            probabilidad = round(probabilidad, 3)
            return probabilidad

        elif self.mano == 8:
            probabilidad = 624 / 2598960 *100
            probabilidad = round(probabilidad, 3)
            return probabilidad

        elif self.mano == 6 or self.mano == 7:
            probabilidad = 3774 / 2598960 *100
            probabilidad = round(probabilidad, 3)
            return probabilidad

        elif self.mano == 5:
            probabilidad = 5108 / 2598960 *100
            probabilidad = round(probabilidad,3)
            return probabilidad

        elif self.mano == 4:
            probabilidad = 10200 / 2598960 *100
            probabilidad = round(probabilidad, 3)
            return probabilidad

        elif self.mano == 3:
            probabilidad = 54912 / 2598960 *100
            probabilidad = round(probabilidad, 3)
            return probabilidad

        elif self.mano == 2:
            probabilidad = 123552 / 2598960 *100
            probabilidad = round(probabilidad, 3)
            return probabilidad

        elif self.mano == 1:
            probabilidad = 1098240 / 2598960 *100
            probabilidad = round(probabilidad, 3)
            return probabilidad

        elif self.mano == 0:
            probabilidad = 1302540 / 2598960 *100
            probabilidad = round(probabilidad, 3)
            return probabilidad

    def proba_aproximada(self,n):

        manopro=0

        while n>0:
            manopro = manopro + pro(n-1).probabilidad()
            n=n-1
        return manopro

    def propensa(self,n):

        mano = pro(n).probabilidad()

        propensas = mano*self.proba_aproximada(n)

        return propensas


        """
        while n>0:
            print("n",n)
     elif n==1:
            manopro = pro(n-1).prob() + pro(n-2).prob()
            return manopro

            n= n-1
        return manopro
        """

       