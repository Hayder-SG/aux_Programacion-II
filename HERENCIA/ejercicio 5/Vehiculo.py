class Vehiculo:
    def __init__(self, conductor, marca, id):
        self.conductor = conductor
        self.marca = marca
        self.id = id
        
    def cambiar_conductor(self, nuevo_conductor):
        self.conductor = nuevo_conductor

class Bus(Vehiculo):
    def __init__(self, conductor, marca, id, capacidad, sindicato):
        super().__init__(conductor, marca, id)
        self.capacidad = capacidad
        self.sindicato = sindicato

class Auto(Vehiculo):
    def __init__(self, conductor, marca, id, caballosFuerza, descapotable):
        super().__init__(conductor, marca, id)
        self.caballosFuerza = caballosFuerza
        self.descapotable = descapotable

class Moto(Vehiculo):
    def __init__(self, conductor, marca, id, cilindrada, casco):
        super().__init__(conductor, marca, id)
        self.cilindrada = cilindrada
        self.casco = casco
        
    
# main
bus = Bus("Juan Perez", "Mercedes", "BUS123", 50, "Sindicato A")
auto = Auto("Maria Gomez", "Toyota", "AUTO456", 150, True)
moto = Moto("Carlos Lopez", "Yamaha", "MOTO789", 600, True)
print(f"Bus - Placa: {bus.id}, Conductor: {bus.conductor}")
print(f"Auto - Placa: {auto.id}, Conductor: {auto.conductor}")
print(f"Moto - Placa: {moto.id}, Conductor: {moto.conductor}")
bus.cambiar_conductor("Luis Martinez")
print(f"Nuevo Conductor del Bus - Placa: {bus.id}, Conductor: {bus.conductor}")
auto.cambiar_conductor("Ana Torres")
print(f"Nuevo Conductor del Auto - Placa: {auto.id}, Conductor: {auto.conductor}")  
moto.cambiar_conductor("Pedro Ramirez")
print(f"Nuevo Conductor del Moto - Placa: {moto.id}, Conductor: {moto.conductor}")