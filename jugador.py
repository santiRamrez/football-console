from persona import Persona

class Jugador(Persona):
    def __init__(self, rut, nombre, equipo, numeroCamiseta):
        super().__init__(rut, nombre)
        self.__equipo = equipo
        self.__numeroCamiseta = numeroCamiseta
        
    def __str__(self):
        return(f'{super().__str__()} \nEquipo: {self.__equipo} \nNumero Camiseta:{self.__numeroCamiseta}')

    def setEquipo(self, eq):
        self.__equipo = eq;

    def setNumCamiseta(self, numCamiseta):
        self.__numeroCamiseta = numCamiseta;

    def getEquipo(self):
        return self.__equipo;

    def getNumCamiseta(self):
        return self.__numeroCamiseta;