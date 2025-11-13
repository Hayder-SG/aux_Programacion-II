class Ordenador:
    def __init__(self, serial, numero, ram, procesador, estado):
        self.serial = serial
        self.numero = numero
        self.ram = ram 
        self.procesador = procesador
        self.estado = estado 

    def mostrar(self):
        print(f"Serial: {self.serial}, N°: {self.numero}, RAM: {self.ram} GB, "
            f"CPU: {self.procesador}, Estado: {self.estado}")

class Laboratorio:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.ordenadores = [] 

    def agregar_ordenador(self, ordenador):
        if len(self.ordenadores) < self.capacidad:
            self.ordenadores.append(ordenador)
        else:
            print(f"El laboratorio '{self.nombre}' está lleno.")

    def informacion(self, filtro=None):
        print(f"Información de ordenadores - Laboratorio: {self.nombre}")
        if filtro is None:
            for pc in self.ordenadores:
                pc.mostrar()
        elif filtro == "activo" or filtro == "inactivo":
            for pc in self.ordenadores:
                if pc.estado.lower() == filtro.lower():
                    pc.mostrar()
        else:
            print("Filtro no reconocido.")

def trasladar_ordenadores(origen: Laboratorio, destino: Laboratorio, cantidad=2):
    print("Traslado de ordenadores:")
    print("Antes del traslado:")
    origen.informacion()
    destino.informacion()

    trasladados = 0
    a_trasladar = []

    for pc in origen.ordenadores:
        if trasladados < cantidad and len(destino.ordenadores) < destino.capacidad:
            a_trasladar.append(pc)
            trasladados += 1

    for pc in a_trasladar:
        origen.ordenadores.remove(pc)
        destino.agregar_ordenador(pc)

    print("Después del traslado:")
    origen.informacion()
    destino.informacion()

def main():

    pc1 = Ordenador("S1001", 1, 4, "Intel i3", "activo")
    pc2 = Ordenador("S1002", 2, 8, "Intel i5", "inactivo")
    pc3 = Ordenador("S1003", 3, 16, "Intel i7", "activo")
    pc4 = Ordenador("S1004", 4, 12, "Ryzen 5", "activo")
    pc5 = Ordenador("S1005", 5, 6, "Intel i5", "inactivo")
    pc6 = Ordenador("S1006", 6, 32, "Ryzen 7", "activo")

    lasin1 = Laboratorio("Lasin 1", capacidad=4)
    lasin2 = Laboratorio("Lasin 2", capacidad=4)

    lasin1.agregar_ordenador(pc1)
    lasin1.agregar_ordenador(pc2)
    lasin1.agregar_ordenador(pc3)
    lasin1.agregar_ordenador(pc4)

    lasin2.agregar_ordenador(pc5)
    lasin2.agregar_ordenador(pc6)

    print("\n--- ORDENADORES ACTIVOS EN LASIN 1 ---")
    lasin1.informacion("activo")

    trasladar_ordenadores(lasin1, lasin2, cantidad=1)

if __name__ == "__main__":
    main()
