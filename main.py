import os
from datetime import datetime
import pandas as pd


def processar_dados(itens: list[dict]) -> pd.DataFrame:
    """Converte uma lista de dicionários em DataFrame e calcula o valor total."""
    if not itens:
        raise ValueError("A lista de itens não pode estar vazia.")

    df = pd.DataFrame(itens)
    df["total"] = df["quantidade"] * df["preco_unitario"]
    return df


def main() -> None:
    ambiente = os.getenv("AMBIENTE", "desenvolvimento")
    inicio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{inicio}] Iniciando execução no ambiente: {ambiente.upper()}")

    dados_exemplo = [
        {"produto": "Servidor EC2", "quantidade": 3, "preco_unitario": 120.50},
        {"produto": "Bucket S3", "quantidade": 5, "preco_unitario": 25.00},
        {"produto": "Load Balancer", "quantidade": 1, "preco_unitario": 85.00},
    ]

    resultado = processar_dados(dados_exemplo)
    custo_geral = resultado["total"].sum()

    print("\nResumo do processamento:")
    print(resultado.to_string(index=False))
    print(f"\nCusto Total Calculado: R$ {custo_geral:.2f}")


if __name__ == "__main__":
    main()
