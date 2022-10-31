# Import clases
from partido import Partido
from jugador import Jugador
from arbitro import Arbitro

import re # Modulo de expresiones regulares

# Validaciones
def validaNombre(a):
  try:
    print(f'Favor ingrese {a} (2 palabras):')
    val = input().upper()
    regex = re.compile(r'^[A-Z]{2,20}\s[A-Z]{2,20}$')

    if regex.match(val):
      return val
    else:
      print('Favor ingrese nombre y apellido, solo 2 palabras')
      return validaNombre(a) 

  except:
    print('Hubo un error en el ingreso')
    return validaNombre(a)    

def validaNumero(a):
  try:
    print(f'Favor ingrese {a}:')
    val = int(input())
    if val > 0 and val < 100:
      return val
    else:
      print("Favor ingrese solo numeros")
      return validaNumero()
  except:
    return validaNumero() 

def validaDni():
  try:
    val = input("Favor ingrese rut: ")
    myRegex = r'^\d{1,2}.\d{3}.\d{3}-(k|K|\d)'
    if re.match(myRegex, val):
      return val
    else:
      print('--- Favor ingrese rut valido con puntos y guión ---')
      return validaDni()
  except:
    print('Favor ingrese rut valido con puntos y guión')
    return validaDni()

def validaOpcion():
  try:
    op = int(input('Ingrese una opción del menú: '))
    if op > 0 and op < 7: 
      return op
    else: 
       print("opción fuera de rango") 
       return validaOpcion()
  except:
      print("Debe ingresar un valor numérico")
      return validaOpcion()

# Menu
def menu():
    print(f"\nMenú principal")
    print("1 Registrar Partido")
    print("2 Asignar Arbitro")
    print("3 Agregar Jugador")
    print("4 Eliminar Jugador")
    print("5 Listar Jugadores por Equipos")
    print("6 Salir\n")

# Run the program
game = ""
start = False

while True:
    menu()

    op = validaOpcion()

    if op == 6:
        break
    elif op == 1: #Registrar Partido --> numero partido - nombre estadio - nombre arbitro
        game = Partido(validaNumero('numero de partido'), validaNombre('nombre del estadio'), validaNombre('nombre arbitro'))
        start = True

    elif op ==2: #Asignar Arbitro --> rut - nombre - antiguedad
        if start:
          print(game.asignarArbitro(validaDni(), validaNombre('nombre arbitro'), validaNumero('años de antiguedad')))

    elif op == 3: #Agregar Jugador --> rut, nombre, equipo, numeroCamiseta
      if start:
        dni = validaDni()
        nombre = validaNombre('nombre jugador')
        equipo = validaNombre('nombre equipo')
        numero = validaNumero('numero camiseta')
        print(game.agregarJugadorPartido(dni, nombre, equipo, numero)) if game.agregarJugadorPartido(dni, nombre, equipo, numero) else print('-- Los equipos están completos --')
      else:
        print('-- Por favor inicie un partido primero --')

    
    elif op == 4: #Eliminar Jugador --> rut, equipo
        print('-- Ingrese Rut Del Jugador --')
        rut = validaDni()
        print('-- Ingrese Equipo del Jugador --')
        equipo = validaNombre()
        print(game.eliminarJugadorPartido(rut, equipo)) 
    
    elif op == 5: #Listar jugadores por equipo
      if start:
        game.desplegarJugadores()
    
  

