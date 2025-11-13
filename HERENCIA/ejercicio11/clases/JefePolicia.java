package HERENCIA.ejercicio11.clases;
public class JefePolicia extends Policia implements IJefePolicia {
    private int añosExperiencia;
    private String zonaAsignada;

    public JefePolicia(String nombre, int edad, double sueldo, String cargo, String grado, 
    String division, int añosExperiencia, String zonaAsignada) {
        super(nombre, edad, sueldo, cargo, grado, division);
        this.añosExperiencia = añosExperiencia;
        this.zonaAsignada = zonaAsignada;
    }

    @Override
    public void mostrarDatos() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad);
        System.out.println("Cargo: " + cargo);
        System.out.println("Grado: " + grado);
        System.out.println("Sueldo: $" + sueldo);
        System.out.println("Años de experiencia: " + añosExperiencia);
        System.out.println("Zona asignada: " + zonaAsignada);
        System.out.println("-------------------------------------");
    }
}