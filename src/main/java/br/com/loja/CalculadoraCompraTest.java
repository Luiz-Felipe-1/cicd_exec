package br.com.loja;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CalculadoraCompraTest {

    @Test
    void deveCalcularDescontoDeDezPorCento() {

        CalculadoraCompra calculadora =
            new CalculadoraCompra();

        double resultado =
            calculadora.calcularTotal(1000, 10);

        assertEquals(900.0, resultado, 0.001);
    }

    @Test
    void deveRetornarValorOriginalSemDesconto() {

        CalculadoraCompra calculadora =
            new CalculadoraCompra();

        double resultado =
            calculadora.calcularTotal(500, 0);

        assertEquals(500.0, resultado, 0.001);
    }

    @Test
    void naoDeveAceitarDescontoMaiorQueCem() {

        CalculadoraCompra calculadora =
            new CalculadoraCompra();

        assertThrows(
            IllegalArgumentException.class,
            () -> calculadora.calcularTotal(1000, 150)
        );
    }
}
