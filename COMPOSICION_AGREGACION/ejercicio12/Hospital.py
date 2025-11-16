class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
    
    def mostrar_info(self):
        print(f"\tNombre: {self.nombre}, Especialidad: {self.especialidad}")
class Hospital:
    def __init__(self, nombre, doctores):
        self.nombre = nombre
        self.doctores = doctores
    def mostrar_info(self):
        print(f"===============================")
        print(f"Hospital: {self.nombre}")
        for doctor in self.doctores:
            doctor.mostrar_info()
        print("===============================")
        print()

d1 = Doctor("Dr. Juan", "Cardiologo")
d2 = Doctor("Dr. Maria", "Pediatria")
d3 = Doctor("Dr. Pedro", "Oncologo")
d4 = Doctor("Dr. Ana", "Ginecologo")
d5 = Doctor("Dr. Luis", "Neurologia")

h1 = Hospital("Hospital A", [d1, d2, d3])
h2 = Hospital("Hospital B", [d4, d5])
h1.mostrar_info()
h2.mostrar_info()