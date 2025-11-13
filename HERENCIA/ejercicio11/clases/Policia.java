package HERENCIA.ejercicio11.clases;

public class Policia extends Empleado {
    protected String grado;
    protected String division;

    public Policia(String nombre, int edad, double sueldo, String cargo, String grado, String division) {
        super(nombre, edad, sueldo, cargo);
        this.grado = grado;
        this.division = division;
    }
}