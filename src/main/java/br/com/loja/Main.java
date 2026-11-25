package br.com.loja;

public class Main {

    public static void main(String[] args) {

        CalculadoraCompra calculadora =
            new CalculadoraCompra();

        double total =
            calculadora.calcularTotal(1000, 10);

        System.out.println(
            "Valor final da compra: R$ " + total
        );
    }
}
