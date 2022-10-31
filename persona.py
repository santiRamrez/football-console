class Persona:
    def __init__(self, rut, nombre):
        self.__rut = rut
        self.__nombre = nombre
        
    def __str__(self):
        return(f'Rut:{self.__rut} \nNombre:{self.__nombre}')

    def setRut(self, rut):
        self.__rut = rut;

    def setNombre(self, nombre):
        self.__nombre = nombre;

    def getRut(self):
        return self.__rut;

    def getNombre(self):
        return self.__nombre;
    
