package HERENCIA.ejercicio13.clases;

public class Administrativo extends Empleado {
    private String cargo;

    public Administrativo(String nombre, float sueldomes, String cargo) {
        super(nombre, sueldomes);
        this.cargo = cargo;
    }

    @Override
    public void mostrarDatos() {
        System.out.println("Administrativo");
        System.out.println("=============");
        System.out.println("| Administrador: " + nombre);
        System.out.println("| Cargo: " + cargo);
        System.out.println("| Sueldo mensual: " + sueldomes);
        System.out.println("=================================");
    }
}
