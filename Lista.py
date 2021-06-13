from Nodo import *
import sys
import os



class Lista(object):

    def __init__(self):
        self.inicio = None
        self.fin = None

    def agregarInicio(self, nombre, apellido, telefono):
        if(self.validar()):
            nuevo = Nodo(nombre, apellido, telefono, None, None)
            self.inicio = nuevo
            self.fin = nuevo
        else:
            nuevo = Nodo(nombre, apellido, telefono, None, self.inicio)
            self.inicio.anterior = nuevo
            self.inicio = nuevo

    def agregar(self):
        nombre = input("Digite nombre: ")
        apellido = input("Digite apellido: ")
        telefono = input("Digite telefono: ")

        temp = self.inicio
        while temp != None:
            if temp.telefono == telefono:
                print("▬"* 75)
                print("\nError, El telefono " + telefono + " ya existe.")
                return

            temp = temp.siguiente

        self.agregarInicio(nombre, apellido, telefono)
        print("▬"*75)
        print("\nEl contacto se ha guardado exitosamente")
    def imprimir(self):
        temp = self.inicio
        while temp != None:
            print("\nNombre:\n"+temp.nombre +
                  "\nApellido:\n"+temp.apellido +
                  "\nTelefono:\n"+temp.telefono)
            temp = temp.siguiente

    def validar(self):
        if(self.inicio == None):
            return True
        return False

    def buscar(self,numero):
        print("▬"*75)
        numero = input("Ingrese el numero a buscar:\n ")

        temp = self.inicio
        while temp != None:
            if (temp.telefono == numero):

                print("Nombre:  "+temp.nombre +
                      "\nApellido:  "+temp.apellido +
                      "\nTelefono:  "+temp.telefono)
                break
            
            elif(temp ==self.fin):
                opc = 0

                while opc != 5:
                    print("■\t\t\tNo se ha encontrado el numero")
                    print("■\t\t\tDesea añadirlo?")
                    print("1.Si.\n")
                    print("2.No.\n")

                    opc = int(input())

                    if opc == 1:
                        nombre = input("Escriba el nombre: ")
                        apellido = input("Escriba el apellido: ")
                        self.agregarInicio(nombre,apellido,numero)
                        print("▬"*75)
                        print("\n■\t\t\tContacto guardado exitosamente")
                        return
                    elif opc == 2:
                        return
                break
            temp = temp.siguiente



           
            
                
