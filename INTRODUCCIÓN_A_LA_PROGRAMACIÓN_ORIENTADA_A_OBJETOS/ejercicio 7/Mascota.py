# a) Agrega un método para alimentar (+20 de energía, máximo 100).
# b) Agrega un método para jugar (-15 de energía, mínimo 0).
# c) Crea dos mascotas, aliméntalas y hazlas jugar, mostrando su energía en cada
# paso.
class Mascota:
    def __init__(self, nombre, tipo, energia):
        self.nombre = nombre
        self.tipo = tipo
        self.energia = energia
    def alimentar(self):
        if self.energia + 20 <= 100:
            self.energia += 20
        else:
            self.energia = 100
        print(f"{self.nombre} ha sido alimentado. Energía actual: {self.energia}")
    def jugar(self):
        if self.energia - 15 >= 0:
            self.energia -= 15
        else:
            self.energia = 0
        print(f"{self.nombre} ha jugado. Energía actual: {self.energia}")
# Crear dos mascotas   
mascota1 = Mascota("Firulais", "Perro", 50)
mascota2 = Mascota("Michi", "Gato", 80)
mascota1.alimentar()
mascota1.jugar()
mascota2.alimentar()
mascota2.jugar()
mascota1.jugar()
mascota2.jugar()
