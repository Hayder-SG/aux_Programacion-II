package INTRODUCCIÓN_A_LA_PROGRAMACIÓN_ORIENTADA_A_OBJETOS.ejercicio3.Java;

public class Producto {
    public String nombre;
    public double precio;
    public int stock;

    public Producto(String nombre, double precio, int stock) {
        this.nombre = nombre;
        this.precio = precio;
        this.stock = stock;
    }

    public void vender(int cantidad) {
        if (cantidad <= this.stock) {
            this.stock -= cantidad;
            double totalVenta = cantidad * this.precio;
            System.out.println("Se han vendido " + cantidad + " unidades de " + this.nombre +
                    ". Total: Bs. " + String.format("%.2f", totalVenta));
        } else {
            System.out.println("No hay suficiente stock de " + this.nombre +
                    ". Stock disponible: " + this.stock);
        }
    }

    public void reabastecer(int cantidad) {
        this.stock += cantidad;
        System.out.println("Se han reabastecido " + cantidad + " unidades de " + this.nombre +
                ". Stock actual: " + this.stock);
    }

    public static void main(String[] args) {
        Producto producto = new Producto("Camiseta", 25.0, 100);

        producto.vender(20);
        producto.reabastecer(50);
        producto.vender(150);
    }
}
