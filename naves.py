import csv

class Nave:
    def __init__(self, nombre, largo, tripulacion,cantidad):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.cantidad = cantidad
    
    def __str__(self):
        return "{} {} {} {}".format(self.nombre,self.largo,self.tripulacion,self.cantidad)

    def to_dict(self):
        return {'nombre': self.nombre,'largo': self.largo,'tripulacion': self.tripulacion,'cantidad' : self.cantidad}
class Naves:
    lista=[]
    def crear_nave(self):
        with open (naves.csv, newline= '\n') as fichero:
            reader = csv.reader(fichero, delimiter = ';')
            for nombre,largo,tripulacion,cantidad in reader:
                nave = Nave(nombre,largo,tripulacion,cantidad)

    @staticmethod
    def buscar(slef):
        for nave in Naves.lista:
            if nave.args = args
            return nave.args
        elif 