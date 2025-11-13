class Bus:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = 0
        self.dinero = 0.0

    def subir_pasajeros(self, cantidad):
        if self.pasajeros + cantidad <= self.capacidad:
            self.pasajeros += cantidad
            print(f"{cantidad} pasajeros han subido al bus.")
        else:
            print("No hay suficiente espacio en el bus.")

    def cobrar_pasaje(self):
        costo_pasaje = 1.50
        total_cobrado = self.pasajeros * costo_pasaje
        self.dinero += total_cobrado
        print(f"Se ha cobrado un total de: Bs. {total_cobrado:.2f}")

    def asientos_disponibles(self):
        asientos_libres = self.capacidad - self.pasajeros
        print(f"Asientos disponibles: {asientos_libres}")
        return asientos_libres

# Crear una instancia del bus
bus = Bus(capacidad=50)

bus.subir_pasajeros(30)
bus.cobrar_pasaje()      
bus.asientos_disponibles()
bus.subir_pasajeros(25)