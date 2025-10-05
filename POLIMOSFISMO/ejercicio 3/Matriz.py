class Matriz:
    def __init__(self, matriz):
        self.matriz = matriz
        
    def matriz_identidad(self, tamaño):
        for i in range(tamaño):
            fila = []
            for j in range(tamaño):
                if i == j:
                    fila.append(1)
                else:
                    fila.append(0)
            self.matriz.append(fila)
            
    def __add__(self, otra):
        resultado = []
        for i in range(len(self.matriz)):
            fila = []
            for j in range(len(self.matriz[i])):
                fila.append(self.matriz[i][j] + otra.matriz[i][j])
            resultado.append(fila)
        return Matriz(resultado)
    
    def __sub__(self, otra):
        resultado = []
        for i in range(len(self.matriz)):
            fila = []
            for j in range(len(self.matriz[i])):
                fila.append(self.matriz[i][j] - otra.matriz[i][j])
            resultado.append(fila)
        return Matriz(resultado)
    
    def __eq__(self, otra):
        return self.matriz == otra.matriz
    
    def mostrar(self):
        for fila in self.matriz:
            print(fila)
# main
matriz1 = Matriz([[1, 2, 3, 4,5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
matriz2 = Matriz([[9, 8, 7, 6, 5], [4, 3, 2, 1, 0], [-1, -2, -3, -4, -5]])
suma = matriz1 + matriz2
resta = matriz1 - matriz2
print("Matriz 1:")
matriz1.mostrar()   
print("Matriz 2:")
matriz2.mostrar()
print("Suma:")
suma.mostrar()
print("Resta:")
resta.mostrar()
print("¿Son iguales las matrices 1 y 2?", matriz1 == matriz2)
# matriz identidad
matriz_identidad = Matriz([])
matriz_identidad.matriz_identidad(3)
print("Matriz Identidad 3x3:")
matriz_identidad.mostrar()
