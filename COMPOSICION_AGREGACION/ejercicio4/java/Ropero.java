package COMPOSICION_AGREGACION.ejercicio4.java;

import java.util.ArrayList;

public class Ropero {
    private String material;
    private ArrayList<Ropa> ropa;
    private int nroRopas;

    public Ropero(String material) {
        this.material = material;
        this.ropa = new ArrayList<>();
        this.nroRopas = 0;
    }

    public void agregarPrenda(Ropa prenda) {
        ropa.add(prenda);
        nroRopas++;
    }

    public void agregarNPrendas(int cantidad, Ropa prenda) {
        for (int i = 0; i < cantidad; i++) {
            ropa.add(prenda);
        }
        nroRopas = ropa.size();
    }

    public void eliminarTipoXMaterialX(String tipo, String material) {
        System.out.println("Las prendas eliminadas son:");
        int eliminadas = 0;

        ArrayList<Ropa> nuevas = new ArrayList<>();

        for (Ropa r : ropa) {
            boolean eliminar = false;

            if (tipo != null && !tipo.isEmpty() && r.getTipo().equals(tipo)) {
                eliminar = true;
            }

            if (material != null && !material.isEmpty() && r.getMaterial().equals(material)) {
                eliminar = true;
            }

            if (eliminar) {
                System.out.println("\tRopa eliminada: " + r.getTipo() + " - " + r.getMaterial());
                eliminadas++;
            } else {
                nuevas.add(r);
            }
        }

        ropa = nuevas;
        nroRopas = ropa.size();

        System.out.println("Número de prendas eliminadas: " + eliminadas);
        System.out.println("===========================================");
    }

    public void mostrarTipoMaterial(String tipo, String material) {
        System.out.println("\nPrendas de tipo '" + tipo + "' y material '" + material + "':");
        int count = 0;

        for (Ropa r : ropa) {
            if (r.getTipo().equals(tipo) && r.getMaterial().equals(material)) {
                r.mostrar();
                count++;
            }
        }

        System.out.println("Total encontradas: " + count);
        System.out.println("===========================================");
    }

    public void mostrarRopa() {
        System.out.println("\nLas prendas de mi ropero de " + material + " son:");
        for (Ropa r : ropa) {
            r.mostrar();
        }
        System.out.println("Total de prendas: " + nroRopas);
        System.out.println("===========================================");
    }
}
