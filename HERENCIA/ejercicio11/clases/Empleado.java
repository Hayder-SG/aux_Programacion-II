package HERENCIA.ejercicio11.clases;

public class Empleado extends Persona {
    public double sueldo;
    public String cargo;

    public Empleado(String nombre, int edad, double sueldo, String cargo) {
        super(nombre, edad);
        this.sueldo = sueldo;
        this.cargo = cargo;
    }
}

