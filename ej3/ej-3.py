class CuentaBancaria:
    def __init__(self, id, nombre, fecha_apertura, num_cuenta, saldo):
        self.id = id
        self.nombre = nombre
        self.id = id
        self.fecha_apertura = fecha_apertura
        self.num_cuenta = num_cuenta
        self.saldo = saldo

    def ingresar(self, importe):
        self.saldo += importe
    
    def retirar(self, importe):
        if self.saldo >= importe:
            self.saldo -= importe
        else:
            print('Saldo insuficiente')
    
    def transferir(self, importe, cuenta):
        if self.saldo >= importe:
            self.retirar(importe) #retiramos el importe de nuestra cuenta
            cuenta.ingresar(importe) # lo ingresamos en la cuenta de destino


class PlazoFijo(CuentaBancaria):
    def __init__(self, id, nombre, fecha_apertura, num_cuenta, saldo, fecha_vencimiento):
        super().__init__(id, nombre, fecha_apertura, num_cuenta, saldo) #atributos heredados
        self.fecha_vencimiento = fecha_vencimiento # nuevo atributo
    
    #método heredado
    def ingresar(self, importe): # igual que la clase padre
        super().ingresar(importe)
    
    #método modificado
    def retirar(self, importe, fecha_actual):
        if fecha_actual > self.fecha_vencimiento:
            self.saldo -= importe - 0.05*importe  # 5% de comisión
        else:
            print('No se puede retirar dinero de la cuenta antes de la fecha de vencimiento')
    
    #método modificado
    def transferir(self, importe, cuenta, fecha_actual):
        if fecha_actual > self.fecha_vencimiento:
            self.saldo -= importe - 0.05*importe  # 5% de comisión
            cuenta.ingresar(importe)
        else:
            print('No se puede retirar dinero de la cuenta antes de la fecha de vencimiento')


class CuentaVIP(CuentaBancaria):
    def __init__(self, id, nombre, fecha_apertura, num_cuenta, saldo, deuda_max):
        super().__init__(id, nombre, fecha_apertura, num_cuenta, saldo) #atributos heredados
        self.deuda_max = deuda_max # nuevo atributo
    
    #método heredado
    def ingresar(self, importe):
        super().ingresar(importe)
    
    #método modificado
    def retirar(self, importe):
        if self.saldo - importe >= -self.deuda_max: #si no nos pasamos del límite de deuda
            self.saldo -= importe
        else:
            print('No se puede retirar más dinero de la cuenta')
    
    #método modificado
    def transferir(self, importe, cuenta):
        if self.saldo - importe >= -self.deuda_max: #si no nos pasamos del límite de deuda
            self.saldo -= importe   #quitamos el importe de nuestra cuenta
            cuenta.ingresar(importe)  #lo ingresamos en la cuenta de destino
        else:
            print('No se puede retirar más dinero de la cuenta')

