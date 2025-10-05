# Ejercicio 5. Dada la clase celular <nroTel, dueño, espacio, ram, nroApp>
# a) realizar el diagrama de clases
# b) realizar la sobrecarga del operador ++ para aumentar en 10 el nroApp.
# c) realizar la sobrecarga del operador - - para disminuir el espacio en 5 gb.
# d) mostrar los datos antes y después de los operadores.

class Celular:
    def __init__(self, nroTel, dueño, espacio, ram, nroApp):
        self.nroTel = nroTel
        self.dueño = dueño
        self.espacio = espacio  
        self.ram = ram          
        self.nroApp = nroApp

    def __str__(self):
        return (f"Número de Teléfono: {self.nroTel}, Dueño: {self.dueño}, "
                f"Espacio: {self.espacio}GB, RAM: {self.ram}GB, Número de Apps: {self.nroApp}")

    def __add__(self, otro):
        if isinstance(otro, int):
            self.nroApp += otro
        return self

    def __sub__(self, otro):
        self.espacio -= otro
        if self.espacio < 0:
            self.espacio = 0  
        return self
# main
celular = Celular("123-456-7890", "Juan Perez", 64, 4, 20)
print("Antes de los operadores:")
print(celular)
celular += 10
celular -= 5
print("Después de los operadores:")
print(celular)  
