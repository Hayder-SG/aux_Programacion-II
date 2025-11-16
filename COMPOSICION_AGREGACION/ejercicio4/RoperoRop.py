class Ropa:
    def __init__(self,tipo , material):
        self.tipo = tipo
        self.material = material

    def mostrar(self):
        print(f"\tTipo: {self.tipo}, Material: {self.material}")

class Ropero:
    def __init__(self, material, ropa =[], nroRopas = 0):
        self.material = material
        self.ropa = ropa 
        self.nroRopas = nroRopas
    def agregar_prenda(self, prenda):
        self.ropa.append(prenda)
        self.nroRopas += 1
        
    def agregar_N_prendas(self, nroRopas, prenda):
        self.nroRopas += nroRopas
        for i in range(nroRopas):
            self.ropa.append(prenda)
    
    def eliminarTipoX_materialX(self, tipo=None, material=None):
        ropasEliminadas = 0
        nuevas_ropas = []
        print("Las prendas eliminadas son:")
        for ropa in self.ropa:
            eliminar = False
            if tipo is not None and ropa.tipo == tipo:
                eliminar = True
            if material is not None and ropa.material == material:
                eliminar = True
            if eliminar:
                
                print(f"\tRopa eliminada: {ropa.tipo} {ropa.material}")
                ropasEliminadas += 1
            else:
                nuevas_ropas.append(ropa)
        self.ropa = nuevas_ropas
        self.nroRopas = len(self.ropa)
        print(f"Numero de ropas eliminadas: {ropasEliminadas}")
        print("===========================================")
    
    def mostrarTipoMaterial(self, tipo=None, material=None):
        print(f"\nPrendas de tipo {tipo} y material {material}:")
        for ropa in self.ropa:
            if tipo == ropa.tipo and material == ropa.material:
                ropa.mostrar()
        print(f"Total de prendasde tipo {tipo} y material {material}: {self.nroRopas}")
        print("===========================================")
        
    def mostrar_ropa(self):
        print(f"\nLas prendas de mi ropero de {self.material} son:")
        for ropa in self.ropa:
            ropa.mostrar()
        print(f"Total de prendas: {self.nroRopas}")
        print("===========================================")


rop = Ropero("Sintético")
ropa1 = Ropa("Camisa", "Algodón")
ropa2 = Ropa("Pantalón", "lino")
ropa3 = Ropa("Pantalón", "Algodón")
ropa = Ropa("saco", "polipropileno")

rop.agregar_prenda(ropa1)
rop.agregar_prenda(ropa2)
rop.agregar_prenda(ropa3)

rop.agregar_N_prendas(3, ropa)
rop.agregar_N_prendas(2, ropa1)

rop.mostrar_ropa()

rop.agregar_N_prendas(2, ropa3)

rop.mostrar_ropa()

rop.eliminarTipoX_materialX("Camisa", "")

rop.mostrar_ropa()

rop.mostrarTipoMaterial("Pantalón", "Algodón")