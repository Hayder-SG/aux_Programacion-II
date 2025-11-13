class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio
    
    def __del__(self):
        print(f"Producto '{self.__nombre}' eliminado de memoria")

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_precio(self, precio):
        if precio >= 0:
            self.__precio = precio
        else:
            print("El precio no puede ser negativo")


class Pedido:
    def __init__(self, id_pedido, estado):
        self.__id_pedido = id_pedido
        self.__estado = estado

    def __del__(self):
        print(f"Pedido #{self.__id_pedido} eliminado de memoria")

    def get_id_pedido(self):
        return self.__id_pedido

    def get_estado(self):
        return self.__estado

    def set_id_pedido(self, id_pedido):
        self.__id_pedido = id_pedido

    def set_estado(self, estado):
        estados_validos = ["registrado", "preparado", "entregado"]
        if estado in estados_validos:
            self.__estado = estado
        else:
            print("Estado no válido")

producto1 = Producto("Café Latte", 20.5)
print(f"Producto: {producto1.get_nombre()} - Precio: {producto1.get_precio()} Bs")

pedido1 = Pedido(101, "registrado")
print(f"Pedido ID: {pedido1.get_id_pedido()} - Estado: {pedido1.get_estado()}")

producto1.set_precio(22)
pedido1.set_estado("preparado")

print(f"Producto actualizado: {producto1.get_nombre()} - Precio: {producto1.get_precio()} Bs")
print(f"Pedido actualizado: ID {pedido1.get_id_pedido()} - Estado: {pedido1.get_estado()}")
