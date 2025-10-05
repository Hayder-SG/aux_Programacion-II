package HERENCIA.ejercicio13.clases;

public class Main {
    public static void main(String[] args) {
        Chef chef = new Chef("Remy", 2000, 10, "Italiana", 25.0f);
        Mesero mesero1 = new Mesero("Alfredo", 1500, 8, 15.0f, 200.0);
        Mesero mesero2 = new Mesero("Linguini", 1500, 5, 15.0f, 180.0);
        Administrativo admin1 = new Administrativo("Colette", 1800, "Gerente");
        Administrativo admin2 = new Administrativo("Django", 1800, "Secretario");

        Empleado[] empleados = {chef, mesero1, mesero2, admin1, admin2};

        float X = 1800;
        System.out.println("\n=== Empleados con sueldo mensual igual a " + X + " ===");
        for (Empleado e : empleados) {
            if (e.getSueldomes() == X) {
                e.mostrarDatos();
            }
        }

        System.out.println("\n=== Sueldos Totales ===");
        for (Empleado e : empleados) {
            e.mostrarDatos();
        }
    }
}
