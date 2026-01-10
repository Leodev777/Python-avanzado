"""
Crea una clase "cuenta bancaria" con atributos como numero de cuenta y saldo implementando metodos
para depositar y rettirar dinero, y muestre el saldo actual.
"""


class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo =100): # Saldo en cuenta
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Deposito exitoso: {cantidad}. Saldo actual: {self.saldo}")
    
    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"Retiro exitoso: {cantidad}. Saldo actual: {self.saldo}")
        else:
            print("Fondos insuficientes para el retiro.")
    
    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")
    
    # Ejemplo de uso

cuenta = CuentaBancaria(100)

cuenta.depositar(400)

cuenta.retirar(500)

cuenta.mostrar_saldo()
