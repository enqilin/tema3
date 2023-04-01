class nodo(object):
    def __init__(self):
        self.info = None
        self.sif = None
class datoPolinomio(object):
    def __init__(self,valor, termino):
        self.valor=valor
        self.termino = termino

class Polinomio(object):
    def __init__(self, termino_mayor = None,grado = -1):
        self.termino_mayor=termino_mayor
        self.grado = grado
    def agregar_termino(polinomio,termino , valor):

        aux=nodo()
        dato = datoPolinomio(valor,termino)
        aux.info=dato
        if(termino > polinomio.grado):
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino
        else:
            actual =polinomio.termino_mayor
            while(actual.sig is not None and termino < actual.sig.info.termino):
                actual =actual.sig
            aux.sig = actual.sig
            actual.sig = aux

    def modificar_valor(polinomio,termino):
        aux = polinomio.termino_mayor
        while(aux is not None and aux.info.termino !=termino):
            aux =aux.sig
        aux.info.valor =ValueError

    def obtener_valor(polinomio,termino):
        aux = polinomio.termino_mayor
        while(aux is not None and aux.info.termino >termino):
            aux =aux.sig
        if(aux is not None and aux.info.termino == termino):
            return aux.info.valor
        else:
            return 0



    def restar(polinomio1 ,polinomio2):
        paux = Polinomio()
        mayor=polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
        for i in range(0, mayor.grado+1):
            total = polinomio1.obtener_valor(i) - polinomio2.obtener_valor(i)
            if (total !=0):
                paux.agregar_termino(i,total)
        return paux
    
    def dividir(polinomio1 ,polinomio2):
        paux = Polinomio()
        pol1 = polinomio1.termino_mayor
        while(pol1 is not None):
            pol2 = polinomio2.termino_mayor
            while (pol2 is not None):
                termino = pol1.info.termino -pol2.info.termino
                valor = pol1.info.valor - pol2.info.valor
                if (paux.obtener_valor(termino)!=0):
                    valor+= paux.obtener_valor(termino)
                    paux.modificar_valor(termino)
                else:
                    paux.agregar_termino(termino,valor)
                pol2 = pol2.sig
            pol1 = pol1.sig
        return paux
    def eliminar_un_termino(polinomio,termino):
        paux = polinomio.termino_mayor
        while (paux is not None and paux.info.termino > termino):
            paux = paux.sig
            if (paux is not None and paux.info.termino == termino):
                paux =paux.sig
    def polinomio_existe_termino(polinomio,termino):
        aux = polinomio.termino_mayor
        while(aux is not None and aux.inof.termino > termino):
            aux = aux.sig
            if (aux is not None and aux.info.termino == termino):
                return aux
            else:
                return None