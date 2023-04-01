class nodopila(object):
    def __init__(self,info = None, sig = None):
        self.info = info
        self.sig = sig

class Pila(object):
    def __init__(self, encima = None , tamanio = 0):
        self.encima = encima
        self.tamanio = tamanio

    def apilar(pila, dato):
        nodo= nodopila()
        nodo.info = dato
        nodo.sig = pila.encima
        pila.encima = nodo

    def desapilar(pila):
        x = pila.encima.info
        pila.encima = pila.encima.sig
        return x
    def pila_vacia(pila):
        return pila.encima is not None

primera = Pila()
segunda = Pila()
tercera = Pila()

def

