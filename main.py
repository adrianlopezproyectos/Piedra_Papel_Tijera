import random
from random import *

#Unicamente existen 3 valores.
a="piedra"
b="papel"
c="tijera"

#Cada uno se muestra en pantalla, para que el usuario elija la opcion que desee.
print("Hola soy Bob! vamos a jugar piedra, papel o tijera")
print("a - piedra")
print("b - papel")
print("c - tijera")
user=input("escribe la letra que eliges: ")

#Defino la funcion para el usuario y la ejecuto.
def eleccion(a,b,c,user):
  if user == "a":
    print("elegiste",a)
  elif user == "b":
    print("elegiste",b)
  else:
    print("elegiste",c)
eleccion(a,b,c,user)

#Ahora defino la funcion para la maquina.
def maquina(a,b,c):
  pc= choice("abc")
  if pc == "a":
    Bob = a
    print("Bob eligió",Bob)
  if pc == "b":
    Bob = b
    print("Bob eligió",Bob)
  if pc == "c":
    Bob = c
    print("Bob eligió",Bob)
  return pc
Bob = maquina(a,b,c)

#Por ultimo la funcion que compara ambas opciones y determina quien es el ganador.
def compara(Bob,user):
  if Bob == user: 
    print("Es un empate!")
  else:
     if (Bob == "a" and user == "c") or \
        (Bob == "b" and user == "a") or \
        (Bob == "c" and user == "b"):
        print("Bob gana esta ronda!")
     else:
      print("Tu ganaste!")
compara(Bob,user)
