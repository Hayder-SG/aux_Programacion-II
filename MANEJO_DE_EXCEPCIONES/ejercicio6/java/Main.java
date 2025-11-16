package MANEJO_DE_EXCEPCIONES.ejercicio6.java;

public class Main {
    public static void main(String[] args) {

        CuentaBancaria cuenta = new CuentaBancaria("12345", "Juan Pérez", 1000);
        cuenta.mostrarInfo();

        try {
            cuenta.depositar(500); 
            cuenta.depositar(-100); 
        } catch (IllegalArgumentException e) {
            System.out.println("ERROR: " + e.getMessage());
        }

        try {
            cuenta.retirar(300);
            cuenta.retirar(1500);
        } catch (FondosInsuficientesException e) {
            System.out.println("ERROR: " + e.getMessage());
        }

        cuenta.mostrarInfo();
    }
}

