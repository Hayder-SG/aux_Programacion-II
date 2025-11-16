class FondosInsuficientesException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


class CuentaBancaria:
    def __init__(self, numeroCuenta, titular, saldo):
        self.numeroCuenta = numeroCuenta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo.")
        self.saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")

    def retirar(self, monto):
        if monto > self.saldo:
            raise FondosInsuficientesException(
                f"Fondos insuficientes. Intentó retirar {monto}, saldo actual {self.saldo}"
            )
        self.saldo -= monto
        print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")

    def mostrarInfo(self):
        print("=== Información de la Cuenta ===")
        print(f"Número de Cuenta: {self.numeroCuenta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")
        print("================================")


    # Crear cuenta
cuenta = CuentaBancaria("12345", "Juan Pérez", 1000)
cuenta.mostrarInfo()
print("\n--- Pruebas de Depósito ---")
try:
    cuenta.depositar(300)
    cuenta.depositar(-50)
except ValueError as e:
    print("ERROR:", e)
print("\n--- Pruebas de Retiro ---")
try:
    cuenta.retirar(200)
    cuenta.retirar(2000)  
except FondosInsuficientesException as e:
    print("ERROR:", e)
cuenta.mostrarInfo()