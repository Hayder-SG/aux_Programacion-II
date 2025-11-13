# Ejercicio 3. Crea una clase base Animal y subclases Leon, Pinguino, y Canguro. Agrega
# un método desplazarse().
# a) Crea la clase Animal con atributos nombre y edad, y el método desplazarse().
# b) Cada subclase debe redefinir el método desplazarse() con su forma particular
# (caminar, saltar, nadar).
# c) Crea un arreglo de animales y haz que cada uno se desplace.
from abc import abstractmethod


class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def desplazarse(self):
        pass

class Leon(Animal):
    def desplazarse(self):
        print(f"El león {self.nombre} está caminando.")

class Pinguino(Animal):
    def desplazarse(self):
        print(f"El pingüino {self.nombre} está nadando.")

class Canguro(Animal):
    def desplazarse(self):
        print(f"El canguro {self.nombre} está saltando.")

animales = [
    Leon("Simba", 5),
    Pinguino("Pingu", 3),
    Canguro("Jack", 2)
]

for animal in animales:
    animal.desplazarse()