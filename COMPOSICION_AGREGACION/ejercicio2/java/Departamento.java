package COMPOSICION_AGREGACION.ejercicio2.java;

import java.util.ArrayList;

public class Departamento {
    private String nombre;
    private String area;
    ArrayList<Empleado> empleados;

    public Departamento(String nombre, String area) {
        this.nombre = nombre;
        this.area = area;
        this.empleados = new ArrayList<>();
    }

    public void mostrarEmpleados() {
        System.out.println("Los empleados del departamento " + nombre + " son:");
        if (empleados.isEmpty()) {
            System.out.println("(Sin empleados)");
        }
        for (Empleado empleado : empleados) {
            empleado.mostrar();
        }
        System.out.println();
    }

    public void cambioSalario(double salario) {
        for (Empleado empleado : empleados) {
            empleado.setSueldo(salario);
        }
    }

    public void verificarDep1(Departamento dep2) {
        boolean existe = false;

        for (Empleado empleado : empleados) {
            if (empleado.getDepartamento() == dep2) {
                System.out.println(empleado.getNombre() + " pertenece también al departamento 2");
                existe = true;
            }
        }

        if (!existe) {
            System.out.println("Ningún empleado de dep1 pertenece a dep2");
        }
    }

    public void moverEmpleados(Departamento dep2) {
        for (Empleado empleado : empleados) {
            dep2.empleados.add(empleado);
        }
        empleados.clear();
    }
}
