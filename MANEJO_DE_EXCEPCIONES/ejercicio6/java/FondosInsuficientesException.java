package MANEJO_DE_EXCEPCIONES.ejercicio6.java;

public class FondosInsuficientesException extends Exception {
    public FondosInsuficientesException(String mensaje) {
        super(mensaje);
    }
}