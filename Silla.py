from Inmueble import Inmueble


class Silla(Inmueble):
    __patas = 0
    __respaldo = False

    def __init__(self, altura, anchura, profundidad, peso, patas, respaldo):
        Inmueble.__init__(self,altura, anchura, profundidad, peso)
        self.__patas = patas
        self.__respaldo = respaldo

    @property
    def patas(self):
        return self.__patas

    @patas.setter
    def patas(self, patas):
        self.__patas = patas

    @property
    def respaldo(self):
        return self.__respaldo

    @respaldo.setter
    def respaldo(self, respaldo):
        self.__respaldo = respaldo

    def __str__(self):
        return Inmueble.__str__(self) + "\nPatas: {} \nRespaldo: {}".format(self.__patas, self.__respaldo)

