class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            total_venta = cantidad * self.precio
            print(f"Se han vendido {cantidad} unidades de {self.nombre}. Total: Bs. {total_venta:.2f}")
        else:
            print(f"No hay suficiente stock de {self.nombre}. Stock disponible: {self.stock}")

    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Se han reabastecido {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}")
    
# Crear una instancia del producto
producto = Producto(nombre="Camiseta", precio=25.0, stock=100)
producto.vender(20)
producto.reabastecer(50)
producto.vender(150)