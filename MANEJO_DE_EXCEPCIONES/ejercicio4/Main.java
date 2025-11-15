package MANEJO_DE_EXCEPCIONES.ejercicio4;

public class Main {
    public static void main(String[] args) {

        Inventario inv = new Inventario();

        try {
            inv.agregarProducto(new Producto("P01", "Mouse", 50, 10));
            inv.agregarProducto(new Producto("P02", "Teclado", 120, 5));

            inv.mostrarInventario();

            Producto p = inv.buscarProducto("P01");
            System.out.println("Producto encontrado: " + p.getNombre());

            inv.venderProducto("P01", 3);

            inv.mostrarInventario();

            inv.venderProducto("P02", 10);

        } catch (ProductoNoEncontradoException e) {
            System.out.println("ERROR: " + e.getMessage());

        } catch (StockInsuficienteException e) {
            System.out.println("ERROR: " + e.getMessage());

        } catch (Exception e) {
            System.out.println("ERROR GENERAL: " + e.getMessage());
        }
    }
}

