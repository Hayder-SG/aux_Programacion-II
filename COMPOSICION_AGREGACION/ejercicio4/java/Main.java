package COMPOSICION_AGREGACION.ejercicio4.java;

public class Main {
    public static void main(String[] args) {

        Ropero rop = new Ropero("Sintético");

        Ropa ropa1 = new Ropa("Camisa", "Algodón");
        Ropa ropa2 = new Ropa("Pantalón", "Lino");
        Ropa ropa3 = new Ropa("Pantalón", "Algodón");
        Ropa ropa4 = new Ropa("Saco", "Polipropileno");

        rop.agregarPrenda(ropa1);
        rop.agregarPrenda(ropa2);
        rop.agregarPrenda(ropa3);

        rop.agregarNPrendas(3, ropa4);
        rop.agregarNPrendas(2, ropa1);

        rop.mostrarRopa();

        rop.agregarNPrendas(2, ropa3);

        rop.mostrarRopa();

        rop.eliminarTipoXMaterialX("Camisa", "");

        rop.mostrarRopa();

        rop.mostrarTipoMaterial("Pantalón", "Algodón");
    }
}
