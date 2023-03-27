class Animal:
    def __init__(self, eucariota, heterotrofo, multicelular):
        self.eucariota = eucariota
        self.heterotrofo = heterotrofo
        self.multicelular = multicelular

    def moverse(self):
        print("Me puedp mover")
    
    def alimentarse(self, comida):
        print("Me puedo alimentar de", comida)
    
    def reproducirse(self, pareja):
        print("Me puedo reproducir con", pareja)


class Viviparo(Animal):
    def __init__(self, eucariota, heterotrofo, multicelular, vientre):
        # atributos heredados
        super().__init__(eucariota, heterotrofo, multicelular)
        #nuevos atributos
        self.gestacion = vientre
    
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
    def __init__(self, eucariota, heterotrofo, multicelular, huevo):
        # atributos heredados
        super().__init__(eucariota, heterotrofo, multicelular)
        #nuevos atributos
        self.gestacion = huevo
    
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
    def __init__(self, eucariota, heterotrofo, multicelular, vientre, mamas):
        # atributos heredados
        super().__init__(eucariota, heterotrofo, multicelular, vientre)
        #nuevos atributos
        self.mamas = mamas
    
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
    def __init__(self, eucariota, heterotrofo, multicelular, vientre, mamas, pelo):
        # atributos heredados
        super().__init__(eucariota, heterotrofo, multicelular, vientre, mamas)
        #nuevos atributos
        self.pelo = pelo
    
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
    def __init__(self, eucariota, heterotrofo, multicelular, huevo, pico):
        # atributos heredados
        super().__init__(eucariota, heterotrofo, multicelular, huevo)
        #nuevos atributos
        self.pico = pico
    
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
    def __init__(self, eucariota, heterotrofo, multicelular, huevo, pico):
        # atributos heredados
        super().__init__(eucariota, heterotrofo, multicelular, huevo)
        #nuevos atributos
        self.pico = pico
    
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


