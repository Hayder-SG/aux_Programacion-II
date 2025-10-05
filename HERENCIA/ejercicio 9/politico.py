class Politico:
    def __init__(self, profesion, añosExp):
        self.profesion = profesion
        self.añosExp = añosExp

class Partido:
    def __init__(self, nombreP, rol):
        self.nombreP = nombreP
        self.rol = rol

class Presidente(Politico, Partido):
    def __init__(self, nombre, apellido, profesion, anosExp, nombreP, rol):
        Politico.__init__(self, profesion, anosExp)
        Partido.__init__(self, nombreP, rol)
        self.nombre = nombre
        self.apellido = apellido
    def mostrar_info(self):
        print(f"Presidente: {self.nombre} {self.apellido}, Profesión: {self.profesion}, Años de Experiencia: {self.añosExp}, Partido: {self.nombreP}, Rol: {self.rol}")

presidente1 = Presidente("Juan", "Perez", "Abogado", 15, "Partido A", "Líder")
presidente2 = Presidente("Maria", "Gomez", "Economista", 10, "Partido B", "Miembro")
presidente1.mostrar_info()
presidente2.mostrar_info()
vector_presidentes = [presidente1, presidente2]
nombre_buscar = "Juan"
for presidente in vector_presidentes:
    if presidente.nombre == nombre_buscar:
        print(f"Partido Político: {presidente.nombreP}, Profesión: {presidente.profesion}")
        break
else:
    print("Presidente no encontrado.")  