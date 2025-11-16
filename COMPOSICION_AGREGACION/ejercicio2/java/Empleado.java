package COMPOSICION_AGREGACION.ejercicio2.java;

public class Empleado {
    private String nombre;
    private String cargo;
    private double sueldo;
    private Departamento departamento;

    public Empleado(String nombre, String cargo, double sueldo, Departamento departamento) {
        this.nombre = nombre;
        this.cargo = cargo;
        this.sueldo = sueldo;
        this.departamento = departamento;
    }

    public String getNombre() {
        return nombre;
    }

    public String getCargo() {
        return cargo;
    }

    public double getSueldo() {
        return sueldo;
    }

    public Departamento getDepartamento() {
        return departamento;
    }

    public void setSueldo(double nuevoSueldo) {
        if (nuevoSueldo >= 0) {
            this.sueldo = nuevoSueldo;
        } else {
            System.out.println("El salario no puede ser negativo.");
        }
    }

    public void mostrar() {
        System.out.println("Nombre: " + nombre + ", Cargo: " + cargo + ", Sueldo: " + sueldo);
    }
}