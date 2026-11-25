
import os


def obter_ambiente():
    ambiente = os.getenv("AMBIENTE", "desenvolvimento")
    return ambiente


def executar():
    ambiente = obter_ambiente()

    print("================================")
    print(" Projeto DevSecOps")
    print("================================")
    print(f"Ambiente: {ambiente}")
    print("Análise de segurança automatizada")
    print("================================")

    return True


if __name__ == "__main__":
    executar()
