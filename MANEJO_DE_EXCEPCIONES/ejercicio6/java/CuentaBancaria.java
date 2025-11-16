package MANEJO_DE_EXCEPCIONES.ejercicio6.java;

public class CuentaBancaria {
    private String numeroCuenta;
    private String titular;
    private double saldo;

    public CuentaBancaria(String numeroCuenta, String titular, double saldo) {
        this.numeroCuenta = numeroCuenta;
        this.titular = titular;
        this.saldo = saldo;
    }

    public void depositar(double monto) {
        if (monto <= 0) {
            throw new IllegalArgumentException("El monto a depositar debe ser positivo.");
        }
        saldo += monto;
        System.out.println("Depósito realizado: " + monto + ". Nuevo saldo: " + saldo);
    }

    public void retirar(double monto) throws FondosInsuficientesException {
        if (monto > saldo) {
            throw new FondosInsuficientesException(
                "Fondos insuficientes. Saldo disponible: " + saldo + ", intento de retiro: " + monto
            );
        }
        saldo -= monto;
        System.out.println("Retiro realizado: " + monto + ". Saldo restante: " + saldo);
    }

    public void mostrarInfo() {
        System.out.println("=== Información de la Cuenta ===");
        System.out.println("Número de cuenta: " + numeroCuenta);
        System.out.println("Titular: " + titular);
        System.out.println("Saldo: " + saldo);
        System.out.println("===============================");
    }
}