class ProductoNoEncontradoException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


class StockInsuficienteException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar(self):
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Stock: {self.stock}")
        print("----------------------------")

class Inventario:
    def __init__(self):
        self.productos = []

    def agregarProducto(self, p):

        for prod in self.productos:
            if prod.codigo == p.codigo:
                raise Exception(f"El código ya existe: {p.codigo}")

        if p.precio < 0 or p.stock < 0:
            raise Exception("Precio o stock no pueden ser negativos.")

        self.productos.append(p)

    def buscarProducto(self, codigo):
        for p in self.productos:
            if p.codigo == codigo:
                return p
        raise ProductoNoEncontradoException(f"Producto no encontrado: {codigo}")

    def venderProducto(self, codigo, cantidad):
        p = self.buscarProducto(codigo)

        if p.stock < cantidad:
            raise StockInsuficienteException(
                f"Stock insuficiente. Disponible: {p.stock}"
            )

        p.stock -= cantidad
        print(f"Venta realizada. Stock actual: {p.stock}")

    def mostrarInventario(self):
        print("=== INVENTARIO ===")
        for p in self.productos:
            p.mostrar()

if __name__ == "__main__":
    inv = Inventario()

    try:
        inv.agregarProducto(Producto("P01", "Mouse", 50, 10))
        inv.agregarProducto(Producto("P02", "Teclado", 120, 5))

        inv.mostrarInventario()

        p = inv.buscarProducto("P01")
        print("Producto encontrado:", p.nombre)

        inv.venderProducto("P01", 3)

        inv.mostrarInventario()
        inv.venderProducto("P02", 10)

    except ProductoNoEncontradoException as e:
        print("ERROR:", e)

    except StockInsuficienteException as e:
        print("ERROR:", e)

    except Exception as e:
        print("ERROR GENERAL:", e)
