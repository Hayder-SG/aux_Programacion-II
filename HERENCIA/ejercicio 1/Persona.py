class Persona:
    def __init__(self, nombre, apellido, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
    
class Cliente(Persona):
    def __init__(self, nombre, apellido, ci, nroCliente, nroCuenta):
        super().__init__(nombre, apellido, ci)
        self.nroCliente = nroCliente
        self.nroCuenta = nroCuenta
class Jefe(Persona):
    def __init__(self, nombre, apellido, ci,sucursal, tipo):
        super().__init__(nombre, apellido, ci)
        self.sucursal = sucursal
        self.tipo = tipo

# main
persona = Persona("Juan", "Perez", "12345678")
cliente = Cliente("Maria", "Gomez", "87654321", "C001", "CUENTA001")
jefe = Jefe("Luis", "Martinez", "11223344", "Sucursal 1", "Gerente")
print(f"Persona: {persona.nombre} {persona.apellido}, CI: {persona.ci}")
print(f"Cliente: {cliente.nombre} {cliente.apellido}, CI: {cliente.ci}, Nro Cliente: {cliente.nroCliente}, Nro Cuenta: {cliente.nroCuenta}")
print(f"Jefe: {jefe.nombre} {jefe.apellido}, CI: {jefe.ci}, Sucursal: {jefe.sucursal}, Tipo: {jefe.tipo}")

