package HERENCIA.ejercicio13.clases;

public class Chef extends Empleado {
    public int horaExtra;
    public String tipo;
    public float sueldoHora;
    public Chef(String nombre, float sueldomes, int horaExtra, String tipo, float sueldoHora) {
        super(nombre, sueldomes);
        this.horaExtra = horaExtra;
        this.tipo = tipo;
        this.sueldoHora = sueldoHora;
    }

    @Override
    public float SueldoTotal() {
        return sueldomes + (horaExtra * sueldoHora);
    }

    @Override
    public void mostrarDatos() {
        System.out.println("Chef");
        System.out.println("====");
        System.out.println("Chef: " + nombre);
        System.out.println("| Tipo: " + tipo);
        System.out.println("| Sueldo base: " + sueldomes);
        System.out.println("| Horas extra: " + horaExtra);
        System.out.println("| Sueldo total: " + SueldoTotal());
        System.out.println("=================================");
    }
}
