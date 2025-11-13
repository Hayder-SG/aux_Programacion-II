class Mp4:
    def __init__(self, marca, capacidadGb, nroCanciones=0, nroVideos=0):
        self.marca = marca
        self.capacidadGb = capacidadGb
        self.nroCanciones = nroCanciones
        self.canciones = []  
        self.nroVideos = nroVideos
        self.videos = []

    def capacidad_total_mb(self):
        return self.capacidadGb * 1024

    def espacio_ocupado_mb(self):
        return sum(c["peso"] for c in self.canciones)

    def espacio_disponible_mb(self):
        return self.capacidad_total_mb() - self.espacio_ocupado_mb()

    def __add__(self, cancion):
        if not isinstance(cancion, dict):
            print("Formato de canción inválido. Debe ser un diccionario.")
            return self

        existe = any(
            c["nombre"].lower() == cancion["nombre"].lower() and
            c["artista"].lower() == cancion["artista"].lower()
            for c in self.canciones
        )

        if existe:
            print(f"La canción '{cancion['nombre']}' de {cancion['artista']} ya existe.")
            return self

        if cancion["peso"] > self.espacio_disponible_mb():
            print("No hay suficiente espacio para agregar esta canción.")
            return self

        self.canciones.append(cancion)
        print(f" Canción '{cancion['nombre']}' de {cancion['artista']} añadida correctamente.")
        return self

    def mostrar_canciones(self):
        print(f"Lista de canciones en el MP4 ({self.marca}):")
        for i, c in enumerate(self.canciones, 1):
            print(f"{i}. {c['nombre']} - {c['artista']} ({c['peso']} MB)")
        print(f"Espacio disponible: {self.espacio_disponible_mb():.2f} MB")


def main():
    mp4 = Mp4("Sony Walkman", 1)  

    c1 = {"nombre": "Shape of You", "artista": "Ed Sheeran", "peso": 4.5}
    c2 = {"nombre": "Perfect", "artista": "Ed Sheeran", "peso": 5.0}
    c3 = {"nombre": "Shape of You", "artista": "Ed Sheeran", "peso": 4.5}  
    c4 = {"nombre": "Larga", "artista": "Grande", "peso": 2000} 
    mp4 + c1
    mp4 + c2
    mp4 + c3  
    mp4 + c4  
    mp4.mostrar_canciones()

if __name__ == "__main__":
    main()
