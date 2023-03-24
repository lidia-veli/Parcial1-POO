class CuentaBancaria:
    def __init__(self, id, nombre, fecha_apertura, num_cuenta, saldo):
        self.id = id
        self.nombre = nombre
        self.id = id
        self.fecha_apertura = fecha_apertura
        self.num_cuenta = num_cuenta
        self.saldo = saldo

    def __str__(self):
        return f'ID: {self.id} - Saldo: {self.saldo}'

    def ingresar(self, importe):
        self.saldo += importe
    
    def retirar(self, importe):
        if self.saldo >= importe:
            self.saldo -= importe
    
    def transferir(self, importe, cuenta):
        if self.saldo >= importe:
            self.retirar(importe)
            cuenta.ingresar(importe)
