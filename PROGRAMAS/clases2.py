class Coche():
    def __init__(self):
        self.largochasis=250
        self.anchochasis=120
        self.__ruedas = 4
        self.enmarcha = False

    def arrancar(self,arrancamos):
        self.enmarcha = arrancamos
        if(self.enmarcha):
            check = self.chequeo()
        if(self.enmarcha and check ):
            return "el coche esta en marcha"
        elif (self.enmarcha and check ==False):
            return "algo a ido mal con el coche, no podemos arrancar"
        else:
            return "el coche esta detenido"
    def estado(self):
        print("El coche tiene", self.__ruedas,"ruedas , un ancho",self.anchochasis,"y un largo de ", self.largochasis)
    def chequeo(self):
        print("Chequeo Interno")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"
        if(self.gasolina == "ok" and self.aceite=="ok" and self.puertas == "cerradas"):
            return True
        else:
            return False

Micoche = Coche()
print(Micoche.arrancar(True))
Micoche.estado()
print("(-----------------------SEGUNDO OBJETO-----------------------------)")
Micoche2 = Coche()
print(Micoche2.arrancar(False))
Micoche2.estado()