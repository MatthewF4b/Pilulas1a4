from semaforo import acao_semaforo


def test_cor_vermelho():
    assert acao_semaforo("vermelho") == "Pare"


def test_cor_amarelo():
    assert acao_semaforo("amarelo") == "Atenção"


def test_cor_verde():
    assert acao_semaforo("verde") == "Siga"


def test_cor_invalida():
    assert acao_semaforo("azul") == "Cor inválida"
