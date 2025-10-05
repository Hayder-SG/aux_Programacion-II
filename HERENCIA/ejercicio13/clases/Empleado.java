package HERENCIA.ejercicio13.clases;

public class Empleado {
    protected String nombre;
    protected float sueldomes;

    public Empleado(String nombre, float sueldomes) {
        this.nombre = nombre;
        this.sueldomes = sueldomes;
    }

    public float SueldoTotal() {
        return sueldomes;
    }

    public String getNombre() {
        return nombre;
    }

    public float getSueldomes() {
        return sueldomes;
    }

    public void mostrarDatos() {
        System.out.println("Empleado");
        System.out.println("========");
        System.out.println("Nombre: " + nombre);
        System.out.println("Sueldo mensual: " + sueldomes);
        System.out.println("Sueldo total: " + SueldoTotal());
        System.out.println("=================================");
    }
}
