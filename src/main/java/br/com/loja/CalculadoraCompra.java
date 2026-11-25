package br.com.loja;

public class CalculadoraCompra {

    public double calcularTotal(
            double valor,
            double percentualDesconto) {

        if (valor < 0) {
            throw new IllegalArgumentException(
                "O valor não pode ser negativo"
            );
        }

        if (percentualDesconto < 0 ||
            percentualDesconto > 100) {

            throw new IllegalArgumentException(
                "Desconto deve estar entre 0 e 100"
            );
        }

        double desconto =
            valor * percentualDesconto / 100;

        return valor - desconto;
    }
}
