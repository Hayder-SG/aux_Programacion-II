class Videojuego:
    def __init__(self, nombre, plataforma, cantidad_jugadores):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cantidad_jugadores = cantidad_jugadores

    def agregarJugadores(self, cantidad=None):
        if cantidad is not None:
            self.cantidad_jugadores += cantidad
        else:
            self.cantidad_jugadores += 1
        
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Plataforma: {self.plataforma}, Cantidad de Jugadores: {self.cantidad_jugadores}")
# main
 
videojuego1 = Videojuego("Juego A", "PC", 1)
videojuego2 = Videojuego("Juego B", "Consola", 4)
videojuego1.mostrar_info()
videojuego2.mostrar_info()

videojuego1.agregarJugadores(3)
videojuego2.agregarJugadores(3)
videojuego1.mostrar_info()
videojuego2.mostrar_info()
cant=input("Ingrese la cantidad de jugadores: ")
videojuego1.agregarJugadores(int(cant))
videojuego1.mostrar_info()