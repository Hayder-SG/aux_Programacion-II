package INTRODUCCIÓN_A_LA_PROGRAMACIÓN_ORIENTADA_A_OBJETOS.ejercicio2.java;

public class Bus {
    public int capacidad;
    public int pasajeros;
    public double dinero;

    public Bus(int capacidad) {
        this.capacidad = capacidad;
        this.pasajeros = 0;
        this.dinero = 0.0;
    }

    public void subirPasajeros(int cantidad) {
        if (this.pasajeros + cantidad <= this.capacidad) {
            this.pasajeros += cantidad;
            System.out.println(cantidad + " pasajeros han subido al bus.");
        } else {
            System.out.println("No hay suficiente espacio en el bus.");
        }
    }

    public void cobrarPasaje() {
        double costoPasaje = 1.50;
        double totalCobrado = this.pasajeros * costoPasaje;
        this.dinero += totalCobrado;
        System.out.println("Se ha cobrado un total de: Bs. " + String.format("%.2f", totalCobrado));
    }

    public int asientosDisponibles() {
        int asientosLibres = this.capacidad - this.pasajeros;
        System.out.println("Asientos disponibles: " + asientosLibres);
        return asientosLibres;
    }

    public static void main(String[] args) {
        Bus bus = new Bus(50);

        bus.subirPasajeros(30);
        bus.cobrarPasaje();
        bus.asientosDisponibles();
        bus.subirPasajeros(25);
    }
}
