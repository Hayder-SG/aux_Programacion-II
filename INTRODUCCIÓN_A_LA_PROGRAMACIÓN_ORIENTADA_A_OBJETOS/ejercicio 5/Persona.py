class Persona:
    def __init__(self, nombre, paterno, materno, edad, ci):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad
        self.ci = ci

    def mostrarDatos(self):
        print(f"Nombre: {self.nombre} {self.paterno} {self.materno}, Edad: {self.edad}, CI: {self.ci}")

    def mayorDeEdad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
            return True
        else:
            print(f"{self.nombre} no es mayor de edad.")
            return False

    def modificarEdad(self, nuevo):
        self.edad = nuevo
        print(f"La edad de {self.nombre} ha sido modificada a {self.edad}.")
    def mismoApellidoPaterno(self, otro):
        if self.paterno == otro.paterno:
            print(f"{self.nombre} y {otro.nombre} tienen el mismo apellido paterno: {self.paterno}.")
            return True
        else:
            print(f"{self.nombre} y {otro.nombre} no tienen el mismo apellido paterno.")
            return False
# Instanciar a dos personas
persona1 = Persona("Juan", "Perez", "Gomez", 25, "1234567")
persona2 = Persona("Ana", "Perez", "Lopez", 17, "7654321")
persona1.mostrarDatos()
persona2.mostrarDatos()
persona1.mayorDeEdad()
persona2.mayorDeEdad()
persona1.modificarEdad(30)
persona1.mostrarDatos()
persona1.mismoApellidoPaterno(persona2)
persona2.mismoApellidoPaterno(persona1)
