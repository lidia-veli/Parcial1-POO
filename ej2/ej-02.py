class Animal:
    
    # atributos de clase
    celulas = 'eucariota'
    organismo = 'multicelular'

    def moverse(self):
        print("Me puedp mover")
    
    def alimentarse(self, comida):
        print("Me puedo alimentar de", comida)
    
    def reproducirse(self, pareja):
        print("Me puedo reproducir con", pareja)


class Viviparo(Animal):
    
    # atributos de clase
    gestacion = 'vientre'
    
    # métodos heredados
    def moverse(self):
        super().moverse()
    
    def alimentarse(self, comida):
        super().alimentarse(comida)
    
    def reproducirse(self, pareja):
        super().reproducirse(pareja)
    
    #métodos nuevos
    def gestar(self):
        print("Mis crías se desarrollan en", self.gestacion)


class Oviparo(Animal):
    
    # atributos de clase
    gestacion = 'huevo'
    
    # métodos heredados
    def moverse(self):
        super().moverse()
    
    def alimentarse(self, comida):
        super().alimentarse(comida)
    
    def reproducirse(self, pareja):
        super().reproducirse(pareja)
    
    #métodos nuevos
    def poner_huevos(self):
        print("Mis crías se desarrollan en", self.gestacion)


class Mamifero(Viviparo):
    
    # atributos de clase
    mamas = 'glándulas mamarias'
    
    # métodos heredados
    def moverse(self):
        super().moverse()
    
    def alimentarse(self, comida):
        super().alimentarse(comida)
    
    def reproducirse(self, pareja):
        super().reproducirse(pareja)
    
    def gestar(self):
        super().gestar()
    
    # métodos nuevos
    def amamantar(self):
        print('Puedo amamantar a mis crías')


class Gato(Mamifero):
    
    # atributos de instancia
    def __init__(self, pelo):
        self.pelo = pelo # tipo de pelo
    
    # métodos heredados
    def moverse(self):
        super().moverse()
    
    def alimentarse(self, comida):
        super().alimentarse(comida)
    
    def reproducirse(self, pareja):
        super().reproducirse(pareja)
    
    def gestar(self):
        super().gestar()
    
    def amamantar(self):
        super().amamantar()
    
    # métodos nuevos
    def maullar(self):
        print('Miau miau')

class Ornitorrinco(Oviparo):

    # atributo de clase
    pico = 'pico plano'
    
    # métodos heredados
    def moverse(self):
        super().moverse()
    
    def alimentarse(self, comida):
        super().alimentarse(comida)
    
    def reproducirse(self, pareja):
        super().reproducirse(pareja)
    
    def poner_huevos(self):
        super().poner_huevos()
    
    # métodos nuevos
    def picar(self):
        print('Puedo picar a mis enemigos')

class Pollo(Oviparo):
    
    # atributo de clase
    pico = 'pico corto'

    #atrivutos de instancia
    def __init__(self, plumas):
        self.plumas = plumas # tipo de plumas
    
    # métodos heredados
    def moverse(self):
        super().moverse()
    
    def alimentarse(self, comida):
        super().alimentarse(comida)
    
    def reproducirse(self, pareja):
        super().reproducirse(pareja)
    
    def poner_huevos(self):
        super().poner_huevos()
    
    # métodos nuevos
    def piar(self):
        print('Pio pio')


