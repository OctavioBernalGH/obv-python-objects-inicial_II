class Inmueble():
    __altura = 0
    __anchura = 0
    __profundidad = 0
    __peso = 0

    def __init__(self, altura, anchura, profundidad, peso):
        self.__altura = altura
        self.__anchura = anchura
        self.__profundidad = profundidad
        self.__peso = peso

    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura):
        self.__altura = altura
    @property
    def anchura(self):
        return self.__anchura
    @anchura.setter
    def anchura(self, anchura):
        self.__anchura = anchura
    @property
    def profundidad(self):
        return self.__profundidad
    @profundidad.setter
    def profundidad(self, profundidad):
        self.__profundidad = profundidad
    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    def __str__(self):
        return "\nAltura: {} \nAnchura: {} \nProfundidad: {} \nPeso: {}".format(self.__altura, self.__anchura, self.__profundidad, self.__peso)






