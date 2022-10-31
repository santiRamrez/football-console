from re import A
from arbitro import Arbitro;
from jugador import Jugador;

class Partido:
    def __init__(self, numPartido, estadio, referi):
        self.__numPartido = numPartido
        self.__estadio = estadio
        self.__referi = referi
        self.__listEq1 = []
        self.__listEq2 = []
        
    def __str__(self):
        return(f'Nº Partido:{self.__numPartido} \nEstadio:{self.__estadio}')

    def setNumPartido(self, numPartido):
        self.__numPartido = numPartido;

    def setEstadio(self, estadio):
        self.__estadio = estadio;

    def setReferi(self, referi):
        self.__referi = referi;
    
    def getNumPartido(self):
        return self.__numPartido;

    def getEstadio(self):
        return self.__estadio;

    def getReferi(self):
        return self.__referi;
    
    def getListEq1(self):
       return self.__listEq1

    def getListEq2(self):
       return self.__listEq2
  
    def asignarArbitro(self, rut, nombre, antiguedad):
      a = Arbitro(rut, nombre, antiguedad)
      self.__referi = a
      return f'Arbitro {nombre} agregado exitosamente'
    
    def pickList(self, li1, li2, equipo):
      if len(li1) > 0:
          eq1 = li1[0].getEquipo().upper()
          if eq1 == equipo.upper():
            return li1 
          else:
            return li2

    def agregarJugadorPartido(self, rut, nombre, equipo, numeroCamiseta):
      jugador = Jugador(rut, nombre, equipo, numeroCamiseta)

      #For default, it adds to the list1 the first player
      if len(self.getListEq1()) == 0 and len(self.getListEq2()) == 0:
        self.getListEq1().append(jugador)

      theList = self.pickList(self.getListEq1(), self.getListEq2(), equipo)
      
      #If there are available positions and this list is according to the team typed by the user 
      #check if the player is not already in
      if len(theList) < 11: 
          for p in theList:
            if p.getRut() == jugador.getRut():
              return f'-- El jugador {jugador.getNombre()} ya existe!'

          theList.append(jugador)
          return f'El jugador {nombre} fue agregado al equipo {equipo}'
      else:
        return f'Está completo el equipo compadre :('
      
    def eliminarJugadorPartido(self, rut, equipo):
      list1 = self.getListEq1()
      list2 = self.getListEq2()
      if len(list1) == 0 and len(list2) == 0:
        return f'No hay jugadores para eliminar'
      else:
        for j in range(0, len(list1), 1):
          if rut.upper() == list1[j].getRut().upper() and equipo.upper() == list1[j].getEquipo().upper():
            list1.pop(j)
            return f'Jugador rut: {rut} fue borrado exitosamente'

        for k in range(0, len(list2), 1):
          if rut.upper() == list2[k].getRut().upper() and equipo.upper() == list2[k].getEquipo().upper():
            list2.pop(k)
            return f'Jugador rut: {rut} fue borrado exitosamente'
        
        return False

      
    def desplegarJugadores(self):
      list1 = self.getListEq1()
      list2 = self.getListEq2()

      if len(list1) == 0 and len(list2) == 0:
        return f'No hay jugadores para Mostrar :('
      else:
        if len(list1) > 0:
          print(f'-- Jugadores del Equipo {list1[0].getEquipo().upper()} --')
          for j in range(0, len(list1), 1):
            print(list1[j])

        if len(list2) > 0:
          print(f'\n-- Jugadores del Equipo {list2[0].getEquipo().upper()} --')
          for k in range(0, len(list2), 1):
            print(list2[k])


