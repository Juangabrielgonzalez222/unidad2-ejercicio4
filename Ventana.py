class Ventana:
    __titulo=0
    __xSupIzquierdo=0
    __ySupIzquierdo=0
    __xInfDerecho=0
    __yInfDerecho=0
    def __init__(self,titulo='',xSupIzquierdo=0,ySupIzquierdo=0,xInfDerecho=500,yInfDerecho=500):
        self.__titulo=titulo
        self.__xSupIzquierdo=xSupIzquierdo
        self.__ySupIzquierdo=ySupIzquierdo
        self.__xInfDerecho=xInfDerecho
        self.__yInfDerecho=yInfDerecho
    def getTitulo(self):
        return self.__titulo
    def alto(self):
        return self.__yInfDerecho-self.__ySupIzquierdo
    def ancho(self):
        return self.__xInfDerecho-self.__xSupIzquierdo
    def moverDerecha(self,cantidad=0):
        if self.__xInfDerecho+cantidad<=500:
            self.__xSupIzquierdo=self.__xSupIzquierdo+cantidad
            self.__xInfDerecho=self.__xInfDerecho+cantidad
        else:
            print('No se pudo realizar la operacion, el limite es 500')
    def bajar(self,cantidad=0):
        if self.__yInfDerecho+cantidad<=500:
            self.__ySupIzquierdo=self.__ySupIzquierdo+cantidad
            self.__yInfDerecho=self.__yInfDerecho+cantidad
        else:
            print('No se pudo realizar la operacion, el limite es 500')
    def moverIzquierda(self,cantidad=0):
        if self.__xSupIzquierdo-cantidad>=0:
            self.__xSupIzquierdo=self.__xSupIzquierdo-cantidad
            self.__xInfDerecho=self.__xInfDerecho-cantidad
        else:
            print('No se pudo realizar la operacion,el limite es 0')
    def subir(self,cantidad=0):
        if self.__ySupIzquierdo-cantidad>=0:
            self.__ySupIzquierdo=self.__ySupIzquierdo-cantidad
            self.__yInfDerecho=self.__yInfDerecho-cantidad
        else:
            print('No se pudo realizar la operacion,el limite es 0')
    def mostrar(self):
        print('Titulo:{}\nVertice Superior Izquierdo:({},{})\nVertice Inferior Derecho:({},{})'.format(self.__titulo,self.__xSupIzquierdo,self.__ySupIzquierdo,self.__xInfDerecho,self.__yInfDerecho))
    def test(self):
        ventanaT=Ventana('Prueba',0,30,200,250)
        ventanaT.mostrar()
        print('Alto:',ventanaT.alto())
        print('Ancho',ventanaT.ancho())
        print('Titulo',ventanaT.getTitulo())
        ventanaT.subir(10)
        ventanaT.moverIzquierda(10)
        ventanaT.moverDerecha(10)
        ventanaT.bajar(20)
        ventanaT.mostrar()