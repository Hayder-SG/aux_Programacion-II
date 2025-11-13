package POLIMOSFISMO.ejercicio5.Java;

public class Main {
    public static void main(String[] args) {
        Celular cel = new Celular(77712345, "Yeider", 64.0f, 4, 20);

        System.out.println("=== Datos antes de aplicar operadores ===");
        cel.mostrarDatos();

        cel.operatorPlusPlus();

        cel.operatorMinusMinus();

        System.out.println("=== Datos después de aplicar operadores ===");
        cel.mostrarDatos();
    }
}
