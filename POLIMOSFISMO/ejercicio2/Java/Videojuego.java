package POLIMOSFISMO.ejercicio2.Java;

public class Videojuego {
    public String nombre;
    public String plataforma;
    public int cantidadJugadores;

    public Videojuego(String nombre, String plataforma, int cantidadJugadores) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = cantidadJugadores;
    }

    public void agregarJugadores(int cantidad) {
        this.cantidadJugadores += cantidad;
    }

    public void agregarJugadores() {
        this.cantidadJugadores += 1;
    }
    public void mostrarInfo() {
        System.out.println("Título: " + nombre);
        System.out.println("Plataforma: " + plataforma);
        System.out.println("Cantidad de Jugadores: " + cantidadJugadores);
    }
}
