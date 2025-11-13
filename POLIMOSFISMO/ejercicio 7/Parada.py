class Parada:
    def __init__(self, admins=0, nombreP="Parada Desconocida"):
        self.admins = admins
        self.nombreP = nombreP
        self.autos =  []

    def mostrar(self):
        print(f"Nombre de la Parada: {self.nombreP}")
        print(f"Número de Administradores: {self.admins}")
        print(f"Número de Autos: {len(self.autos)}")
        for idx, auto in enumerate(self.autos, 1):
            print(f"  Auto {idx}: Marca: {auto[0]}, Dueño: {auto[1]}, Matrícula: {auto[2]}")

    def adicionar_admin(self, x):
        self.admins += x
        print(f"Se agregaron {x} administradores. Total ahora: {self.admins}")

    def adicionar_auto(self, marca, dueño, matricula):
        if len(self.autos) < 10:
            self.autos.append([marca, dueño, matricula])
            print(f"Auto agregado: Marca: {marca}, Dueño: {dueño}, Matrícula: {matricula}")
        else:
            print("No se pueden agregar más autos, capacidad máxima alcanzada.")

# main
parada1 = Parada(5, "Parada Central")
parada1.mostrar()
parada1.adicionar_admin(2)
parada1.adicionar_auto("Toyota", "Juan", "ABC123")
parada1.mostrar()