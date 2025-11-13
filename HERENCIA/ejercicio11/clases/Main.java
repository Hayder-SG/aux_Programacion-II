package HERENCIA.ejercicio11.clases;

public class Main {
    public static void main(String[] args) {
        JefePolicia jefe1 = new JefePolicia("Carlos Pérez", 45, 5000, "Comandante", "Teniente", "Antinarcóticos", 20, "Zona Norte");
        JefePolicia jefe2 = new JefePolicia("Luis Gómez", 40, 4800, "Subcomandante", "Teniente", "Criminalística", 18, "Zona Sur");

        System.out.println("=== DATOS DE LOS JEFES DE POLICÍA ===");
        jefe1.mostrarDatos();
        jefe2.mostrarDatos();

        System.out.println("=== Jefe con mayor sueldo ===");
        if (jefe1.sueldo > jefe2.sueldo) {
            System.out.println(jefe1.nombre + " tiene el mayor sueldo.");
        } else if (jefe2.sueldo > jefe1.sueldo) {
            System.out.println(jefe2.nombre + " tiene el mayor sueldo.");
        } else {
            System.out.println("Ambos tienen el mismo sueldo.");
        }


        System.out.println("=== Comparación de grado ===");
        if (jefe1.grado.equals(jefe2.grado)) {
            System.out.println("Ambos tienen el mismo grado: " + jefe1.grado);
        } else {
            System.out.println("Tienen grados distintos: " + jefe1.grado + " y " + jefe2.grado);
        }
    }
}