class Arbol :

    def __init__(self) :
      self.pagina = []
      self.hijos = []
      self.pad = None

    def insertar(self, dato, min, max, padre = None) :

        tmp = []
        self.pad = padre

        if len(self.pagina) == max :

            self.pagina.append(dato)
            self.pagina.sort()

            for i in range(0, max/2) :
                tmp.append(self.pagina.pop())
            dato = self.pagina.pop()

            if self.pad == None :

                self.pad = Arbol()
                self.pad.pagina = []
                self.pad.hijos = []
                self.pad.insertar(dato, min, max)
                self.pad.hijos.append(self)

                arboltmp = Arbol()
                arboltmp.pagina = []
                arboltmp.hijos = []

                for a in len(tmp) :
                    arboltmp.insertar(tmp.pop(), min, max)

                self.pad.hijos.append(arboltmp)
                return self.pad

            print "Ud quiere insertar el dato " + str(dato) + " pero lapagina ya esta llena"

        else :

            self.pagina.append(dato)
            self.pagina.sort()
            return self

class ArbolB :

    def __init__(self, d) :
        self.dmax = 2*d
        self.dmin = d
        self.raiz = Arbol()

    def insertar(self, dato) :
        self.raiz = self.raiz.insertar(dato, self.dmin, self.dmax)

    def __repr__(self) :
        return str(self.raiz.pagina)