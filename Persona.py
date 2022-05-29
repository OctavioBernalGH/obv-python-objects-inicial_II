class Persona():
    "Se crean los atributos de clase privados."
    __dni: ""
    __nombre: ""
    __apellidos: ""
    __edad: 0
    __sueldo: 0.0
    __añosAntiguedad = 0

    "Se define el constructor de clase con todos los atributos."

    def __init__(self, dni, nombre, apellidos, edad, sueldo, añosAntiguedad):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = edad
        self.__sueldo = sueldo
        self.__añosAntiguedad = añosAntiguedad

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    @property
    def sueldo(self):
        return self.__sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self.__sueldo = sueldo

    @property
    def añosAntiguedad(self):
        return self.__añosAntiguedad

    @añosAntiguedad.setter
    def añosAntiguedad(self, añosAntiguedad):
        self.__añosAntiguedad = añosAntiguedad

    def __str__(self):
        return "\nUsuario:\n- Identificador: {}\n- Nombre: {}\n- Apellidos: {}\n- Edad: {}\n- Sueldo: {}\n- Años de Antiguedad: {}".format(
            self.__dni, self.__nombre, self.__apellidos, self.__edad, self.__sueldo, self.__añosAntiguedad)
