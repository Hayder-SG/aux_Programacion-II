class Bailarin:
    def __init__(self, nombre, edad, id, facultad, fraternidad):
        self.nombre = nombre
        self.edad = edad
        self.id = id
        self.facultad = facultad
        self.fraternidad = fraternidad
    def mostrar_info(self):
        print(f"\tNombre: {self.nombre}, Edad: {self.edad}, ID: {self.id}, Facultad: {self.facultad}, Fraternidad: {self.fraternidad}")


class Fraternidad:
    def __init__(self, nombre, encargado, bailarines):
        self.nombre = nombre
        self.encargado = encargado
        self.bailarines = bailarines
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Encargado: {self.encargado}")
        for bailarin in self.bailarines:
            bailarin.mostrar_info()
    def añadir_bailarin(self, bailarin):
        self.bailarines.append(bailarin)


class Facultad:
    def __init__(self, nombre, bailarines):
        self.nombre = nombre
        self.bailarines = bailarines
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        for bailarin in self.bailarines:
            bailarin.mostrar_info()

class Gestion:
    def __init__(self, bailarines, fraternidades, facultades):
        self.bailarines = bailarines
        self.fraternidades = fraternidades
        self.facultades = facultades
    
    def mostrar_info(self):
        print("Bailarines:")
        for bailarin in self.bailarines:
            bailarin.mostrar_info()
        print("\nFraternidades:")
        for fraternidad in self.fraternidades:
            fraternidad.mostrar_info()
        print("\nFacultades:")
        for facultad in self.facultades:
            facultad.mostrar_info()
    
    def esta_2_fraternidad(self):
        print("\nBailarines que están en 2 o más fraternidades:")
        duplicados = []
        conteo = {}
        for fraternidad in self.fraternidades:
            for bailarin in fraternidad.bailarines:
                conteo[bailarin.id] = conteo.get(bailarin.id, 0) + 1
        for bailarin_id, cantidad in conteo.items():
            if cantidad > 1:
                duplicados.append(bailarin_id)
        if duplicados:
            for bailarin in self.bailarines:
                if bailarin.id in duplicados:
                    bailarin.mostrar_info()  
        else:
            print("No hay bailarines repetidos.") 
    
    def agregar_bailarin(self, bailarin):
        for b in self.bailarines:
            if b.id == bailarin.id:
                print("El bailarín ya pertenece a una fraternidad.")
                return
        self.bailarines.append(bailarin)
        print(f"Bailarín {bailarin.nombre} registrado correctamente.")
        
b1 = Bailarin("Bailarin 1", 20, 1, "Facultad 1", "Fraternidad 1")
b2 = Bailarin("Bailarin 2", 21, 2, "Facultad 2", "Fraternidad 2")
b3 = Bailarin("Bailarin 3", 22, 3, "Facultad 1", "Fraternidad 1")
b4 = Bailarin("Bailarin 4", 23, 4, "Facultad 2", "Fraternidad 2")
b5 = Bailarin("Bailarin 5", 24, 5, "Facultad 1", "Fraternidad 1")
b6 = Bailarin("Bailarin 6", 25, 6, "Facultad 2", "Fraternidad 2")
b7 = Bailarin("Bailarin 7", 26, 7, "Facultad 1", "Fraternidad 1")

f1 = Facultad("Facultad 1", [b1, b3, b5])
f2 = Facultad("Facultad 2", [b2, b4, b6])

fr1 = Fraternidad("Fraternidad 1", "Encargado 1", [b1, b3, b5])
fr2 = Fraternidad("Fraternidad 2", "Encargado 2", [b2, b4, b6])

g = Gestion([b1, b2, b3, b4, b5, b6, b7], [fr1, fr2], [f1, f2])

g.mostrar_info()
g.esta_2_fraternidad()

g.agregar_bailarin(Bailarin("Bailarin 8", 27, 8, "Facultad 1", "Fraternidad 1"))

g.mostrar_info()
g.esta_2_fraternidad()