package POLIMOSFISMO.ejercicio5.Java;

public class Celular {
    private int nroTelefono;
    private String dueño;
    private float espacio; 
    private int ram; 
    private int nroApp;

    public Celular(int nroTelefono, String dueño, float espacio, int ram, int nroApp) {
        this.nroTelefono = nroTelefono;
        this.dueño = dueño;
        this.espacio = espacio;
        this.ram = ram;
        this.nroApp = nroApp;
    }

    public void operatorPlusPlus() {
        nroApp += 10;
        System.out.println("📱 Se agregaron 10 aplicaciones.");
    }

    public void operatorMinusMinus() {
        espacio -= 5;
        if (espacio < 0) espacio = 0;
        System.out.println("⚙️ Se redujo el espacio en 5 GB.");
    }
    public void mostrarDatos() {
        System.out.println("Dueño: " + dueño);
        System.out.println("Número: " + nroTelefono);
        System.out.println("RAM: " + ram + " GB");
        System.out.println("Espacio: " + espacio + " GB");
        System.out.println("Número de Apps: " + nroApp);
        System.out.println("----------------------------------");
    }
    public void agregarApp() {
        nroApp += 10;
    }
}

