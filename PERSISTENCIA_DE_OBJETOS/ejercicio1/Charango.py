import json

class Charango:
    def __init__(self, material, nroCuerdas, Cuerdas=None):
        self.material = material
        self.nroCuerdas = nroCuerdas
        self.Cuerdas = Cuerdas
    def mostrar(self):
        print("================================================================")
        print(f"Material: {self.material} || nroCuerdas: {self.nroCuerdas}")
        print("Cuerdas:", self.Cuerdas)
        print("Cuerdas malas:", self.cuerdasMalas())
        print("================================================================")
            
    def cuerdasMalas(self):
        contador = 0 
        for cuerda in self.Cuerdas:
            if not cuerda:
                contador += 1
        return contador

    def to_dict(self):
        return {
            "material": self.material,
            "nroCuerdas": self.nroCuerdas,
            "cuerdas": self.Cuerdas
        }

    @staticmethod
    def from_dict(data):
        return Charango(
            data["material"],
            data["nroCuerdas"],            
            data["cuerdas"]
        )


class ListaCharangos:
    def __init__(self):
        self.charangos = []

    def agregar(self, charango):
        self.charangos.append(charango)

    def mostrar(self):
        for i, char in enumerate(self.charangos, 1):
            print("================================================================")
            print("Numero: ", i)
            print(f"Material: {char.material} || nroCuerdas: {char.nroCuerdas}")
            print("Cuerdas:", char.Cuerdas)
            print("Cuerdas malas:", char.cuerdasMalas())
            print("================================================================")

    def guardar(self):
        with open("Charango.json", "w") as archivo:
            json.dump([b.to_dict() for b in self.charangos], archivo, indent=4)
            
    #b) Eliminar a los charangos cuyas cuerdas en estado false sea mayor a 6.
    def cargar(self):
        with open("Charango.json", "r") as archivo:
            data = json.load(archivo)
        self.charangos = []
        for d in data:
            char = Charango.from_dict(d)
            if char.cuerdasMalas() <= 6:
                self.agregar(char)
        
    def listarCharangoMatX(self, material):
        for char in self.charangos:
            if char.material == material:
                char.mostrar()
    
    def buscarCharangocuerdasN(self, nCuerdas):
        for char in self.charangos:
            if char.nroCuerdas == nCuerdas:
                char.mostrar()
    def ordenarPorMaterial(self):
        self.charangos.sort(key=lambda c: c.material)

                
            

                
# --- USO ---

charangos = [
    Charango("quirquincho", 9, [True]*10),
    Charango("quirquincho", 9, [True]*10),
    Charango("quirquincho", 9, [True]*10)
]

cChar = ListaCharangos()
for c in charangos:
    cChar.agregar(c)

# Guardar en JSON
cChar.guardar()
cChar.cargar()
cChar.mostrar()
#c) Listar a los charangos de material x.
cChar.listarCharangoMatX("quirquincho")
#d) Buscar los charangos con 10 cuerdas.
cChar.buscarCharangocuerdasN(10)
#e) Ordenar los charangos por material en orden alfabético.

cChar.ordenarPorMaterial()
cChar.mostrar()