
from codigo.main import obter_ambiente, executar


def test_obter_ambiente(monkeypatch):
    monkeypatch.setenv("AMBIENTE", "producao")

    assert obter_ambiente() == "producao"


def test_ambiente_padrao(monkeypatch):
    monkeypatch.delenv("AMBIENTE", raising=False)

    assert obter_ambiente() == "desenvolvimento"


def test_executar():
    assert executar() is True
