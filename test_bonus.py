from bonus import calcular_bonus


def test_bonus_excelente():
    assert calcular_bonus(5000, "Excelente") == 1000


def test_bonus_bom():
    assert calcular_bonus(3000, "Bom") == 300


def test_bonus_regular():
    assert calcular_bonus(2000, "Regular") == 40


def test_bonus_ruim():
    assert calcular_bonus(4000, "Ruim") == 0.0


def test_bonus_salario_negativo():
    assert calcular_bonus(-1000, "Excelente") == 0.0


def test_bonus_avaliacao_invalida():
    assert calcular_bonus(5000, "Mais ou Menos") == 0.0
