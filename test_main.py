import pytest
from main import processar_dados


def test_processar_dados_calculo_correto():
    entrada = [
        {"produto": "Item A", "quantidade": 2, "preco_unitario": 50.0},
        {"produto": "Item B", "quantidade": 4, "preco_unitario": 10.0},
    ]
    df = processar_dados(entrada)

    assert len(df) == 2
    assert df["total"].tolist() == [100.0, 40.0]
    assert df["total"].sum() == 140.0


def test_processar_dados_lista_vazia():
    with pytest.raises(ValueError, match="não pode estar vazia"):
        processar_dados([])
