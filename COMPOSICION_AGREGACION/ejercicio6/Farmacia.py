class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
class Medicamento(Producto):
    def __init__(self, nombre, precio, stock, caducidad, tipo):
        super().__init__(nombre, precio, stock)
        self.caducidad = caducidad
        self.tipo = tipo
    
    def mostrar_informacion(self):
        print("===============================")
        print(f"\tNombre: {self.nombre}")
        print(f"\tPrecio: {self.precio}")
        print(f"\tStock: {self.stock}")
        print(f"\tCaducidad: {self.caducidad}")
        print(f"\tTipo: {self.tipo}")
        print("===============================")

class Higiene(Producto):
    def __init__(self, nombre, precio, stock, marca, tipo):
        super().__init__(nombre, precio, stock)
        self.marca = marca
        self.tipo = tipo
    def mostrar_informacion(self):
        print("===============================")
        print(f"\tNombre: {self.nombre}")
        print(f"\tPrecio: {self.precio}")
        print(f"\tStock: {self.stock}")
        print(f"\tMarca: {self.marca}")
        print(f"\tTipo: {self.tipo}")
        print("===============================")

class Farmacia:
    def __init__(self, nombre, lugar):
        self.nombre = nombre
        self.lugar = lugar
        self.medicamentos = []
        self.higiene = []
    
    def mostrar_productos(self):
        print("\nMedicamentos:")
        for medicamento in self.medicamentos:
            medicamento.mostrar_informacion()
        print("Higiene:")
        for higiene in self.higiene:
            higiene.mostrar_informacion()
        
    
    def agregar_producto(self, producto):
        self.productos.append(producto)


class Registro:
    def __init__(self, farmacia):
        self.farmacia = farmacia
        
    def agregar_medicamento(self, medicamento):
        self.farmacia.medicamentos.append(medicamento)
        
    def agregar_higiene(self, higiene):
        self.farmacia.higiene.append(higiene)

med1 = Medicamento("Paracetamol", 5, 100, "2022-12-31", "Analgesico")
med2 = Medicamento("Ibuprofeno", 10, 50, "2022-12-31", "Analgesico")

hi1 = Higiene("Desodorante", 15, 20, "Colgate", "Higiene personal")
hi2 = Higiene("Shampoo", 20, 10, "Ballerina", "Higiene personal")

farmacia = Farmacia("Mi Farmacia", "Calle 123")
registro = Registro(farmacia)

registro.agregar_medicamento(med1)
registro.agregar_medicamento(med2)

registro.agregar_higiene(hi1)
registro.agregar_higiene(hi2)

farmacia.mostrar_productos()