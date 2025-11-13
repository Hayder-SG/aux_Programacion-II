
class Persona:
    def __init__(self, nombre, paterno, materno, edad):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad
    def mostrar(self):
        print(f"Nombre: {self.nombre} {self.paterno} {self.materno}, Edad: {self.edad}")
    
class Docente(Persona):
    def __init__(self, nombre, paterno, materno, edad, sueldo, regProfesional):
        super().__init__(nombre, paterno, materno, edad)
        self.sueldo = sueldo
        self.regProfesional = regProfesional
    def mostrar(self):
        super().mostrar()
        print(f"Sueldo: {self.sueldo}, Registro Profesional: {self.regProfesional}")
        
class Estudiante(Persona):
    def __init__(self, nombre, paterno, materno, edad, ru, matricula):
        super().__init__(nombre, paterno, materno, edad)
        self.ru = ru
        self.matricula = matricula
    def mostrar(self):
        super().mostrar()
        print(f"RU: {self.ru}, Matrícula: {self.matricula}")
    def modificarEdad(self, nueva_edad):
        self.edad = nueva_edad
    @staticmethod
    def promedio(estudiantes):
        if not estudiantes:
            return 0
        total_edad = sum(est.edad for est in estudiantes)
        return total_edad / len(estudiantes)
# main
docente = Docente("Ana", "Perez", "Lopez", 40, 3000, "RP12345")
estudiante1 = Estudiante("Juan", "Gomez", "Martinez", 20, "RU001", "MAT001")
estudiante2 = Estudiante("Maria", "Rodriguez", "Sanchez", 22, "RU002", "MAT002")
docente.mostrar()
estudiante1.mostrar()
estudiante2.mostrar()