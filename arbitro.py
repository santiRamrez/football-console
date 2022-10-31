from persona import Persona

class Arbitro(Persona):
    def __init__(self, rut, nombre, antiguedad):
        super().__init__(rut, nombre)
        self.__antiguedad = antiguedad
        
    def __str__(self):
        return(f'{super().__str__()} \nAntiguedad: {self.__antiguedad}')

    def setAntiguedad(self, a):
        self.__antiguedad = a;

    def getAntiguedad(self):
        return self.__antiguedad;
