import os
from os import system, name
from Lista import *
metodo = Lista()


def mainMenu():
    print("▬"*75)
    print("\n■\t\t\tMenu Principal")
    print("■\t\t1. Ingrese Nuevo Contacto")
    print("■\t\t2. Buscar Contacto")
    print("■\t\t3. Visualizar agenda")
    print("▬"*75)
    opcion = input("\n■\t>>Ingrese opcion: ")

    if opcion == "1":
        clear()
        print("▬"*75)
        print("■\t\t\tNuevo Contacto: ")
        
        metodo.agregar()
        mainMenu()
    if opcion == "2":
        clear()
        metodo.buscar(None)
       
    if opcion == "3":
        metodo.imprimir()
        mainMenu()


    else: 
        mainMenu()



def clear():
    if name == 'nt':
        _ = system('cls')
       
mainMenu()
#hi
