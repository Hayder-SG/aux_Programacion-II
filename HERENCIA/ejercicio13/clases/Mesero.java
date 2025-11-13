package HERENCIA.ejercicio13.clases;

public class Mesero extends Empleado {
    private double propina;
    private int horaExtra;
    private float sueldoHora;

    public Mesero(String nombre, float sueldomes, int horaExtra, float sueldoHora, double propina) {
        super(nombre, sueldomes);
        this.horaExtra = horaExtra;
        this.sueldoHora = sueldoHora;
        this.propina = propina;
    }

    @Override
    public float SueldoTotal() {
        return (float)(sueldomes + (horaExtra * sueldoHora) + propina);
    }

    @Override
    public void mostrarDatos() {
        System.out.println("Mesero");
        System.out.println("=======");
        System.out.println("|Mesero: " + nombre );
        System.out.println("|Sueldo base: " + sueldomes);
        System.out.println("|Horas extra: " + horaExtra);
        System.out.println("|Propina: " + propina);
        System.out.println("|Sueldo total: " + SueldoTotal());
        System.out.println("=================================");
    }
}
