from conceito import converter_nota_para_conceito


def test_conceito_a():
    assert converter_nota_para_conceito(9.0) == "A"


def test_conceito_b():
    assert converter_nota_para_conceito(8.9) == "B"


def test_conceito_c():
    assert converter_nota_para_conceito(5.0) == "C"


def test_conceito_d():
    assert converter_nota_para_conceito(4.9) == "D"


def test_conceito_f():
    assert converter_nota_para_conceito(2.0) == "F"


def test_nota_invalida():
    assert converter_nota_para_conceito(-1) == "Nota inválida"
    assert converter_nota_para_conceito(11) == "Nota inválida"
