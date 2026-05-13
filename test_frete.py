from frete import calcular_frete


def test_frete_ate_um_quilo():
    assert calcular_frete(1.0) == 5


def test_frete_entre_um_e_cinco_quilos():
    assert calcular_frete(1.01) == 10
    assert calcular_frete(5.0) == 10


def test_frete_acima_de_cinco_quilos():
    assert calcular_frete(5.01) == 18


def test_frete_peso_zero():
    assert calcular_frete(0) == 0


def test_frete_peso_negativo():
    assert calcular_frete(-10) == 0
