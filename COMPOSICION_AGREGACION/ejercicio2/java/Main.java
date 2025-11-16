package COMPOSICION_AGREGACION.ejercicio2.java;

public class Main {
    public static void main(String[] args) {

        // Instanciar departamentos
        Departamento dep1 = new Departamento("Departamento limpieza", "Area 1");
        Departamento dep2 = new Departamento("Departamento mantenimiento", "Area 2");

        // Crear empleados
        Empleado e1 = new Empleado("Juan 1", "Cargo 1", 1000, dep1);
        Empleado e2 = new Empleado("Pepe 2", "Cargo 2", 2000, dep1);
        Empleado e3 = new Empleado("Maria 3", "Cargo 1", 3000, dep1);
        Empleado e4 = new Empleado("Jose 4", "Cargo 3", 4000, dep1);
        Empleado e5 = new Empleado("Alicia 5", "Cargo 2", 5000, dep1);

        dep1.empleados.add(e1);
        dep1.empleados.add(e2);
        dep1.empleados.add(e3);
        dep1.empleados.add(e4);
        dep1.empleados.add(e5);

        // Mostrar departamentos
        dep1.mostrarEmpleados();
        dep2.mostrarEmpleados();

        // Cambiar salario
        dep1.cambioSalario(1500);

        dep1.mostrarEmpleados();
        dep2.mostrarEmpleados();

        // Verificar dep1 ↔ dep2
        dep1.verificarDep1(dep2);

        // Mover empleados de dep1 a dep2
        dep1.moverEmpleados(dep2);

        dep1.mostrarEmpleados();
        dep2.mostrarEmpleados();
    }
}
