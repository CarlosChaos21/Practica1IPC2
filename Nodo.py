class Nodo(object):

    nombre = ""
    apellido = ""
    telefono = ""
    anterior = None
    siguiente = None

    def __init__(self, nombre, apellido, telefono, anterior, siguiente):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.anterior = anterior
        self.siguiente = siguiente

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getTelefono(self):
        return self.telefono

    def getAnterior(self):
        return self.anterior

    def getSiguiente(self):
        return self.siguiente
    
