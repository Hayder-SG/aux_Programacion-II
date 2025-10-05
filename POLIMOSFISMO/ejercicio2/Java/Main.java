package POLIMOSFISMO.ejercicio2.Java;

public class Main {
    public static void main(String[] args) {
        Videojuego juego1 = new Videojuego("The Legend of Zelda", "Aventura", 59);
        Videojuego juego2 = new Videojuego("Super Mario Odyssey", "Plataformas", 49);
        Videojuego juego3 = new Videojuego("Minecraft", "Sandbox", 26);

        juego1.mostrarInfo();
        System.out.println();
        juego2.mostrarInfo();
        System.out.println();
        juego3.mostrarInfo();
        System.out.println();
        System.out.println("Después de agregar jugadores:");
        System.out.println();
        juego1.agregarJugadores(5);
        juego2.agregarJugadores();
        juego3.agregarJugadores(2);
        juego1.mostrarInfo();
        System.out.println();
        juego2.mostrarInfo();
        System.out.println();
        juego3.mostrarInfo();
        System.out.println();
    }
}
