class Pasajero:
    def __init__(self, nombre="", edad=0, genero="", costo_pasaje=0.0):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.costo_pasaje = costo_pasaje

    def __add__(self, other):
        return self

    def __sub__(self, other):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, Costo: ${self.costo_pasaje:.2f}")
        return self


class Crucero:
    def __init__(self, nombre="", paisOrigen="", paisDestino="", nropasajeros=0):
        self.nombre = nombre
        self.paisOrigen = paisOrigen
        self.paisDestino = paisDestino
        self.nropasajeros = nropasajeros
        self.pasajeros = []

    def __add__(self, other):
        if isinstance(other, Crucero):
            if len(self.pasajeros) == len(other.pasajeros):
                print("Ambos cruceros tienen la misma cantidad de pasajeros.")
            else:
                print("Los cruceros tienen diferente cantidad de pasajeros.")
            return None
        elif isinstance(other, Pasajero):
            if len(self.pasajeros) < self.nropasajeros:
                self.pasajeros.append(other)
                print(f"Pasajero {other.nombre} agregado al crucero.")
            else:
                print("El crucero está lleno.")
            return self
        else:
            print("Operación '+' no válida.")
            return self

    def __sub__(self, other):
        if other is None:
            print(f"Crucero: {self.nombre}")
            print(f"Origen: {self.paisOrigen}, Destino: {self.paisDestino}")
            print(f"Número de pasajeros: {len(self.pasajeros)}")
            print("Lista de pasajeros:")
            for idx, pasajero in enumerate(self.pasajeros, 1):
                print(f"Pasajero {idx}:")
                pasajero - None
            return self
        elif other == "genero":
            hombres = sum(1 for p in self.pasajeros if p.genero.lower() == "m")
            mujeres = sum(1 for p in self.pasajeros if p.genero.lower() == "f")
            print(f"Mujeres a bordo: {mujeres}")
            print(f"Hombres a bordo: {hombres}")
            return None
        else:
            print("Operación '-' no válida.")
            return self

    def __eq__(self, other):
        total = sum(p.costo_pasaje for p in self.pasajeros)
        print(f"Suma total del costo de los pasajes: Bs{total:.2f}")
        return True

def main():
    crucero1 = Crucero("Crucero Pacifico", "Chile", "Argentina", 3)
    crucero2 = Crucero("Crucero Atlantico", "Brasil", "Uruguay", 2)

    p1 = Pasajero("Ana", 25, "F", 600)
    p2 = Pasajero("Luis", 30, "M", 500)
    p3 = Pasajero("Clara", 40, "F", 700)

    p4 = Pasajero("Pedro", 50, "M", 800)
    p5 = Pasajero("Sofia", 28, "F", 550)

    crucero1 + p1
    crucero1 + p2
    crucero1 + p3

    crucero2 + p4
    crucero2 + p5

    print("Comparando número de pasajeros:")
    crucero1 + crucero2

    crucero1 - None

    print("Género en crucero1:")
    crucero1 - "genero"

    print("Costo total de pasajes en crucero1:")
    crucero1 == None

if __name__ == "__main__":
    main()
