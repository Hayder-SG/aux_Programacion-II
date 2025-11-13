class Fruta:
    def __init__(self, nombre, tipo, vitaminas):
        self.nombre = nombre
        self.tipo = tipo
        self.vitaminas = vitaminas 

    def contar_vitaminas(self):
        return len(self.vitaminas)

    def mostrar_vitaminas(self):
        return self.vitaminas

    def vitaminas_citricas(self):
        citricas = {'C', 'B1', 'B2', 'B3', 'B5', 'B6', 'B9'}
        return [vitamina for vitamina in self.vitaminas if vitamina in citricas]

    def ordenar_vitaminas(self):
        return sorted(self.vitaminas)

fruta1 = Fruta(nombre="Kiwi", tipo="Subtropical", vitaminas=["C", "E", "K"])
fruta2 = Fruta(nombre="Naranja", tipo="Cítrica", vitaminas=["C", "B1", "B2"])
fruta3 = Fruta(nombre="Mango", tipo="Tropical", vitaminas=["A", "C", "E"])
fruta4 = Fruta(nombre="Fresa", tipo="Cítrica", vitaminas=["C", "B9", "K"])

frutas = [fruta1, fruta2, fruta3, fruta4]  
fruta_mas_vitaminas = max(frutas, key=lambda fruta: fruta.contar_vitaminas())
print(f"La fruta con más vitaminas es: {fruta_mas_vitaminas.nombre} con {fruta_mas_vitaminas.contar_vitaminas()} vitaminas.")   

fruta_x = fruta2 
print(f"Las vitaminas de la {fruta_x.nombre} son: {', '.join(fruta_x.mostrar_vitaminas())}")

for fruta in frutas:
    vitaminas_citricas = fruta.vitaminas_citricas()
    print(f"La {fruta.nombre} tiene {len(vitaminas_citricas)} vitaminas cítricas: {', '.join(vitaminas_citricas)}")

for fruta in frutas:
    vitaminas_ordenadas = fruta.ordenar_vitaminas()
    print(f"Las vitaminas de la {fruta.nombre} ordenadas alfabéticamente son: {', '.join(vitaminas_ordenadas)}")
    