package MANEJO_DE_EXCEPCIONES.ejercicio4;

import java.util.ArrayList;

public class Inventario {
    private ArrayList<Producto> productos;

    public Inventario() {
        productos = new ArrayList<>();
    }

    // c) Agregar Producto
    public void agregarProducto(Producto p) throws Exception {
        // Validar código repetido
        for (Producto prod : productos) {
            if (prod.getCodigo().equals(p.getCodigo())) {
                throw new Exception("El código ya existe: " + p.getCodigo());
            }
        }

        // Validar valores negativos
        if (p.getPrecio() < 0 || p.getStock() < 0) {
            throw new Exception("Precio o stock no pueden ser negativos.");
        }

        productos.add(p);
    }

    // d) Buscar Producto
    public Producto buscarProducto(String codigo) throws ProductoNoEncontradoException {
        for (Producto p : productos) {
            if (p.getCodigo().equals(codigo)) {
                return p;
            }
        }
        throw new ProductoNoEncontradoException("Producto no encontrado: " + codigo);
    }

    // e) Vender Producto
    public void venderProducto(String codigo, int cantidad)
            throws ProductoNoEncontradoException, StockInsuficienteException {

        Producto p = buscarProducto(codigo);

        if (p.getStock() < cantidad) {
            throw new StockInsuficienteException("Stock insuficiente. Disponible: " + p.getStock());
        }

        p.setStock(p.getStock() - cantidad);
        System.out.println("Venta realizada. Stock actual: " + p.getStock());
    }

    public void mostrarInventario() {
        System.out.println("=== INVENTARIO ===");
        for (Producto p : productos) {
            p.mostrar();
        }
    }
}

